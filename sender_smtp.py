import json
import smtplib
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

"""
prep:

pip install sendgrid -t .   (install evertyhing into current working dir, then zip it for lambda exec)
Then zip file.

File: lambda_function
Method_name: lambda_handler

"""

def forward_email(event, context):

    print(event)

    message = Mail(
        from_email='bransfieldjack@gmail.com',
        to_emails='exo.databot@gmail.com',
        subject=event["subject"],
        html_content='Sender:' + ' ' + event["email"] + ' ' + event["message"] + ' ' + event["message"])
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return {
            'statusCode': json.dumps(response.status_code),
            'body': json.dumps(response.body),
            'headers': {
                'Access-Control-Allow-Origin' : '*',
                'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Credentials' : true,
                'Content-Type': 'application/json'
            },
            # 'resp headers': json.dumps(response.headers),
            'test_response': json.dumps(event),
        }
    except Exception as e:
        print(e)
