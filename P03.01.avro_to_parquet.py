#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/21/2018
# Descr. : Converting avro files to parquet and upload to S3

import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
from avro import schema, datafile, io
import sys
import boto3
from botocore.client import Config

# Define keys to access S3 aws.
ACCESS_KEY_ID = 'WWWWWWWWWWWWWWWW'
ACCESS_SECRET_KEY = 'ZZZZZZZZZZZZZZZZZ'
BUCKET_NAME = 'harvardassignment0'


# Main function
def main ():

    # Create a datum writer.
    rec_reader = io.DatumReader()

    # Define files to convert into parquet files
    files = ['logs_0.avro', 'logs_1.avro', 'logs_2.avro', 'logs_3.avro']
    pqfiles = []
    #files = ['logs_small.avro']

    # Loop to process the files 
    for f in files:

        # Print message
        print ("Converting", f, "to parquet format..")

        # Define reader to avro format.
        df_reader = datafile.DataFileReader(open(f, "rb"), rec_reader)

        # Convert the records from avro into pandas dataframe.
        df = pd.DataFrame.from_records(df_reader)

        # Convert pandas dataframe into parquet table
        table = pa.Table.from_pandas(df)

        # Set the avro file name (new) and append on the list.
        newfile = str(f).replace('.avro', '.parquet')
        pqfiles.append(newfile)

        # Write the data into a parquet file format.
        pq.write_table(table, newfile)

        # Close the dataframe reader
        df_reader.close()


    # S3 setup
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_SECRET_KEY,
            config=Config(signature_version='s3v4')
        )

    # Loop to save the files on S3.
    for f in pqfiles:

        # File to upload on S3
        upfile = open(f, 'rb')

        # Upload the file on S3.
        print ("Uploading", f, "on S3 AWS..")
        s3.Bucket(BUCKET_NAME).put_object(Key=f, Body=upfile)

        # Close the file.
        upfile.close()
    

# Calling main function
if __name__ == '__main__':    
    sys.exit(main())



