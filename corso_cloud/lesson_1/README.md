# Twitter search client example

- connects to twitter APIs and searches for tweets using a query
- saves results in postgres database


## Build

To build an installable archive do:

    python setup.py sdist

You'll find the archive in `dist/twitter_example-X.Y.tar.gz`


## Publish / upload the archive

If you have dropbox synced with your home folder:

    python publish.py


Otherwise:

- Copy the archive into your dropbox folder
- share it with dropbox
- copy the shared url


## Install / Download

    pip install [archive-url-on-dropbox]


## Run on server

We prefer circus as a process manager, and we already have a circusd config file
available.

    circusd circus.ini


## Running the app on your machine

To search for tweets containing `ciao` do:

    python -m twitter_example ciao
