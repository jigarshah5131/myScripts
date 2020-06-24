#!/usr/bin/env python
import sys,os
import boto3,pprint,argparse,os,re
boto3path = os.path.expanduser('~/boto3')
#boto3path='~/boto3'
sys.path.append(boto3path)
#sys.path.append(pythonpath)
#from jinja2 import Environment,FileSystemLoader
from modules.common import email as Mail
print(sys.path)
