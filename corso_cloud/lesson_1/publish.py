'''
Copies the archive into a shared dropbox folder
'''
import glob
import botocore.session


def publish():
    bucket = 'tsac_marco_test'
    session = botocore.session.Session(
        session_vars={'profile': (None, None, 'tsac-test')}
    )
    s3 = session.create_client('s3')
    s3.create_bucket(Bucket=bucket)

    # get archives
    for fname in glob.glob('dist/twitter_example-*.tar.gz'):
        with open(fname, 'rb') as f:
            s3.put_object(
                Bucket=bucket,
                Key='archive.tar.gz',
                Body=f,
                ACL='public-read'
            )
        print('archive available at https://s3.amazonaws.com/{}/archive.tar.gz'.format(bucket))

if __name__ == '__main__':
    publish()
