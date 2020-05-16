import hmac
import base64
import hashlib,hmac

import requests
import json
list=[]
token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNoYXJtYWthbmNoYW4zNDRAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiI0MTUzIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMTA5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6IjEwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IkJhc2ljIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMC0wNC0xMyIsImlzcyI6Imh0dHBzOi8vYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTU4ODgzODU4MCwibmJmIjoxNTg4ODMxMzgwfQ.0nzwP7lW4mluNmIIV3z6hywAGzQ1OtfH9CRa_jkFr3g&format=json&language=en-gb"

def symptoms():
    url="https://healthservice.priaid.ch/symptoms?token="+token
    response=requests.get(url)
    x=json.loads(response.content)
    #print(x)
    dict={}
    l=[]
    #print(x[5])
    for i in range(len(x)):
        y=x[i]['ID']
        l.append(y)
        k=x[i]['Name']
        dict[y]=k
    #print(dict)
    #for a,b in dict.items():
        #print(a,b)
    return l
def issues():

    url1="https://healthservice.priaid.ch/issues?token="+token
    response1=requests.get(url1)
    y=json.loads(response1.text)
    print(y)
    l1=[]
    for i in range(len(y)):
        x=y[i]['ID']
        l1.append(x)
    print(l1)
    if 10 in l1:
        print('yes')
def issuesdata():
    url2 = "https://healthservice.priaid.ch/issues/"+str(105)+"/info?&token="+token

#"https://healthservice.priaid.ch/issues/105/info?

    response2 = requests.get(url2)
    z=json.loads(response2.text)
    name=z['Name']
    description=z['Description']
    descriptionshort=z['DescriptionShort']
    medicalcondition=z['MedicalCondition']
    possiblesymptom=z['PossibleSymptoms']
    profname=z['ProfName']
    synonyms=z['Synonyms']
    treatmentdescription=z['TreatmentDescription']
    print(name,treatmentdescription)
def diagnosis():
    urldiag="https://healthservice.priaid.ch/diagnosis?symptoms=[10]&gender=female&year_of_birth=1999&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNoYXJtYWthbmNoYW4zNDRAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiI0MTUzIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMTA5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6IjEwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IkJhc2ljIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMC0wNC0xMyIsImlzcyI6Imh0dHBzOi8vYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTU4ODE2MTg3MSwibmJmIjoxNTg4MTU0NjcxfQ.nrx8IXpHKnaxwN_y3of3mogpXYJx5ok26gkYYctKbXs&format=json&language=en-gb"
    diag=requests.get(urldiag)
    print(diag.text)

def specialisations():
    urlspecial="https://healthservice.priaid.ch/diagnosis/specialisations?symptoms=[15]&gender=female&year_of_birth=1998&token="+token
    response3=requests.get(urlspecial)
    y=json.loads(response3.text)
    print(y)
def proposedsymptoms():
    x=symptoms()
    print(x)
    y=int(input('enter your id:'))
    urlproposed="https://healthservice.priaid.ch/symptoms/proposed?symptoms=["+str(y)+"]&gender=female&year_of_birth=1998&token="+token
    diag=requests.get(urlproposed)
    y=json.loads(diag.text)
    print(y)
def bodylocation():
    urllocation="https://healthservice.priaid.ch/body/locations?token="+token


    diag=requests.get(urllocation)
    x=json.loads(diag.text)
    print(x)
    return x
list=[]
def bodysubloaction():
    x=bodylocation()
    for i in x:
        y=i['ID']
        list.append(y)
    print(list)
    k=int(input("enter any number from above list:"))

    urlsublocation="https://healthservice.priaid.ch/body/locations/"+str(x)+"?token="+token

    diag=requests.get(urlsublocation)
    y=json.loads(diag.text)
    for i in y:
        print(i['Name'])
    print(i)
def bodysymptoms():
    x=int(input("enter 0 for male and 1 for female:"))
    urlbodysymptom="https://healthservice.priaid.ch/symptoms/"+str(x)+"/1?token="+token
    diag=requests.get(urlbodysymptom)
    z=json.loads(diag.text)
    print(z)
def redflag():
    urlredflag="https://healthservice.priaid.ch/redflag?symptomId=105&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNoYXJtYWthbmNoYW4zNDRAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiI0MTUzIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMTA5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6IjEwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IkJhc2ljIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMC0wNC0xMyIsImlzcyI6Imh0dHBzOi8vYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTU4ODE2MjM4NSwibmJmIjoxNTg4MTU1MTg1fQ.sc5SXvbi_Gcz3mpZ3qm5SWUH6hQ6XRJ5BHUABcv877E&format=json&language=en-gb"
    diag=requests.get(urlredflag)
    print(diag.text)
#print("symptoms")
#symptoms()

#print("proposed symptoms")
#proposedsymptoms()
#print("issue")
#issues()
#print("issuedata")
#issuesdata()

#print("diagnosis")
#diagnosis()
#print("specialisations")
#specialisations()

#print("Body location")
#bodylocation()
#print("body subloaction")
#bodysubloaction()
#print("BODY SYMPTOMS")
#print("redflag")
#bodysymptoms()
#redflag()

def create_token():
    username="t8B5W_GMAIL_COM_AUT"
    password="Kf8a4MFx56Sdo7PDg"
    req_uri='https://authservice.priaid.ch/login'

    #some encryption for making a post request , to ask for token from apimedic
    raw_hash=hmac.new(password.encode("utf-8"),req_uri.encode("utf-8"),hashlib.md5)
    computed_hash=base64.b64encode(raw_hash.digest())

    header={
        'Authorization': f"Bearer {username}:{computed_hash.decode('utf-8')}",
    }

    myreq=requests.post(req_uri,headers=header)
    response=myreq.json()

    #check your cmd window , this is your api token
    #you need to create this each time before making
    #request to apimedic
    #print(response['Token'])

    return response['Token']
#y=create_token()
#print(y)
