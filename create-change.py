import requests, json
def get_key():
    url = "https://us2-smax.saas.microfocus.com/auth/authentication-endpoint/authenticate/token?TENANTID=107894932"
    
    payload = json.dumps({
        "Login": "IntUser_PSDC",
        "Password": "Testing@123456"})
    headers = {
        'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    #print(response.text)
    return response.text

get_key()

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
