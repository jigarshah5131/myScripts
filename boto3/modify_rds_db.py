#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,time,json

pp = pprint.PrettyPrinter(indent=2)
client = boto3.client('rds')
t=0
maxt=1600
sleepint=60

if len(sys.argv)== 1:
  print ("\n")
  print (" **** Use " + sys.argv[0] + " -h for filter options")
  print ("\n")
  sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('-i','--instname',help='Instance Name to rename to', required=True, default='')
parser.add_argument('-r','--newinstname',help='New Instance name ', required=True ,default='')
parser.add_argument('-a','--apply',help='Apply immediately <True|False>', required=True)
#J
args=parser.parse_args()

## Check if Instance exists..


try:
  response = client.describe_db_instances(DBInstanceIdentifier = args.instname)

  for inst in response['DBInstances']:
   if inst['DBInstanceIdentifier']:
     print (args.instname + ' Exists.. Moving forward with renaming the instance.')
     response = client.modify_db_instance(DBInstanceIdentifier = args.instname, NewDBInstanceIdentifier = args.newinstname, ApplyImmediately = bool(args.apply))
     pp.pprint(response)
#   else:
#    print (args.instname + ' Does not exist..')
#    sys.exit(1)
except Exception as error:
  print(error)
  sys.exit(1)
print('sleeping.. ' + str(sleepint) + ' seconds')
time.sleep(sleepint)
while t < maxt:
   #response = client.describe_db_instances(DBInstanceIdentifier = args.newinstname)
   response = client.describe_db_instances()
   for inst in response['DBInstances']:
     if inst['DBInstanceIdentifier'] == args.newinstname and inst['DBInstanceStatus'] == 'available':
        print('Instance Renamed to :' + inst['DBInstanceIdentifier'] + ' Status : '+  inst['DBInstanceStatus'])
        sys.exit(1)
     else:
       if inst['DBInstanceIdentifier'] == args.instname or inst['DBInstanceIdentifier'] == args.newinstname:
        print('Instance ' + inst['DBInstanceIdentifier'] + ' Status : '+  inst['DBInstanceStatus'])
        print('Renaming may be in progress. Be patient or ctrl-c' )
        print (str(t) + ':' + str(maxt) + ' seconds')
        time.sleep(sleepint)
        t = t + sleepint
print('Loop max reached. Exiting..')

