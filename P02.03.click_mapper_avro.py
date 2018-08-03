#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/21/2018
# Descr. : Mapping user Clicks by URL Avro Format.

import sys
import avro.schema
from json import loads
import sys 
    
# Loop in the log file    
for logs in sys.stdin:

    # Loads the line with logs from json format.
    line = loads(logs) 

    # Get the URL, User, Timestamp and print.
    sURL   = line['url']
    sUser  = line['user']
    sClick = line['timestamp']
    print ("%s\t%s\t%s" % (sURL, sUser, sClick))

