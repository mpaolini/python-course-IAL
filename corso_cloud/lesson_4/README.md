# Run the twitter example client on an AWS machine

- create a virtualenv

    virtualenv -p python3 virtual

- activate virtualenv

    source virtual/bin/activate

- install circus
- upload circus config file `circus.ini`
- set env vars:

    export APP_KEY=XXXX
    export APP_SECRET=YYY
    export LOGENTRIES_KEY=ZZZZ

- pip install `app_url.tar.gz`
- start circusd

    circusd circus.ini
