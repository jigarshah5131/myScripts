#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os,re,json
from pprint import pprint

accountid='150812941021'
client = boto3.client('quicksight')
response1 = client.list_dashboards(AwsAccountId=accountid)

dashboardinfo = {}
dashboard_list = []
for list in response1['DashboardSummaryList']:
    dashboard = {list['Name'] : {'DashboardName' : list['Name'] , 'DashboardId' : list['DashboardId']}}
#    dashboard = { 'DashboardName' : list['Name'] , 'DashboardId' : list['DashboardId']}
    dashboard_list.append(dashboard)
print(dashboard_list)
dashboardinfo['dashboards'] = dashboard_list
print(dashboardinfo)
#J
#for item in dashboard_list:
#    DashboardName = item['DashboardName']
#    dashboardinfo[DashboardName] = item
#print(type(dashboardinfo))
#print(dashboardinfo.items())


#Jdashboardinfo["dashboards"] = dashboard_list
jsondash = json.dumps(dashboardinfo,indent=4,sort_keys=True)
#J#jsondash = json.dumps(dashboard_list,indent=4,sort_keys=True)
json_file =  open('dashmetadata2.txt','w')
print (jsondash,file=json_file)
json_file.close()
#J
#Jf = open('dashmetadata2.txt','r')
#J
#Jjdata = json.load(f)
#Jprint(jdata)
#J
#J#for k in jdata:
#J#  for j,v in k.items():
#J#     print(j,'->',v)
