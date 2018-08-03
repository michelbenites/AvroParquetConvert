#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/20/2018
# Descr. : Mapping URL - Avro format

import avro.schema
from avro.datafile import DataFileReader
from avro.io import DatumReader
from json import loads
import sys

# Loop in the reader.    
for logs in sys.stdin:

    # Loads the line with logs from json format.
    line = loads(logs) 

    # Get the URL from log avro format and print.
    sURL = line['url']
    print ("%s" % (sURL))




##import avro.schema
##from avro.datafile import DataFileReader
##from avro.io import DatumReader
##from json import loads
##import sys
##import platform


### Checks which platform is in use.
##if platform.system() == "Windows":
##    # Sets the output file.
##    out_file = open("map_url_out.txt", "w")
##
##    # Sets the reader from system argument.
##    reader = DataFileReader(open(sys.argv[1], 'rb'), DatumReader())
##else:
##    # In the EMR it gets from sys.stdin.
##    reader = sys.stdin
##
### Loop in the reader.    
##for logs in reader:
##
##    # Checks which platform is in use.
##    if platform.system() == "Windows":
##        line = logs
##    else:
##        # Loads the line with logs from json format.
##        line = loads(logs) 
##
##    # Get the URL from log avro format.
##    sURL = line['url']
##    print ("%s" % (sURL))
##
##    # Checks which platform is in use.
##    if platform.system() == "Windows":
##        out_file.write("%s\n" % (sURL))
##
### Close the reader.
##reader.close()
##
### Checks which platform is in use.
##if platform.system() == "Windows":
##    # Close output file.
##    out_file.close()

