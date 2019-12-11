import boto3

from collections import defaultdict
from colors import bcolors

class S3Analyzer():
    def __init__(self):
        self.s3_resource = boto3.resource('s3')
        self.s3_client = boto3.client('s3')

        self.groups = {
            "http://acs.amazonaws.com/groups/global/AllUsers": "Everyone",
            "http://acs.amazonaws.com/groups/global/AuthenticatedUsers": "Authenticated AWS users"
        }

    def bucket_analyzer(self):
        buckets = self.s3_resource.buckets.all()

        for bucket in buckets:
            acl = bucket.Acl()
            public, grants = self.verify_acl(acl)

            if public:
                print("{0}[WARNING]{1}: Bucket {2} is public!".format(bcolors.FAIL, bcolors.ENDC, bucket.name))

    def verify_acl(self, acl):
        dangerous = defaultdict(list)

        for grant in acl.grants:
            grantee = grant["Grantee"]
            if grantee["Type"] == "Group" and grantee["URI"] in self.groups:
                dangerous[grantee["URI"]].append(grant["Permission"])
        
        if dangerous:
            public = True
        else: 
            public = False

        return public, dangerous
