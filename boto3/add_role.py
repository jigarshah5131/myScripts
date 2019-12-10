#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,re


client = boto3.client('rds')

try:
 response = client.add_role_to_db_instance(
    DBInstanceIdentifier='prodr-dz-oracle01-rds',
    RoleArn='arn:aws:iam::150812941021:role/rds-s3-integration-role',
    FeatureName='S3_INTEGRATION'
 )
except Exception as error:
  print(error)

#print(response)
