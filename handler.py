import json
import boto3

# Get the service resource
s3 = boto3.client('s3')

def size_compute(event, context):

    directory_size = 0
    #Get bucket from client
    bucket = s3.list_objects_v2(Bucket='test-bucket-lambda321',Delimiter='/',Prefix='images/')
    content = bucket['Contents']
    for key in content:
        print(key)
        file_name = key['Key']
        size = key['Size']
        directory_size += size

    # print(bucket)
    size = float(directory_size)
    size = round(size/(1024*1024), 2)
    print("The size of " + file_name + " is " + size + " MB")


    return
