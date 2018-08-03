#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/24/2018
# Descr. : Converting normal logs to avro format

import sys
import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter
import uuid

# Main function
def main ():

    # Define schema of avro file.
    schema = avro.schema.Parse(open("logs_uuid.avsc", "rb").read())

    # Create a datum writer.
    rwriter = DatumWriter(schema)

    files = ['logs_0.txt', 'logs_1.txt', 'logs_2.txt', 'logs_3.txt']
    
    # Loop to process the files 
    for f in files:

        # open file and store in a variable
        logfile = open(f, "r")
        text    = logfile.readlines()
        logfile.close()

        # Set the avro file name (new)
        newfile = str(f).replace('.txt','uuid.avro')

        # Create a data file writer.
        dfwriter = DataFileWriter (open(newfile, "wb"), DatumWriter(), schema)

        # Loop to get information from each line
        for line in text:

            # Get the variables from line.
            sdt, surl, suser = line.strip().split('\t')

            # Defines a dictionary structure
            data = {}
            data['timestamp'] = sdt
            data['url']       = surl
            data['user']      = suser
            data['uuid']      = str(uuid.uuid1())

            # Write the data in the file.
            dfwriter.append (data)

        # Close the file after the loop.
        dfwriter.close()


# Calling main function
if __name__ == '__main__':    
    sys.exit(main())
