
#Missing:
# To update and change we need to parse the Id and LastUpdateTime
# Actually we need to parse everyingthing from the get and deside what to update.
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
        "AffectsActualService": 15797,
        "BasedOnChangeModel": 691245,
        "Category": 15103,
        "ChangeImplementationGroup_c": 10003,
        "ChangeImplementationOwner_c": 748862,
        "DatacenterLocation_c": 11331,
        "DisplayLabel": "Python3-Working",
        "Id": "751624",
        "LastUpdateTime": 1657808380502,
        "NotificationtocustomerRequired_c": "Yes_c",
        "OwnedByGroup": 10003,
        "PeerReviewGroup_c": 10004,
        "Product_c": 14484,
        "ReasonForChange": "Legislation",
        "RequestedByPerson":748862,
        "RiskAssessment": "NoRisk",
        "Urgency": "SlightDisruption"

      }
    }
  ],
  "operation": "UPDATE"
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'LWSSO_COOKIE_KEY=' + key,
  'SMAX_AUTH_TOKEN': key,
  'User-Agent': 'Apache-HttpClient/4.1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
