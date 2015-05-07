import botocore.session


def get_dns_name(instance_id):
    session = botocore.session.Session(
        session_vars={'profile': (None, None, 'tsac-test')}
    )
    ec2 = session.create_client('ec2', region_name='eu-west-1')
    instances_desc = ec2.describe_instances(InstanceIds=[instance_id])
    return instances_desc['Reservations'][0]['Instances'][0]['PublicDnsName']


if __name__ == '__main__':
    import sys
    print(get_dns_name(sys.argv[1]))
