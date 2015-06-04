# Final exam

Write a python program that preiodically reports cpu information
and logs it to logentries.

You can use the `os.getloadavg()` function

The program has a simple build/publish
procedure and includes all the
needed documentation for the sysadmin
to run it on the server.


## Build the package

    python setup.py sdist


## Publish the archive on s3

    python publish.py


## Deploy it on the server

    pip install <s3-archive-url>

## Run it on the server

    python -m cpuinfo.main <logentries token>
