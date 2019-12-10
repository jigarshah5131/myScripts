#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,re

client = boto3.client('iam')
#response = client.get_role(RoleName='rds-s3-integration-role')
response = client.get_role(RoleName='rds-s3-integration-role')
pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(response['Role'])

roles=response['Role']

for key,value in roles.items():
   if 'Arn' in key:
#    print(value)
     new_val=value

print()
print(new_val)
print()

#client=boto3.client('rds')



#try:
# response = client.add_role_to_db_instance(
#    DBInstanceIdentifier='imp2-dz-oracle01-rds',
#    RoleArn=new_val,
#    FeatureName='S3_INTEGRATION'
# )
##except Exception as error:
#  print(error)
