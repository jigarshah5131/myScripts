#!/usr/bin/env python
 
import boto3
 
profile='aws-hhs-cms-mitg-fm-prod'
 
session=boto3.Session(profile_name=str(profile))
s3=session.resource('s3')
bucket=s3.Bucket('fcs-ml-shared-pr0-dz-emr-fm-raw')
 
for object in bucket.objects.all():
  print('s3://'+object.bucket_name+'/'+object.key)
  acl=s3.ObjectAcl(object.bucket_name,object.key)
  acl.put(ACL="bucket-owner-full-control") 
