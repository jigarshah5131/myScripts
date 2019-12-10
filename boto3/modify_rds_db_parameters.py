#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,time,json,os,datetime,time,re
from subprocess import Popen,PIPE

now=datetime.datetime.now()
pp = pprint.PrettyPrinter(indent=2)
client = boto3.client('rds')
t=0
maxt=3600
sleepint=60

if len(sys.argv)== 1:
  print ("\n")
  print (" **** Use " + sys.argv[0] + " -h for filter options")
  print ("\n")
  sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('-i','--instname',help='Instance Name to modify to', required=True, default='')
parser.add_argument('-r','--rename',help='New Instance name ', required=False ,default='')
parser.add_argument('-a','--apply',help='Apply immediately <true|false>', required=True)
parser.add_argument('-c','--dbconnect',help='Connect string to database <fmimpl1b|fmimpl1a>', required=False)
#J
args=parser.parse_args()

#sys.stdout = open('file', 'w')

def runSqlQuery(sqlCommand, connectString):
    session = Popen(['sqlplus', '-S',connectString],stdin=PIPE, stdout=PIPE,stderr=PIPE)
    session.stdin.write(sqlCommand)
    return session.communicate()

#Jtry:
#J  connectString = 'dbadmin/FMcms123$@'+ args.dbconnect
#J  sqlCommand = b'@/home/oracle/impl1b/gen_update_pass.sql'
#J  queryResult,errorMessage = runSqlQuery(sqlCommand,connectString)
#J  print(queryResult)
#J  print(errorMessage)
#Jexcept Exception as error:
#J  print(error)
#J  sys.exit(1)


modstr = []

if args.instname:
  modstr.append("DBInstanceIdentifier    = instance[args.instname]['DBInstanceIdentifier']")
  modstr.append("MultiAZ                 = instance[args.instname]['MultiAZ']")
  modstr.append("PubliclyAccessible      = instance[args.instname]['PubliclyAccessible']")
  modstr.append("AutoMinorVersionUpgrade = instance[args.instname]['AutoMinorVersionUpgrade']")
  modstr.append("OptionGroupName         = instance[args.instname]['OptionGroupName']")
  modstr.append("StorageType             = instance[args.instname]['StorageType']")
  modstr.append("DeletionProtection      = instance[args.instname]['DeletionProtection']")
  modstr.append("DBParameterGroupName    = instance[args.instname]['DBParameterGroupName']")
  modstr.append("DBInstanceClass         = instance[args.instname]['DBInstanceClass']")
  modstr.append("AllocatedStorage        = instance[args.instname]['AllocatedStorage']")
  modstr.append("VpcSecurityGroupIds     = instance[args.instname]['VpcSecurityGroupIds']")
  modstr.append("EngineVersion           = instance[args.instname]['EngineVersion']")
  modstr.append("ApplyImmediately        = bool(args.apply)")

#print(',\n'.join(modstr))
## Check if Instance exists..
with open ('instances.json') as f:
  data = json.load(f)
for instance in data['instances']:
  newinstname = instance[args.instname]['DBInstanceIdentifier'] + '-' + now.strftime("%Y%m%d%H%M") + '-remove'
  if instance[args.instname]['StorageType'] == 'io1':
     modstr.append("Iops                    = instance[args.instname]['Iops']")
  if args.rename == 'rename' and instance[args.instname]['DBInstanceIdentifier'] != newinstname:
     modstr.append("NewDBInstanceIdentifier = newinstname")
  finalstr='response = client.modify_db_instance(\n  ' + ',\n  '.join(modstr) + '\n  )'
  print(finalstr)
  print(newinstname)
  response = client.describe_db_instances()
  for inst in response['DBInstances']:
    if inst['DBInstanceIdentifier'] == instance[args.instname]['DBInstanceIdentifier'] and inst['DBInstanceStatus'] != 'available' :
      print(instance[args.instname]['DBInstanceIdentifier'] + " is not in right status ")
      sys.exit(1)

print(instance[args.instname]['DBInstanceIdentifier'])
try:
 #print(',\n'.join(modstr))
  print(finalstr)
  exec(finalstr)
except Exception as error:
  print(error)
  sys.exit(1)

print('sleeping.. ' + str(sleepint) + ' seconds')
time.sleep(sleepint)

while t < maxt:
  response = client.describe_db_instances()
  for inst in response['DBInstances']:
     if inst['DBInstanceIdentifier'] == instance[args.instname]['DBInstanceIdentifier'] :
        identifier = instance[args.instname]['DBInstanceIdentifier']
     elif inst['DBInstanceIdentifier'] == newinstname:
        identifier = newinstname
  print("identifier is " + str(identifier))
  response = client.describe_db_instances(DBInstanceIdentifier =   identifier)
  for inst in response['DBInstances']:
      print("Going to for loop")
      if inst['DBInstanceIdentifier'] == identifier and inst['DBInstanceStatus'] == 'available':
        print('Instance modification completed :' + identifier + ' Status : '+  inst['DBInstanceStatus'])
        sys.exit(1)
      else:
        if inst['DBInstanceIdentifier'] == identifier:
          print('Instance ' + identifier + ' Status : '+  inst['DBInstanceStatus'])
          print('Renaming may be in progress. Be patient or ctrl-c' )
          print (str(t) + ':' + str(maxt) + ' seconds')
  time.sleep(sleepint)
  t = t + sleepint
print('Loop max reached. Exiting..')

#Temp(my_env) [oracle@e1afmproddora01 boto3]$ cat modify_rds_db_parameters.py
#Temp#!/home/oracle/environments/my_env/bin/python
#Tempimport boto3,pprint,argparse,sys,time,json
#Temp
#Temppp = pprint.PrettyPrinter(indent=2)
#Tempclient = boto3.client('rds')
#Tempt=0
#Tempmaxt=1600
#Tempsleepint=60
#Temp
#Tempif len(sys.argv)== 1:
#Temp  print ("\n")
#Temp  print (" **** Use " + sys.argv[0] + " -h for filter options")
#Temp  print ("\n")
#Temp  sys.exit(1)
#Temp
#Tempparser = argparse.ArgumentParser()
#Tempparser.add_argument('-i','--instname',help='Instance Name to rename to', required=True, default='')
#Temp#parser.add_argument('-r','--newinstname',help='New Instance name ', required=True ,default='')
#Tempparser.add_argument('-a','--apply',help='Apply immediately <True|False>', required=True)
#Temp#J
#Tempargs=parser.parse_args()
#Temp
#Temp## Check if Instance exists..
#Tempwith open ('instances.json') as f:
#Temp  data = json.load(f)
#Temp
#Temptry:
#Temp for instance in data['instances']:
#Temp
#Temp  response = client.modify_db_instance(
#Temp    DBInstanceIdentifier    = instance[args.instname]['DBInstanceIdentifier'],
#Temp    NewDBInstanceIdentifier = instance[args.instname]['NewDBInstanceIdentifier'],
#Temp#    DBSubnetGroupName       = instance[args.instname]['DBSubnetGroupName'],
#Temp    MultiAZ                 = instance[args.instname]['MultiAZ'],
#Temp    PubliclyAccessible      = instance[args.instname]['PubliclyAccessible'],
#Temp    AutoMinorVersionUpgrade = instance[args.instname]['AutoMinorVersionUpgrade'],
#Temp    OptionGroupName         = instance[args.instname]['OptionGroupName'],
#Temp    StorageType             = instance[args.instname]['StorageType'],
#Temp    Iops                    = instance[args.instname]['Iops'],
#Temp    AllocatedStorage        = instance[args.instname]['AllocatedStorage'],
#Temp    DBParameterGroupName    = instance[args.instname]['DBParameterGroupName'],
#Temp    DeletionProtection      = instance[args.instname]['DeletionProtection'],
#Temp    DBInstanceClass         = instance[args.instname]['DBInstanceClass'],
#Temp    VpcSecurityGroupIds     = instance[args.instname]['VpcSecurityGroupIds'],
#Temp    ApplyImmediately        = bool(args.apply)
#Temp
#Temp    )
#Temp  pp.pprint(response)
#Temp
#Tempexcept Exception as error:
#Temp  print(error)
#Temp  sys.exit(1)
#Temp
#Tempprint('sleeping.. ' + str(sleepint) + ' seconds')
#Temptime.sleep(sleepint)
#Temp
#Tempwhile t < maxt:
#Temp   response = client.describe_db_instances(DBInstanceIdentifier = instance[args.instname]['NewDBInstanceIdentifier'])
#Temp   for inst in response['DBInstances']:
#Temp     if inst['DBInstanceIdentifier'] == instance[args.instname]['NewDBInstanceIdentifier'] and inst['DBInstanceStatus'] == 'available':
#Temp        print('Instance modification completed :' + inst['DBInstanceIdentifier'] + ' Status : '+  inst['DBInstanceStatus'])
#Temp        sys.exit(1)
#Temp     else:
#Temp       if inst['DBInstanceIdentifier'] == instance[args.instname]['DBInstanceIdentifier'] or  NewDBInstanceIdentifier == instance[args.instname]['NewDBInstanceIdentifier']:
#Temp        print('Instance ' + inst['DBInstanceIdentifier'] + ' Status : '+  inst['DBInstanceStatus'])
#Temp        print('Renaming may be in progress. Be patient or ctrl-c' )
#Temp        print (str(t) + ':' + str(maxt) + ' seconds')
#Temp        time.sleep(sleepint)
#Temp        t = t + sleepint
#Tempprint('Loop max reached. Exiting..')

