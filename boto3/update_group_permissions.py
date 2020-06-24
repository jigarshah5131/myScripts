#!/home/oracle/environments/my_env/bin/python

import boto3,pprint,sys,os,re,json
from pprint import pprint

accountid='150812941021'
client = boto3.client('quicksight')


#with open('dashmetadatafinalfull.save','r') as f:
#with open('dashmetadatanewusers','r') as f:
#  dashdata = json.load(f)

#for mainkey in dashdata:
#    for items in dashdata[mainkey]:
##        if 'accenturefederal' in items['Email']:
#          dashboardid = items['DashboardID']
#userarn = "arn:aws:quicksight:us-east-1:150812941021:group/default/SMLeads"
#userarn = "arn:aws:quicksight:us-east-1:150812941021:group/default/QSPaymentGroup"
#userarn = "arn:aws:quicksight:us-east-1:150812941021:group/default/QSSBEGroup"
userarn = "arn:aws:quicksight:us-east-1:150812941021:group/default/QSAuthorsGroup"
actionlist = ["quicksight:DescribeDashboard", "quicksight:ListDashboardVersions", "quicksight:QueryDashboard"]
#          if dashboardid not in dashboardidmap.keys():
#            dashboardidmap[dashboardid] = []
#dashboardidmap[dashboardid].append({ 'Principal' : userarn , 'Actions'   : actionlist })
#response = client.update_dashboard_permissions( AwsAccountId=accountid, DashboardId='8a7f8f46-a252-415e-8f06-a12eefc0a55b', GrantPermissions = [{ 'Principal' : userarn , 'Actions'   : actionlist }])
#print(response)
response = client.update_dashboard_permissions( AwsAccountId=accountid, DashboardId='858c3991-169a-441e-95a7-e05ddcfef83f', GrantPermissions = [{ 'Principal' : userarn , 'Actions'   : actionlist }])
#print(response)
#response = client.update_dashboard_permissions( AwsAccountId=accountid, DashboardId='f685fbf4-6a48-4731-acd7-c36cf9763648', GrantPermissions = [{ 'Principal' : userarn , 'Actions'   : actionlist }])
#response = client.update_dashboard_permissions( AwsAccountId=accountid, DashboardId='99a06aff-8674-4d6c-9010-345024111029', GrantPermissions = [{ 'Principal' : userarn , 'Actions'   : actionlist }])
#response = client.update_dashboard_permissions( AwsAccountId=accountid, DashboardId='b70a01ac-7ef4-465b-aed8-fe833f05bf0e', GrantPermissions = [{ 'Principal' : userarn , 'Actions'   : actionlist }])
#print(response)
#response = client.update_dashboard_permissions( AwsAccountId=accountid, DashboardId='1f2f0015-db28-449e-816c-4d0c5518b614', GrantPermissions = [{ 'Principal' : userarn , 'Actions'   : actionlist }])
#response = client.update_dashboard_permissions( AwsAccountId=accountid, DashboardId='189edae1-6841-4e69-bacf-0a207ce65336', GrantPermissions = [{ 'Principal' : userarn , 'Actions'   : actionlist }])
print(response)

#arn:aws:quicksight:us-east-1:150812941021:dashboard/858c3991-169a-441e-95a7-e05ddcfef83f 858c3991-169a-441e-95a7-e05ddcfef83f Reference Data
#arn:aws:quicksight:us-east-1:150812941021:dashboard/a281bea3-46f1-4c89-84a6-5f5b49230cd9 a281bea3-46f1-4c89-84a6-5f5b49230cd9 EAPS
#arn:aws:quicksight:us-east-1:150812941021:dashboard/8a7f8f46-a252-415e-8f06-a12eefc0a55b 8a7f8f46-a252-415e-8f06-a12eefc0a55b Reference Data:ProdR
#arn:aws:quicksight:us-east-1:150812941021:dashboard/f685fbf4-6a48-4731-acd7-c36cf9763648 f685fbf4-6a48-4731-acd7-c36cf9763648 PPM:ProdR
#arn:aws:quicksight:us-east-1:150812941021:dashboard/b70a01ac-7ef4-465b-aed8-fe833f05bf0e b70a01ac-7ef4-465b-aed8-fe833f05bf0e SBE Data Quality:ProdR
#arn:aws:quicksight:us-east-1:150812941021:dashboard/99a06aff-8674-4d6c-9010-345024111029 99a06aff-8674-4d6c-9010-345024111029 PPM
#arn:aws:quicksight:us-east-1:150812941021:dashboard/189edae1-6841-4e69-bacf-0a207ce65336 189edae1-6841-4e69-bacf-0a207ce65336 EDGE
#arn:aws:quicksight:us-east-1:150812941021:dashboard/1f2f0015-db28-449e-816c-4d0c5518b614 1f2f0015-db28-449e-816c-4d0c5518b614 SBE Data Quality
