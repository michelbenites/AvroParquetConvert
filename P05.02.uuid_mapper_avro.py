#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/24/2018
# Descr. : Mapping user Clicks by URL Avro Format and UUID.

import sys
import avro.schema
from avro.datafile import DataFileReader
from avro.io import DatumReader
from json import loads
import sys
import platform

# Checks which platform is in use.
if platform.system() == "Windows":
    # Sets the reader from system argument.
    reader = DataFileReader(open(sys.argv[1], 'rb'), DatumReader())
else:
    # In the EMR it gets from sys.stdin.
    reader = sys.stdin

# Loop in the reader.    
for logs in reader:

    # Loads the line with logs from json format.
    line = loads(logs)
    #line = logs

    # Get the URL, User, Timestamp, UUID and print.
    sURL   = line['url']
    sUser  = line['user']
    sClick = line['timestamp']
    sUUID  = line['uuid']
    print ("%s\t%s\t%s\t%s" % (sURL, sUser, sUUID, sClick))

