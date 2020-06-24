#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os,re
from jinja2 import Environment,FileSystemLoader

#accountid='150812941021'

client = boto3.client('quicksight')
prodacctid='150812941021'


for line in sys.stdin:
  fields = line.strip().split(":")
  un = fields[0]
  email = fields[1]
  role = fields[2]
  print(f'deleting user {un} email address {email} and role {role}')
  response = client.delete_user(UserName=un,AwsAccountId='150812941021',Namespace='default')
