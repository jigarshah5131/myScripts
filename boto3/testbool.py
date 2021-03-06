#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os,re
boto3path = os.path.expanduser('~/boto3')
sys.path.append(boto3path)
from jinja2 import Environment,FileSystemLoader
from modules.common import email as Mail

accountid='150812941021'
client = boto3.client('quicksight')
response1 = client.list_dashboards(AwsAccountId=accountid)
reportfile = 'dashboardinfo.html'

title = 'Quicksight Dashboard Security information'

mailcmd = "mailx -a " + reportfile + " -s 'Dashboardinfo' mari.baz@accenturefederal.com < /dev/null"

dashboardinfo = []
for i in response1['DashboardSummaryList']:

  response2 = client.describe_dashboard_permissions(AwsAccountId=accountid,DashboardId=i['DashboardId'])

  for j in response2['Permissions']:

    permissions = list(str(j['Actions']).replace('quicksight:','').replace("'",'').replace("[",'').replace("]",'').replace(" ",'').split(","))
    permissions = ("-".join(permissions))
    username = re.search ('default/(.*)',j['Principal']).group(1)
    response3 = client.describe_user(AwsAccountId=accountid,Namespace='default',UserName=username)
    role = response3['User']['Role']
    dashboardname = i['Name']
    status = response3['User']['Active']
    status = str(status).replace('True','Active').replace('False','INACTIVE')
    email = response3['User']['Email']
    color="black"
    bcolor="cornsilk"
    if status is False:
      color="white"
      bcolor="red"


    jsondata  = {
    'DashboardName' : dashboardname,
    'UserName' : username,
    'Role' : role,
    'Status' : status,
    'Email' : email,
    'DashboardPermissions' : permissions,
    'color' : str(color),
    'bcolor' : str(bcolor)
    }
    dashboardinfo.append(jsondata)

print(dashboardinfo)
