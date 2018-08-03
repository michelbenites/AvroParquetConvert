#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/21/2018
# Descr. : Mapping user and url

import sys
import avro.schema
from json import loads
import sys

# Loop in the log file    
for logs in sys.stdin:

    # Loads the line with logs from json format.
    line = loads(logs) 

    # Get the URL, User and print.
    sURL  = line['url']
    sUser = line['user']
    print ("%s\t%s\t%d" % (sURL, sUser, 1))
