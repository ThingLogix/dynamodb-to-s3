# ThingLogix
### AWS Lambda function to copy all data in a DynamoDB table to a CSV file in S3

## Installation guide
Clone this repository, then either copy/paste the code into the inline Lambda text editor, or zip the contents of this folder, then upload the zip file to AWS Lambda as a Lambda function. This Lambda function should have runtime Python 3.6. The handler should be dynamodb_to_s3.lambda_handler.

### Usage instructions
To use this AWS Lambda function, see the example below. You must give the following parameters:
* table - name of DynamoDB table to get data from
* bucket - name of S3 bucket in which to place CSV
* key - key that CSV file will have when placed in S3

```
{
    "table": "fndy_object_type_dev",
    "bucket": "open-source-lambdas",
    "key": "object_types.csv"
}
```
