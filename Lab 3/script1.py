import boto3


startup_script = '''#!/bin/bash
sudo yum update -y
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
cd /var/www/html
sudo rm index.html
sudo wget "bucket link"
'''

def createAutoScalingGroup():
    client = boto3.client('autoscaling')
    try:
        print("Creating launch configuration...\n")
        # A launch configuration is an instance configuration template that an Auto Scaling group uses to launch EC2 instances.
        launch_config = client.create_launch_configuration(
            LaunchConfigurationName="launch-config-as",
            ImageId='IMAGE_ID',
            InstanceType='t2.micro',
            KeyName='CS351-CG31-KP',
            SecurityGroups=[
                'SECURITY_GROUP'
            ],
            UserData=startup_script
        )
    except Exception as e:
        print(e)

    try:
        print("Creating auto scaling group...\n")
        auto_scaling_group = client.create_auto_scaling_group(
            AutoScalingGroupName="auto-scaling-group",
            LaunchConfigurationName="launch-config-as",
            MinSize=1,#minimum size of the group - number of instances
            MaxSize=3,
            VPCZoneIdentifier='subnet-e67a55c7'#virtual private cloud 
        )
    except Exception as e:
        print(e)

    try:
        print("Adding ScaleUp Policy...\n")
        # Creates or updates a scaling policy for an Auto Scaling group.
        # Scaling policies are used to scale an Auto Scaling group based on configurable metrics.
        scale_up_policy = client.put_scaling_policy(
            AutoScalingGroupName="auto-scaling-group",
            PolicyName="ScaleUp",
            ScalingAdjustment=1,# A positive value adds to the current capacity while a negative number removes from the current capacity. 
            AdjustmentType="ChangeInCapacity"
            # Specifies how the scaling adjustment is interpreted (for example, an absolute number or a percentage).
            # The valid values are ChangeInCapacity , ExactCapacity , and PercentChangeInCapacity .
        )
    except Exception as e:
        print(e)

    try:
        print("Adding ScaleDown Policy...\n")
        scale_down_policy = client.put_scaling_policy(
            AutoScalingGroupName="auto-scaling-group",
            PolicyName="ScaleDown",
            ScalingAdjustment=-1,
            AdjustmentType="ChangeInCapacity"
        )
    except Exception as e:
        print(e)
        
    # Amazon CloudWatch is a monitoring and management service that provides data and actionable insights for AWS,
    # hybrid, and on-premises applications and infrastructure resources. 
    cloudwatch = boto3.client('cloudwatch')

    try:
        print("Putting Alarm metrics in place..\n")
        # Creates or updates an alarm and associates it with the specified metric, metric math expression, or anomaly detection model.
        cloudwatch.put_metric_alarm(
            AlarmName='high_CPU_Utilization',
            # The arithmetic operation to use when comparing the specified statistic and threshold. 
            ComparisonOperator='GreaterThanThreshold',
            EvaluationPeriods=2,
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Period=120,
            Statistic='Average',
            # The value against which the specified statistic is compared.
            Threshold=80.0,
            AlarmDescription='Alarm when server CPU exceeds 80%',
            Dimensions=[
                {
                'Name': 'AutoScalingGroupName',
                'Value': 'auto-scaling-group'
                },
            ],
            Unit='Seconds'
        )
    except Exception as e:
        print(e)

    try:
        cloudwatch.put_metric_alarm(
            AlarmName='low_CPU_Utilization',
            ComparisonOperator='LessThanThreshold',
            EvaluationPeriods=2,
            # The name for the metric associated with the alarm.
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Period=120,
            Statistic='Average',
            Threshold=20.0,
            AlarmDescription='Alarm when server CPU is below 20%',
            # The dimensions for the metric specified in MetricName .
            Dimensions=[
                {
                'Name': 'AutoScalingGroupName',
                'Value': 'auto-scaling-group'
                },
            ],
            Unit='Seconds'
        )
    except Exception as e:
        print(e)

createAutoScalingGroup()