#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os,re
from jinja2 import Environment,FileSystemLoader
from modules.common import email as Mail
from pprint import pprint

accountid='150812941021'
client = boto3.client('quicksight')
response1 = client.list_dashboards(AwsAccountId=accountid)

dashboardinfo = []
for i in response1['DashboardSummaryList']:
    dashboardarn = i['Arn']
    dashboardid = i['DashboardId']
    dashboardname = i['Name']
    print(dashboardarn,dashboardid,dashboardname)
