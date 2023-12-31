import requests, json, os

SMAXUSER = os.environ['SMAXUSER']
SMAXPW = os.environ['SMAXPW']
def get_key():
    url = "https://us2-smax.saas.microfocus.com/auth/authentication-endpoint/authenticate/token?TENANTID=107894932"    
    payload = json.dumps({
        "Login": SMAXUSER,
        "Password": SMAXPW})
    headers = {
        'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

get_key()
key = get_key()

url = "https://us2-smax.saas.microfocus.com/rest/107894932/ems/bulk"

payload = json.dumps({
  "entities": [
    {
      "entity_type": "Change",
      "properties": {
        "AffectsActualService": "15797",
        "BasedOnChangeModel": "46415",
        "ChangeImplementationGroup_c":"736393",
        "ChangeImplementationOwner_c":"367243",
        "DatacenterLocation_c":"12648",
        "DataDomains": [
          "Public"
        ],
        "Description": "<p>Git in Action</p>",
        "DetectedEntities": "{\"complexTypeProperties\":[]}",
        "DisplayLabel": "Using Git Actions",
        "Justification": "<p>Testing Github</p>",
        "ReasonForChange": "BusinessRequirement",
        "Urgency":"SlightDisruption",
        "UserOptions": "{\"complexTypeProperties\":[{\"properties\":{}}]}"
      }
    }
  ],
  "operation": "CREATE"
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'LWSSO_COOKIE_KEY=' + key,
  'SMAX_AUTH_TOKEN': key,
  'User-Agent': 'Apache-HttpClient/4.1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)