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

url = "https://us2-smax.saas.microfocus.com/rest/107894932/ems/Change/751624?layout=AffectsActualService,BasedOnChangeModel,BasedOnChangeModel,Category,ChangeImplementationGroup_c,ChangeImplementationOwner_c,DatacenterLocation_c,Description,DisplayLabel,Id,NotificationtocustomerRequired_c,Priority,ReasonForChange,RiskAssessment,Urgency"

payload={}
headers = {
  'Cookie': 'LWSSO_COOKIE_KEY=' + key,
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
