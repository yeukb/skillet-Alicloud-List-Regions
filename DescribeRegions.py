#!/usr/bin/env python

import json
import argparse
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--alicloud_access_key', help='Alicloud Key', required=True)
parser.add_argument('-s', '--alicloud_secret_key', help='Alicloud Secret', required=True)
args = parser.parse_args()

access_key = args.alicloud_access_key
secret_key = args.alicloud_secret_key

client = AcsClient(access_key, secret_key, 'ap-southeast-1')

request = DescribeRegionsRequest()
request.set_accept_format('json')

response = client.do_action_with_exception(request)

parsed = json.loads(str(response, encoding='utf-8'))

data = parsed['Regions']['Region']

for x in range(len(data)):
  print(str(x+1) + ' :' + '\t' + data[x]["RegionId"])
