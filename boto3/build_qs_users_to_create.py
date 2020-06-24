#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os

client = boto3.client('quicksight')
response = client.list_users(AwsAccountId='150812941021',Namespace='default')
pp = pprint.PrettyPrinter(indent=4)

tname  = "UserName"
temail = "Email"
trole  = "Role"
tstatus = "Active"
tarn = "Arn"

userlist = []
for k in response['UserList']:
  #print(k['UserName'] +','+ k['Email'] + ',' + k['Role'] + ',' + str(k['Active']))
#  if "accenturefederal" in k['Email']:
    userlist.append(k['UserName'] +':'+ k['Email'] + ':' + k['Role'] )
#print(userlist)

userlist.sort(key=str.lower)
with open('create_qs_users.txt','w') as f:
 for i in userlist:
   f.write(i + "\n")
