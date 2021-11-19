import boto3


startup_script = '''#!/bin/bash
sudo yum update -y
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
cd /var/www/html
rm index.html
wget "bucket link here"
'''


def createInstance() -> str:
    try:
        print('Creating Instance!')
        ec2 = boto3.resource('ec2')
        response = ec2.create_instances(
            ImageId='IMAGE_ID',
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName='CS351-CG31-KP',
            SecurityGroupIds=['SECURITY_GROUP'],
            UserData=startup_script)
        instance = response[0]
        print('Instance created! Now waiting to be in running state..')
        instance.wait_until_running()
        print('Successful ! Instance in running!')
        instance.load()
        print('Your public DNS address: ', get_name(instance))
    except Exception as e:
        print(e)


def get_name(inst):
    client = boto3.client('ec2')
    response = client.describe_instances(InstanceIds=[inst.instance_id])
    result = response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicDnsName']
    return result


createInstance()