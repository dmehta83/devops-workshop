def lambda_handler(event, context):
    body='Hello from Lambda!. ARN: '+context.invoked_function_arn
    return {
        'statusCode': 200,
        'body': body
    }