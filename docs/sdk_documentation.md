# AWS SDK Documentation References

## Boto3 Documentation Links

### S3 Service

1. **Boto3 S3 Client Documentation**

   - [S3 Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
   - Used in our scripts for interacting with S3 buckets and objects

2. **S3 Bucket Operations**

   - [list_buckets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_buckets)
   - [head_bucket](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.head_bucket)
   - Used to list all buckets and check bucket existence

3. **S3 Object Operations**
   - [list_objects_v2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects_v2)
   - [get_paginator](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_paginator)
   - Used to list and count objects in a bucket

### Lambda Service

1. **Boto3 Lambda Client Documentation**
   - [Lambda Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html)
   - Used for AWS Lambda function deployment in Terraform

### EC2 Service

1. **Boto3 EC2 Client Documentation**
   - [EC2 Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html)
   - Used for EC2 instance management in Terraform

## Python Standard Library Documentation

1. **CSV Module**

   - [csv](https://docs.python.org/3/library/csv.html)
   - Used in our CSV analyzer script

2. **Argparse Module**

   - [argparse](https://docs.python.org/3/library/argparse.html)
   - Used for command-line argument parsing in our scripts

3. **Path from Pathlib**
   - [pathlib.Path](https://docs.python.org/3/library/pathlib.html)
   - Used for file path operations in our scripts
