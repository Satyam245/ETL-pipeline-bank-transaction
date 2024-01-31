import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')

    job_name = 'your_transaction_data_processing_job'  # Replace with your Glue job name

    args = {
        '--JOB_NAME': 'transaction_data_processing_job',
    }

    response = glue.start_job_run(JobName=job_name, Arguments=args)

    return {
        'statusCode': 200,
        'body': response
    }
