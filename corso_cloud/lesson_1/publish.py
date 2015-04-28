'''
Copies the archive into a shared dropbox folder
'''
import shutil
import glob
import os.path


for fname in glob.glob('dist/twitter_example-*.tar.gz'):
    shutil.copy(fname, os.path.expanduser('~/Dropbox/'))
    print('copying {} into Dropbox'.format(fname))
