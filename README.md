# Install Serverless
Serverless is a cool library you could use to deploy your serverless applications. You can learn more about serverless at [serverless.com](https://serverless.com/)
## How to install
Simply follow the instruction on the website to install it! It's basically
```
npm install -g serverless
```
# Serverless Commands with AWS Lambda backend

## General
|Command|Description |
|--|--|
|`serverless`|lists all the commands available in serverless|
|`sls`|lists all the commands available in serverless|

## Creating and Deploying a service
|Command|Description |
|--|--|
|`sls deploy -v`|deploy the whole stack|
|`sls deploy function -f your_function_name`|deploy a specific updated function! (Much faster)|

```
# Install a service with aws-python template
sls create --template aws-python --path hello-world-python

# Deploy a service 
sls deploy -v
```
Then make sure you modify the serverless.yml file and add these key values:
```
profile: serverless-admin
region: your_aws_region
```
You can check AWS console lambda to check out your service worked!

## Invoke a function
|Command|Description |
|--|--|
|`sls invoke -f your_function_name -l`|invoke function your_function_name and get the logs|

```
# invoke a function and get the logs
sls invoke -f hello -l
```

# Fetching function logs
To check for logs on AWS console simply go to AWS lambda and click on ```check logs on CloudWatch```
You can also check the logs locally using this command:
|Command|Description |
|--|--|
|`sls logs -f your_function_name -t`|get the logs for function your_function_name and tail it!|

## Destroy a service
We need to clean up Fucction, Dependencies of function, CloudWatch log groups, IAM roles!
|Command|Description |
|--|--|
|`sls remove`|THE PURGE!|

# More on AWS Lambda Functions
## Timeout and Memory
Timeout determines the maximum duration your function is allowed to execute and return the results. If that exceeds the timeout value
then !!!
Modify the serverless.yml file as follows:
```
functions:
  function_name:
    handler: handler.hello
    timeout: some_seconds
    memorySize: memory_in_MBs

```