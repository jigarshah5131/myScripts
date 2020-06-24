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
mailcmd = "mailx -a 'userlist.csv' -s 'qs users' jigar.b.shah@accenturefederal.com < /dev/null"

#pp.pprint(response['UserList'])
#print (response['UserList'])
userlist = []
for k in response['UserList']:
  #print(k['UserName'] +','+ k['Email'] + ',' + k['Role'] + ',' + str(k['Active']))
#  if "accenturefederal" in k['Email']:
    userlist.append(k['UserName'] +','+ k['Email'] + ',' + k['Role'] + ',' + str(k['Active']) + ',' + k['Arn'])
#print(userlist)

userlist.sort(key=str.lower)
"""
duplist = []
for line in sorted(userlist):
  d = line.split(',') 
#  duplist.append(d[1])
  duplist.append(d[0])
duplist.sort(key=str.lower)
for dup in duplist:
  print(dup)
#userlist.sort(key=lambda x: x)
"""
with open('userlist.csv','w') as f:

  f.write("%s,%s,%s,%s,%s" %(tname,temail,trole,tstatus,tarn) + '\n')
  for row in userlist:
    f.write(row+'\n')
#os.system(mailcmd)
