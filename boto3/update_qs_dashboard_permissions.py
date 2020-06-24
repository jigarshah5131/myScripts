#!/home/oracle/environments/my_env/bin/python

import boto3,pprint,sys,os,re,json
from pprint import pprint

accountid='150812941021'
client = boto3.client('quicksight')


dashboardidmap = {}

with open('dashmetadatafinalfull.save','r') as f:
#with open('dashmetadatanewusers','r') as f:
  dashdata = json.load(f)

for mainkey in dashdata:
    for items in dashdata[mainkey]:
#        if 'accenturefederal' in items['Email']:
          dashboardid = items['DashboardID']
          userarn = "arn:aws:quicksight:us-east-1:150812941021:user/default/" + items['Username']
          actionlist = items['Permissions']
          if dashboardid not in dashboardidmap.keys():
            dashboardidmap[dashboardid] = []
          dashboardidmap[dashboardid].append({ 'Principal' : userarn ,
                          'Actions'   : actionlist
                        })
try:
 for key in dashboardidmap:
   for i in dashboardidmap[key]:
      username = re.search('default/(.*)',i['Principal']).group(1) 
      print("Granting Permissions for dashboard " + key + " to "+ username)
      response = client.update_dashboard_permissions( AwsAccountId=accountid, DashboardId=key, GrantPermissions = dashboardidmap[key])
      for j in response:
#         print(response['DashboardArn'],response['DashboardId'],response['Permissions'])
        if 'Permissions' in j:
          for k in response['Permissions']:
            if username in  k['Principal']:
              createduser = re.search('default/(.*)',k['Principal']).group(1)
              print("\tUser " + createduser + " has been granted permissions " + str(k['Actions']), end="\n\n")
except Exception as e:
 print(e)
