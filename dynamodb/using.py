import boto3

# Get the service resource.
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id='AKIAJQI3UJJWLUR7DL4A',
    aws_secret_access_key='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',
    region_name='us-west-2'
)
# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('test_table')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
#print(table.Node_ID)

print(dynamodb)
print(table)
