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
   try:
    permissions = list(str(j['Actions']).replace('quicksight:','').replace("'",'').replace("[",'').replace("]",'').replace(" ",'').split(","))
    permissions = ("-".join(permissions))
    username = re.search ('default/(.*)',j['Principal']).group(1)
    print("Generating for " + username)
    response3 = client.describe_user(AwsAccountId=accountid,Namespace='default',UserName=username)
    role = response3['User']['Role']
    dashboardname = i['Name']
    status = response3['User']['Active']
    status = str(status).replace('True','Active').replace('False','Inactive')
    email = response3['User']['Email']
    color="black"
    bcolor="cornsilk"
    if status in 'Inactive':
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
   except Exception as e:
    print(e)



dashboardinfo.sort(key=lambda x: (x['DashboardName'],x['UserName']))

template_path = os.path.dirname(os.path.realpath(sys.argv[0]))+'/templates/'
file_loader = FileSystemLoader(template_path)
#file_loader = FileSystemLoader('templates/')
env = Environment(loader=file_loader)
template = env.get_template('dashboard_info_report.j2')
output = template.render(dashboardinfo = dashboardinfo,title = 'Quicksight Dashboard Security information')
print('Sending email')
Mail(output)
with open('listqsdashboards.html','w') as f:
  f.write(output)
#print("Sending email to " + mailcmd)

#with open(reportfile,'w') as f:
#  f.write(output)
#os.system(mailcmd)

#    dashboardinfo.append(dashboardname + ',' + username + ',' + role + ',' + str(status) +','+ email + ',' + permissions)
