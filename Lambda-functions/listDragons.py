import boto3
import json

#setting the clients for s3 and systems manager to perform operations.
#pulling out the bucket name and dragons data file name from the parameter store.
s3 = boto3.client('s3','us-east-1')
ssm = boto3.client('ssm', 'us-east-1')
bucket_name = ssm.get_parameter( Name='dragon_data_bucket_name',WithDecryption=False)['Parameter']['Value']
file_name = ssm.get_parameter( Name='dragon_data_file_name',WithDecryption=False)['Parameter']['Value']

#function to access the s3 bucket contents to retrieve dragons details.
def listDragons(event, context):
    #defining expression to query using s3.select_object_content api.
    expression = "select * from s3object[*][*] s"
    
    #checking for query string parameters if present in request and filtering the data according to the conditions specified in query strings.
    if 'queryStringParameters' in event and event['queryStringParameters'] is not None:
        if 'dragonName' in event['queryStringParameters']:
            expression = "select * from S3Object[*][*] s where s.dragon_name_str =  '" + event["queryStringParameters"]['dragonName'] + "'"
        if 'family' in event['queryStringParameters']:
            expression = "select * from S3Object[*][*] s where s.family_str =  '" + event["queryStringParameters"]['family'] + "'"
  
#taking all the result data recieved by s3 select api in the form of JSON object and storing in result variable.
    result = s3.select_object_content(
            Bucket=bucket_name,
            Key=file_name,
            ExpressionType='SQL',
            Expression=expression,
            InputSerialization={'JSON': {'Type': 'Document'}},
            OutputSerialization={'JSON': {}}
    )
    
  #formatting the result so that it is readable by the user.
    result_stream = []
    for event in result['Payload']:
        if 'Records' in event:
            for line in event['Records']['Payload'].decode('utf-8').strip().split("\n"):
                result_stream.append(json.loads(line))
            
   #returning a statuscode of 200 if successful as a response      
    return {
        "statusCode": 200,
        "body": json.dumps(result_stream),
        "headers" : {"access-control-allow-origin": "*"}
    }

        
