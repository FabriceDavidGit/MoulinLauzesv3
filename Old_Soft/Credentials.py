# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError
import json

def get_secret():

    secret_name = "rds!db-9fa8189e-47a9-4721-b370-edf2db66f0c0"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # secret = get_secret_value_response['SecretString']
    secret = json.loads(get_secret_value_response['SecretString'])
    username = str(secret['username'])
    password = str(secret['password'])
    print (username)
    print (password)
    # Your code goes here.


get_secret()