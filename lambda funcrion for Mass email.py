import csv
import boto3
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    ses = boto3.client('ses')

    bucket = 'myemailbucketbybadarqa'
    key = 'uploads/Email.csv'

    try:
        obj = s3.get_object(Bucket=bucket, Key=key)
        body = obj['Body'].read().decode('utf-8-sig')  # removes BOM
        reader = csv.DictReader(io.StringIO(body))
        print(f"Detected headers: {reader.fieldnames}")

        for row in reader:
            email = row.get('email')
            name = row.get('name')
            print(f"Processing: {email}, {name}")

            if email and name:
                ses.send_email(
                    Source='badarqa25@gmail.com',
                    Destination={'ToAddresses': [email]},
                    Message={
                        'Subject': {'Data': 'Lambda SES Test'},
                        'Body': {
                            'Text': {'Data': f"Hello {name}, this is a test email."}
                        }
                    }
                )
                print(f"Email sent to {email}")
            else:
                print(f"Skipped row: {row}")

        return {'statusCode': 200, 'body': 'Emails processed'}
    except Exception as e:
        print(f"Error: {e}")
        return {'statusCode': 500, 'body': str(e)}
