import click

from modules.s3 import S3Analyzer
from modules.iam import IamAnalyzer
from modules.securitygroups import SgAnalyzer
from modules.elasticip import ElasticIpAnalyzer
from modules.volumes import VolumesAnalyzer
from modules.ami import AmiAnalyzer
from modules.banner import Banner

@click.command()
@click.option("--s3", is_flag=True, help="Search buckets public in s3")
@click.option("--iam", is_flag=True, help="Search iam users based on creation date")
@click.option('--sg', is_flag=True, help="Search security groups with inbound rule 0.0.0.0")
@click.option('--elasticip', is_flag=True, help="Search elastic IP not associated")
@click.option('--volumes', is_flag=True, help="Search volumes available")
@click.option('--ami', is_flag=True, help="Search AMIs with permission public")
@click.option('--owner', multiple=True, default='', help="Defines the owner of the resources to be found")

def main(s3, iam, sg, elasticip, volumes, ami, owner):

    if s3:
        s3 = S3Analyzer()
        s3.bucket_analyzer()

    elif iam:
        iam = IamAnalyzer()
        iam.find_max_access_key_age()

    elif sg:
        sg = SgAnalyzer()
        sg.find_security_groups()

    elif elasticip:
        ip = ElasticIpAnalyzer()
        ip.find_elastic_dissociated()

    elif volumes:
        vol = VolumesAnalyzer()
        vol.find_volumes_available()

    elif ami:
        owners = list()

        for own in owner:
            owners.append(own)

        ami = AmiAnalyzer(owners)
        ami.find_public_ami()

if __name__=='__main__':
    print(Banner.banner)
    main()
