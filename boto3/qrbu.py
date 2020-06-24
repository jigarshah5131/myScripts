#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os,re,json
from jinja2 import Environment,FileSystemLoader
boto3path = os.path.expanduser('~/boto3')
sys.path.append(boto3path)
import pandas as pd
from modules.common import email as Mail
#from modules.common import excel_email as Mail

title = 'Dashboard Report by users'

with open('dashmetadatafinalfull','r') as f:
  data = json.load(f)
dataframes=[]

for key in data.keys():
  dataframes.append(pd.DataFrame(data[key]))
df = pd.concat(dataframes)
df.drop(columns = ['DashboardID','Permissions','Role','Status'],inplace=True)
dn_group =  df.groupby(['Username','Email'],as_index=False).agg(lambda x:("/".join(sorted(set(x)))))
dn_group.set_index(['Username','Email'],inplace=True)
final_result = dn_group.reset_index()

#print(final_result)
userinfo = []
for row in final_result.itertuples():
  jsondata = {
     'UserName' : row.Username,
     'Email' : row.Email,
     'DashboardName' : row.DashboardName
  }
  userinfo.append(jsondata)
#  print(row.Username,row.Email,row.DashboardName) 
#print(userinfo)

env = Environment (loader = FileSystemLoader( searchpath ='templates/'))
template = env.get_template('userinfo.j2')
output = template.render(userinfo = userinfo,title = 'Dashboard REporting by Users')


#template_path = os.path.dirname(os.path.realpath(sys.argv[0]))+'/templates/'
#file_loader = FileSystemLoader(template_path)
#env = Environment(loader=file_loader)
#template = env.get_template('userinfo.j2')
#output = template.render(title = 'Dashboard REport by Users')
print(output)
Mail(output)
with open('outinfo.html','w') as f:
  f.write(output)
