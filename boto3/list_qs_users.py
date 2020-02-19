#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os

client = boto3.client('quicksight')
response = client.list_users(AwsAccountId='150812941021',Namespace='default')
pp = pprint.PrettyPrinter(indent=4)

tname  = "UserName"
temail = "Email"
trole  = "Role"
tstatus = "Active"
mailcmd = "mailx -a 'userlist.csv' -s 'qs users' jigar.b.shah@accenturefederal.com < /dev/null"

#pp.pprint(response['UserList'])
#print (response['UserList'])
userlist = []
for k in response['UserList']:
  #print(k['UserName'] +','+ k['Email'] + ',' + k['Role'] + ',' + str(k['Active']))
  userlist.append(k['UserName'] +','+ k['Email'] + ',' + k['Role'] + ',' + str(k['Active']))
#print(userlist)

userlist.sort(key=str.lower)

with open('userlist.csv','w') as f:

  f.write("%s,%s,%s,%s" %(tname,temail,trole,tstatus) + '\n')
  for row in userlist:
    f.write(row+'\n')
os.system(mailcmd)
