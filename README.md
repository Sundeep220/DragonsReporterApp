# DragonsApp

**General Notes**

An `Dragons Reporter` app made using Vue.js has been provided in this repo.This app shows the details of dragons spotted around the world and and let's the users to 
also report about the new dragons if spotted.


- I'm now building this application on AWS cloud. Currently this app doesn't works as there is storage service connected to it and no backend services 
to store and retrieve the dragons info. 

**For now building this app , I'm going to:
1. Create an s3 bucket to host the application and store the dragons data in a file.
2. Create an api gateway using REST api to create an endpoints for users to make request to list the dragons details and to report the new dragons if spotted.
3. Create an authentication service to authenticate users to allow them through my api gateway to access the app. For this I'm going to use Amazon Cognnito.
4. Create the backend services which will then retrieve the dragons details from s3 bucket and also save the details about the new dragons posted by the authenticated 
   users. For this I'm going to use Lambda functions.
5. For the users to post the details about new dragons, to make sure that they are not posting details about the dragon that already exists in database, I'm going to 
   create a another lambda function to validate the dragon details and if they are validated , then add them to dragons database. So now we have 2 lambda functions in 
   the process of saving details about the dragons. To make the functions to works in a sequential manner, I'm going to make use of anonther AWS service called as 
   Amazon Step Functions which will help me to create a workflow for my Lambda functions. To create the workflow design I'm going to use the Amazon States Language(ASL)
   provided by AWS.
6. Lastly to see the progress of these services and functions created I'm going to use Amazon Cloudwatch logs and Amazon X-ray services to monitor the lambda functions, 
   APIs created, and the state machine created. This will help me to troubleshoot any error or erronious behaviour of the application.
   
   
- I'm going to use Amazon Cloud9 IDE to manage and create these services using aws cli and aws sdk for python `boto3`.
