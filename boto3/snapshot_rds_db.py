#!/home/oracle/environments/my_env/bin/python
import boto3,pprint,argparse,sys,datetime,time

now=datetime.datetime.now()
pp = pprint.PrettyPrinter(indent=2)
instident=None
t=0
maxt=3600
sleepint=20


if len(sys.argv)== 1:
  print ("\n")
  print (" **** Use " + sys.argv[0] + " -h for filter options")
  print ("\n")
  exit()

parser = argparse.ArgumentParser()
parser.add_argument('-i','--instname',help='Provide the environment name. For Ex (imp1b-dz) ', required=True, default='')
parser.add_argument('-t','--tag',help='Append the tag at the end of snapshot name. For Ex <GC> Golden Copy', required=False, default='gc')
args=parser.parse_args()

client = boto3.client('rds')
response= client.describe_db_instances ()

for inst in response['DBInstances']:
 if args.instname in inst['DBInstanceIdentifier'] and 'ora' in  inst['DBInstanceIdentifier'] and inst['DBInstanceStatus'] == 'available':
    instident = inst['DBInstanceIdentifier']
    print (inst['DBInstanceIdentifier'],inst['DBName'],inst['Endpoint']['Address'],inst['Endpoint']['Port'],inst['DBInstanceStatus'])

if instident:
  snapshotName='Manual-'+instident+ '-' + now.strftime("%Y%m%d%H%M")+ '-' + args.tag
  print(snapshotName)
  response = client.create_db_snapshot(
    DBSnapshotIdentifier=snapshotName,
    DBInstanceIdentifier=instident
  )
#  pp.pprint(response)
else:
  print(args.instname + ' is not at the right state of taking snapshot. It might be backing-up. Exiting..')
  exit(1)

while t < maxt :

   response = client.describe_db_snapshots(SnapshotType='manual',DBSnapshotIdentifier=snapshotName)

   for inst in response['DBSnapshots']:
     print(inst['DBInstanceIdentifier'], inst['DBSnapshotIdentifier'],inst['SnapshotType'],inst['Status'])

   if inst['Status'] == 'available':
        print (inst['DBSnapshotIdentifier'] + ' Snapshot completed Successfully at '+ str(inst['SnapshotCreateTime']) + ' and '+ inst['Status']+'.')
        #break
        sys.exit()
   else:
        print ('Snapshot creation is in progres.. Status : '+ inst['Status'])
   print (str(t) + ':' + str(maxt) + ' seconds')
   time.sleep(sleepint)
   t = t + sleepint

print ('Maximum number of seconds waited. Snapshot is taking longer. Exiting..')

response = client.describe_db_snapshots(SnapshotType='manual',DBSnapshotIdentifier=snapshotName)

for inst in response['DBSnapshots']:
  print(inst['DBInstanceIdentifier'], inst['DBSnapshotIdentifier'],inst['SnapshotType'],inst['Status'])
