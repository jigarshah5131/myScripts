#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,os

client = boto3.client('quicksight')
response = client.describe_user(AwsAccountId='150812941021',Namespace='default',UserName='Erika.McGowens1@cms.hhs.gov')
pp = pprint.PrettyPrinter(indent=4)

print (response['User']['Role'])

#Jtname  = "UserName"
#Jtemail = "Email"
#Jtrole  = "Role"
#Jtstatus = "Active"
#Jmailcmd = "mailx -a 'userlist.csv' -s 'qs users' jigar.b.shah@accenturefederal.com < /dev/null"
#J
#J#pp.pprint(response['UserList'])
#J#print (response['UserList'])
#Juserlist = []
#Jfor k in response['UserList']:
#J  #print(k['UserName'] +','+ k['Email'] + ',' + k['Role'] + ',' + str(k['Active']))
#J  userlist.append(k['UserName'] +','+ k['Email'] + ',' + k['Role'] + ',' + str(k['Active']))
#J#print(userlist)
#J
#Juserlist.sort(key=str.lower)
#J
#Jwith open('userlist.csv','w') as f:
#J
#J  f.write("%s,%s,%s,%s" %(tname,temail,trole,tstatus) + '\n')
#J  for row in userlist:
#J    f.write(row+'\n')
#Jos.system(mailcmd)
