#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os,re,itertools,json
from collections import OrderedDict
from jinja2 import Environment,FileSystemLoader
from modules.common import email as Mail
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
          if dashboard not in dashboardmap.keys():
            dashboardmap[dashboard] = []
          dashboardmap[dashboard].append(  
                                         {
                                          'DashboardID'   : response1[key], 
                                          'DashboardName' : dashboard, 
                                          'Username': re.search('default/(.*)',d['Principal']).group(1),
                                          'Permissions' : d['Actions']
                                         }
                                        )
pprint(dashboardmap)
jsondash = json.dumps(dashboardmap,indent=4,sort_keys=True)
with open('dashmetadatafinal','w') as json_file:
  json_file.write(jsondash)

"""
for k,value in itertools.groupby (dashboardmap, key=itemgetter('Name')): 
   print(k)
   print("========")
   for i in value:
      print(i.get('Username'))
#pprint(dashboardmap)
"""
"""
for i in dashboardmap:
   for j in dashboardmap[i]:
     print(j['Name'] , j['Username'])
"""
