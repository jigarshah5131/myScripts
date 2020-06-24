#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os,re,itertools,json
from collections import OrderedDict
from jinja2 import Environment,FileSystemLoader
#from modules.common import email as Mail
from operator import itemgetter
from pprint import pprint
from collections import defaultdict

accountid='150812941021'
client = boto3.client('quicksight')

response = client.list_dashboards(AwsAccountId=accountid)
dashboards = []
for i in response['DashboardSummaryList']:
  dashboard = {i['Name'] : i['DashboardId']}
  dashboards.append(dashboard)

dashboardmap = {}
#dashboardmap = OrderedDict()
for dashmap in dashboards:
  for dashboard in dashmap:
    response1 = client.describe_dashboard_permissions(AwsAccountId=accountid,DashboardId=dashmap[dashboard])
    for key in response1:
      if 'DashboardId' in key:
        for d in response1['Permissions']:
          #print(d['Principal'])
          if dashboard not in dashboardmap.keys():
               dashboardmap[dashboard] = []
          username = re.search('default/(.*)',d['Principal']).group(1)
          print(username)
