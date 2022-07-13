from ast import In
import requests, json, os

#https://medium.datadriveninvestor.com/accessing-github-secrets-in-python-d3e758d8089b#:~:text=To%20add%20a%20new%20secret,in%20your%20GitHub%20actions%20workflow.
'''
In [ ]:
        SMAXUSER = os.environ['SMAXUSER']
        SMAXPW = os.environ['SMAXPW']
'''
def get_key():
    url = "https://us2-smax.saas.microfocus.com/auth/authentication-endpoint/authenticate/token?TENANTID=107894932"    
    payload = json.dumps({
        "Login": "SMAXUSER",
        "Password": "SMAXPW"})
    headers = {
        'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


key = get_key()

url = "https://us2-smax.saas.microfocus.com/rest/107894932/ems/bulk"

payload = json.dumps({
  "entities": [
    {
      "entity_type": "Change",
      "properties": {
        "ReasonForChange": "BusinessRequirement",
        "AffectsActualService": "15797",
        "BasedOnChangeModel": "46415",
        "DisplayLabel": "something new 02 python",
        "Description": "<p>some</p>",
        "UserOptions": "{\"complexTypeProperties\":[{\"properties\":{}}]}",
        "DataDomains": [
          "Public"
        ],
        "Justification": "<p>some</p>",
        "DetectedEntities": "{\"complexTypeProperties\":[]}"
      }
    }
  ],
  "operation": "CREATE"
})
headers = {
  'Cookie': 'LWSSO_COOKIE_KEY=' + key,
  'Content-Type': 'application/json',
  'User-Agent': 'Apache-HttpClient/4.1',
  'SMAX_AUTH_TOKEN': key
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)