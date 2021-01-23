import requests
import uuid

# Don't forget to replace with your Cog Services subscription key!
# If you prefer to use environment variables, see Extra Credit for more info.
subscription_key = 'eac8d2c45da94ce58dcf209090b73e78'


# curl -X POST "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=es" \
#      -H "Ocp-Apim-Subscription-Key:eac8d2c45da94ce58dcf209090b73e78" \
#      -H "Ocp-Apim-Subscription-Region:eastus" \
#      -H "Content-Type: application/json" \
#      -d "[{'Text':'Hello, what is your name?'}]"
#

# Our Flask route will supply two arguments: text_input and language_output.
# When the translate text button is pressed in our Flask app, the Ajax request
# will grab these values from our web app, and use them in the request.
# See main.js for Ajax calls.
def get_translation(text_input, language_output):
    base_url = 'https://api.cognitive.microsofttranslator.com/'
    path = '/translate?api-version=3.0'
    params = '&to=' + language_output
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': "eastus",
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text_input
    }]
    response = requests.post(constructed_url, headers=headers, json=body)
    res_json = response.json()
    print(res_json)
    return res_json
