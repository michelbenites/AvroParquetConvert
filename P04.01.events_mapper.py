#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/23/2018
# Descr. : Mapping url and day using the parameters filter.

import sys
import pyarrow.parquet as pq
from datetime import datetime

def mapper():

    # Verify if the numbers of arguments are Ok.
    if len(sys.argv) < 3:
        print('Invalid number of arguments!!!!')
        return
                    
    # Getting the arguments value.
    purl = sys.argv[1]
    pday = sys.argv[2]

    # Open the file to generate the mapper file.
    #foutput = open('map_out.txt', 'w')

    # Define files
    files = ['logs_0.parquet', 'logs_1.parquet', 'logs_2.parquet', 'logs_3.parquet']
    #files = sys.stdin

    for f in files:

        # Read parquet file and store in a dict.
        rtable  = pq.read_table(f)
        diclog  = rtable.to_pydict()

        # Get the size of list.
        size = len(diclog['url'])

        # Loop to get the data from listlog.
        for i in range(size-1):

            # Get the variables.
            stimest = diclog['timestamp'][i]
            surl    = diclog['url'][i]
            suser   = diclog['user'][i]

            # Get the day from the timestamp varuiable.
            sday    = stimest[:10]

            # Verify if the record is in the user filter.
            if surl == purl and sday == pday:

                # Get the hour from timestamp varuiable.
                stimest = stimest[:19]
                dtimest = datetime.strptime(stimest, '%Y-%m-%dT%H:%M:%S')
                stimest = datetime.strftime(dtimest, '%Y-%m-%d %Hh') 

                # print to reducer.
                print ('%s\t%s\t%d' % (surl, stimest, 1))
     #           foutput.write('%s\t%s\t%d\n' % (surl, stimest, 1))       

    #foutput.close()

# Calling main function
if __name__ == '__main__':    
    sys.exit(mapper())

    
