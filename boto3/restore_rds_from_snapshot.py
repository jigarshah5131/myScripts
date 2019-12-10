#!/home/oracle/environments/my_env/bin/python

import boto3,pprint,argparse,sys,json,time

pp = pprint.PrettyPrinter(indent=2)
t=0
maxt=3600
client = boto3.client('rds')
sleepint =  60


if len(sys.argv)== 1:
  print ("\n")
  print (" **** Use " + sys.argv[0] + " -h for filter options")
  print ("\n")
  exit()

parser = argparse.ArgumentParser()
parser.add_argument('-i','--instname',help='Short name of the instance, Ex (imp1a)', required=True, default='')
parser.add_argument('-s','--snapname',help='Short name of the instance, Ex (imp1a)', required=True, default='')

args=parser.parse_args()

with open ('instances.json') as f:
  data = json.load(f)

for instance in data['instances']:

  response = client.restore_db_instance_from_db_snapshot(
    DBInstanceIdentifier    = instance[args.instname]['InstanceIdentifier'],
    DBSnapshotIdentifier    = args.snapname,
    DBSubnetGroupName       = instance[args.instname]['SubnetGroupName'],
    MultiAZ                 = instance[args.instname]['MultiAZ'],
    PubliclyAccessible      = instance[args.instname]['PubliclyAccessed'],
    AutoMinorVersionUpgrade = instance[args.instname]['AutoMinorUpgrade'],
    DBName                  = instance[args.instname]['DbName'],
    OptionGroupName         = instance[args.instname]['OptionGroup'],
    StorageType             = instance[args.instname]['StorageType'],
    Iops                    = instance[args.instname]['Iops'],
    DBParameterGroupName    = instance[args.instname]['ParameterGroup'],
    DeletionProtection      = instance[args.instname]['DeleteProtection'],
    DBInstanceClass         = instance[args.instname]['InstanceSize'],
    VpcSecurityGroupIds     = instance[args.instname]['VpcSecurityGroups']
)
pp.pprint(response)


while t < maxt :
   response = client.describe_db_instances(DBInstanceIdentifier = instance[args.instname]['InstanceIdentifier'])

   for inst in response['DBInstances']:
    print (inst['DBInstanceIdentifier'],inst['DBName'],inst['DBInstanceStatus'])
   if inst['DBInstanceStatus'] == 'available':
    print (inst['DBInstanceIdentifier'],inst['DBName'],inst['Endpoint']['Address'],inst['Endpoint']['Port'],inst['DBInstanceStatus'])
    print (inst['DBInstanceIdentifier'] + ' restored Successfully ' + ' and '+ inst['DBInstanceStatus']+'.')
    sys.exit()
   else:
    print(inst['DBInstanceIdentifier'] + ' restore is in progress.. Status : ' + inst['DBInstanceStatus'] +'.')
    print (str(t) + ':' + str(maxt) + ' seconds')
    time.sleep(sleepint)
    t = t + sleepint

print ('Maximum number of seconds waited. Snapshot is taking longer. Exiting..')

response = client.describe_db_instances(DBInstanceIdentifier = instance[args.instname]['InstanceIdentifier'])

for inst in response['DBInstances']:
    print (inst['DBInstanceIdentifier'],inst['DBName'],inst['DBInstanceStatus'])
