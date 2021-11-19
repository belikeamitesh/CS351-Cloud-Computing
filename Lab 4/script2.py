import boto3

access_id_key = ""
secret_access_key = ""
session_token_key = ""

boto3client = boto3.client(
    "elasticbeanstalk",
    region_name="us-east-1",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
)


boto3client.create_application_version(
    ApplicationName="my-portfolio",
    AutoCreateApplication=True,
    Description="my-app-v1",
    Process=True,
    SourceBundle={
        "S3Bucket": "BUCKET_NAME",
        "S3Key": "labass4.zip",
    },
    VersionLabel="v1",
)

import time

while True:

    response = boto3client.describe_application_versions(
        ApplicationName="my-portfolio",
        VersionLabels=[
            "v1",
        ],
        MaxRecords=123,
    )

    if response["ApplicationVersions"][0]["Status"] != "PROCESSED":
        time.sleep(5)
    else:
        break

response = boto3client.create_environment(
    ApplicationName="my-portfolio-1",
    CNAMEPrefix="my-app-link-amitesh-098",
    EnvironmentName="my-env-1",
    SolutionStackName="64bit Amazon Linux 2 v5.4.5 running Node.js 14",
    VersionLabel="v1",
    OptionSettings=[
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "IamInstanceProfile",
            "Value": "aws-elasticbeanstalk-ec2-role",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "InstanceType",
            "Value": "t2.micro",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "EC2KeyName",
            "Value": "CS351-CG31-KP",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "ImageId",
            "Value": "IMAGE_ID",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "SecurityGroups",
            "Value": "CS351-CG31-SG",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "BreachDuration",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Statistic",
            "Value": "Average",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Unit",
            "Value": "Percent",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "EvaluationPeriods",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Period",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "UpperThreshold",
            "Value": "80",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "UpperBreachScaleIncrement",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "MeasureName",
            "Value": "CPUUtilization",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "LowerThreshold",
            "Value": "20",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "LowerBreachScaleIncrement",
            "Value": "-1",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "Availability Zones",
            "Value": "Any 2",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "MaxSize",
            "Value": "3",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "MinSize",
            "Value": "1",
        },
    ],
)
