import boto3


# aws configuration
access_id_key = ""
secret_access_key = ""
session_token_key = ""


rdsClient = boto3.client(
    "rds",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)

response = rdsClient.create_db_instance(
    DBName="amitesh",
    DBInstanceIdentifier="amitesh",
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    Engine="MySQL",
    MasterUsername="amiteshkumar",
    MasterUserPassword="amiteshkumar",
    PubliclyAccessible=True,
)


import time

while True:
    response = rdsClient.describe_db_instances(
        DBInstanceIdentifier="amitesh",
        MaxRecords=20,
    )

    status = response["DBInstances"][0]["DBInstanceStatus"]

    if status == "available" or status == "AVAILABLE":
        break
    else:
        time.sleep(10)


print(response["DBInstances"][0]["Endpoint"]["Address"])
