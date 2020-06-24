#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os,re
from modules.common import email as Mail

client = boto3.client('quicksight')
prodacctid='150812941021'


for line in sys.stdin:
  fields = line.strip().split(":")
  un = fields[0]
  email = fields[1]
  role = fields[2]
  print(f'creating user {un} email address {email} and role {role}')
  response = client.register_user(IdentityType='QUICKSIGHT',Email=email,UserRole=role,UserName=un,AwsAccountId=prodacctid,Namespace='default')
