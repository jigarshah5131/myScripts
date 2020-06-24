#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os,re
from jinja2 import Environment,FileSystemLoader
from pprint import pprint
from modules.common import email as Mail

accountid='150812941021'
client = boto3.client('quicksight')
response1 = client.list_data_sets(AwsAccountId=accountid)
#reportfile = 'dashboardinfo.html'
#pprint(response1['DataSetSummaries'])
for dataset in response1['DataSetSummaries']:
  #print(dataset['Arn'],dataset['Name'],dataset['CreatedTime'].strftime("%Y-%m-%d %H:%M:%S"),dataset['LastUpdatedTime'].strftime("%Y-%m-%d %H:%M:%S"))
  if "2020" in dataset['LastUpdatedTime'].strftime("%Y-%m-%d %H:%M:%S"):
   print(dataset['Name'],dataset['CreatedTime'].strftime("%Y-%m-%d %H:%M:%S"),dataset['LastUpdatedTime'].strftime("%Y-%m-%d %H:%M:%S"))



#Jtitle = 'Quicksight Dashboard Security information'
#J
#Jmailcmd = "mailx -a " + reportfile + " -s 'Dashboardinfo' jigar.b.shah@accenturefederal.com < /dev/null"
#J
#Jdashboardinfo = []
#Jfor i in response1['DashboardSummaryList']:
#J
#J  response2 = client.describe_dashboard_permissions(AwsAccountId=accountid,DashboardId=i['DashboardId'])
#J
#J  for j in response2['Permissions']:
#J
#J    permissions = list(str(j['Actions']).replace('quicksight:','').replace("'",'').replace("[",'').replace("]",'').replace(" ",'').split(","))
#J    permissions = ("-".join(permissions))
#J    username = re.search ('default/(.*)',j['Principal']).group(1)
#J    response3 = client.describe_user(AwsAccountId=accountid,Namespace='default',UserName=username)
#J    role = response3['User']['Role']
#J    dashboardname = i['Name']
#J    status = response3['User']['Active']
#J    email = response3['User']['Email']
#J    color="black"
#J    bcolor="cornsilk"
#J    if status is False:
#J      color="white"
#J      bcolor="red"
#J
#J
#J    jsondata  = {
#J    'DashboardName' : dashboardname,
#J    'UserName' : username,
#J    'Role' : role,
#J    'Status' : status,
#J    'Email' : email,
#J    'DashboardPermissions' : permissions,
#J    'color' : str(color),
#J    'bcolor' : str(bcolor)
#J    }
#J    dashboardinfo.append(jsondata)
#J
#J
#J
#Jdashboardinfo.sort(key=lambda x: (x['DashboardName'],x['UserName']))
#J
#J
#Jfile_loader = FileSystemLoader('./templates')
#Jenv = Environment(loader=file_loader)
#Jtemplate = env.get_template('dashboard_info_report.j2')
#Joutput = template.render(dashboardinfo = dashboardinfo)
#Jprint(output)
#JMail(output)
#J
#J#with open(reportfile,'w') as f:
#J#  f.write(output)
#J#os.system(mailcmd)
#J
#J#    dashboardinfo.append(dashboardname + ',' + username + ',' + role + ',' + str(status) +','+ email + ',' + permissions)
