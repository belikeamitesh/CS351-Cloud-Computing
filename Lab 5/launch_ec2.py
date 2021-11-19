import boto3

access_id_key = "ACCESS ID KEY"
secret_access_key = "SECRET ACCESS KEY"
session_token_key = "SECRET TOKEN KEY"

ec2 = boto3.resource(
    "ec2",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)

instances = ec2.create_instances(
    ImageId="IMAGE ID",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="CS351-CG31-KP",
    SecurityGroupIds=["SG GROUP ID"],
    UserData=open(
        "/home/amitesh/Desktop/Semester 5/lab5-cloud/lab5/startup_script.sh"
    ).read(),
)


print(instances)


instance = instances[0]
instance.wait_until_running()
instance.load()

print(instance.public_dns_name)
