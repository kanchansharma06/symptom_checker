import requests
import json
list=[]
token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNoYXJtYWthbmNoYW4zNDRAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiI0MTUzIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMTA5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6IjEwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IkJhc2ljIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMC0wNC0xMyIsImlzcyI6Imh0dHBzOi8vYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTU4ODg2NjE2MCwibmJmIjoxNTg4ODU4OTYwfQ.v5tYtSEEzpLiyqMOE6og9OOw93JTYHWXpC9hDbwzGRM&format=json&language=en-gb"

def bodylocation():
    urllocation="https://healthservice.priaid.ch/body/locations?token="+token


    diag=requests.get(urllocation)
    x=json.loads(diag.text)
    print(x)
    return x
bodylocation()
list=[]
def bodysubloaction():
    x=bodylocation()
    for i in x:
        y=i['ID']
        list.append(y)
    print(list)
    k=int(input("enter any number from above list:"))

    urlsublocation="https://healthservice.priaid.ch/body/locations/"+str(k)+"?token="+token

    diag=requests.get(urlsublocation)
    y=json.loads(diag.text)
    print(y)
    return y
def bodysymptoms():
    k=bodysubloaction()

    z=int(input("enter no from above list"))
    x=int(input("enter 0 for male and 1 for female:"))

    urlbodysymptom="https://healthservice.priaid.ch/symptoms/"+str(z)+"/"+str(x)+"?token="+token
    diag=requests.get(urlbodysymptom)
    z=json.loads(diag.text)
    print(z)
    for i in range(len(z)):
        print(z[i]['ID'])
    return z
bodysymptoms()
def diagnosis():
    m=bodysymptoms()
    print(m)
    k=int(input("enter your symptom:"))
    urldiag="https://healthservice.priaid.ch/diagnosis?symptoms=["+str(k)+"]&gender=female&year_of_birth=1999&token="+token
    diag=requests.get(urldiag)
    a=json.loads(diag.text)
    return a
def issuesdata():
    l=diagnosis()
    print(l)
    n=int(input("enter number:"))
    url2 = "https://healthservice.priaid.ch/issues/"+str(n)+"/info?&token="+token

#"https://healthservice.priaid.ch/issues/105/info?

    response2 = requests.get(url2)
    z=json.loads(response2.text)
    print(z["TreatmentDescription"])



#bodylocation()
#bodysubloaction()
#bodysymptoms()
diagnosis()
#issuesdata()
