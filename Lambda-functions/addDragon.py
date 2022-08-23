

import boto3
import json

s3 = boto3.client('s3')
ssm = boto3.client('ssm', 'us-east-1')
bucket_name = ssm.get_parameter( Name='dragon_data_bucket_name',WithDecryption=False)['Parameter']['Value']
file_name = ssm.get_parameter( Name='dragon_data_file_name',WithDecryption=False)['Parameter']['Value']

def addDragonToFile(event, context):

    dragon_data = {
     "description_str":event['description_str'],
     "dragon_name_str":event['dragon_name_str'],
     "family_str":event['family_str'],
     "location_city_str":event['location_city_str'],
     "location_country_str":event['location_country_str'],
     "location_neighborhood_str":event['location_neighborhood_str'],
     "location_state_str":event['location_state_str']
    }
    
    resp=s3.get_object(Bucket=bucket_name, Key=file_name)
    data=resp.get('Body').read()
    
    json_data = json.loads(data)
    json_data.append(dragon_data)
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(json_data).encode())
