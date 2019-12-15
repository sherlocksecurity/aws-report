import click

from modules.s3 import S3Analyzer
from modules.iam import IamAnalyzer
from modules.securitygroups import SgAnalyzer
from modules.banner import Banner

@click.command()
@click.option("--s3", is_flag=True, help="Search buckets public in s3")
@click.option("--iam", is_flag=True, help="analyze iam users based on creation date")
@click.option('--sg', is_flag=True, help="Search security groups with inbound rule 0.0.0.0")

def main(s3, iam, sg):

    if s3:
        s3 = S3Analyzer()
        s3.bucket_analyzer()

    elif iam:
        iam = IamAnalyzer()
        iam.find_max_access_key_age()

    elif sg:
        sg = SgAnalyzer()
        sg.find_security_groups()

if __name__=='__main__':
    print(Banner.banner)
    main()
