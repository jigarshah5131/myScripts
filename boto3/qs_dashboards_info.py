#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os,re
from jinja2 import Environment,FileSystemLoader
from pprint import pprint
from modules.common import email as Mail

accountid='150812941021'
client = boto3.client('quicksight')
response1 = client.list_dashboards(AwsAccountId=accountid)
#reportfile = 'dashboardinfo.html'

#title = 'Quicksight Dashboard Security information'

#mailcmd = "mailx -a " + reportfile + " -s 'Dashboardinfo' jigar.b.shah@accenturefederal.com < /dev/null"

dashboardinfo = []
for i in response1['DashboardSummaryList']:

  response2 = client.describe_dashboard(AwsAccountId=accountid,DashboardId=i['DashboardId'])
  arn = response2['Dashboard'].get('Arn')
  name = response2['Dashboard'].get('Name')
  created = response2['Dashboard'].get('CreatedTime')
  lastpubtime = response2['Dashboard'].get('LastPublishedTime')
  lastupdtime = response2['Dashboard'].get('LastUpdatedTime')
  #dashboardinfo.append(str(arn) + "," + str(name)+","+str(created)+","+str(lastpubtime)+","+str(lastupdtime))
  #dashboardinfo.append(str(arn) + "," + str(name))
  dashboardinfo.append(str(name))
#  dashboardinfo.append(str(name)+str(created)+str(lastpubtime))
for each in dashboardinfo:
  print(each)
