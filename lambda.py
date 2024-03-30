import json
import urllib.request
import urllib.parse

def lambda_handler(event, context):
    print(event)
    try:
        body = json.loads(event['body'])
        print(body)
        
        message_part = body['message'].get('text')
        print("Message part: {}".format(message_part))
        
        data = {'url': message_part}
        data = urllib.parse.urlencode(data).encode('utf-8')
        
        with urllib.request.urlopen('https://cleanuri.com/api/v1/shorten', data=data) as response:
            short_url = json.loads(response.read())['result_url']
            print("The short URL is: {}".format(short_url))
        
        chat_id = body['message']['chat']['id']
        
        url = f'https://api.telegram.org/bot7196704687:AAGYm5_VEyUECYS-UQsmHPtdUDxmc5s8bFM/sendMessage'
        payload = {
            'chat_id': chat_id,
            'text': short_url
        }
        
        payload = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
        
        with urllib.request.urlopen(req) as response:
            response_text = response.read().decode('utf-8')
            print(response_text)
        
        return {"statusCode": 200}
    except Exception as e:
        print("Error:", e)
        return {"statusCode": 500}
