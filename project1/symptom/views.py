import datetime   #from datetime import datetime--------datetime.now()
import json
from cProfile import Profile
import requests
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth,User
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic.base import View
from django.contrib.auth.models import auth,User
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
import hmac
import base64
import hashlib
from .models import meddata
from .Model_Class import Modeldiag,Modelissue,Modeldat
from .models import contact,meddata,body_loc1,body_data1,sub_body1

#index/home
def index(request):
    return render(request,'index.html')
#covid19
def covid(request):
    return render(request,'covid19.html')
#covid-treatment
def treatment(request):
    return render(request,'treatment.html')
#covid-symptoms
def symptoms(request):
    return render(request,'symptoms.html')
#covid-prevention
def prevention(request):
    return render(request,'prevention.html')
#basic-page-layout
def basic(request):
    return render(request,'basic.html')
#about
def about(request):
    return render(request,'about.html')


l=[]
#token for api
def create_token():
    username="sharmakanchan344@gmail.com"
    password="c3LCb6n5Y9RaTm42P"
    req_uri='https://sandbox-authservice.priaid.ch/login'
    raw_hash=hmac.new(password.encode("utf-8"),req_uri.encode("utf-8"),hashlib.md5)
    computed_hash=base64.b64encode(raw_hash.digest())
    header={
        'Authorization': f"Bearer {username}:{computed_hash.decode('utf-8')}",
    }
    myreq=requests.post(req_uri,headers=header)
    response=myreq.json()
    return response['Token']

dict = {}
#body location
def bodyloc(request):
    list = []
    token=create_token()
    urllocation="https://sandbox-healthservice.priaid.ch/body/locations?token="+token+"&format=json&language=en-gb"
    response = requests.get(urllocation)
    document = json.loads(response.text)
    for x in document:
        id = x['ID']
        name = x['Name']
        dict.update({name:id})
    return render(request, 'bodyloc.html', {"dict":dict})
#subbody ,location
def subbody(request):
    listt = []
    print("working")
    if request.method == 'POST':
        bodyID = request.POST['symid']
        age=request.POST.get('yearofbirth','')
        gender1=request.POST.get('gender','')
        y=age
        if gender1=='0':
            l.append("male")
        else:
            l.append("female")
        gender=l[0]
        gender1=meddata(med_age=age,med_gender=gender)
        gender1.save()
        token=create_token()
        urllocation="https://sandbox-healthservice.priaid.ch/body/locations?token="+token+"&format=json&language=en-gb"
        response = requests.get(urllocation)
        document = json.loads(response.content)
        dict={}
        for x in document:
            id = x['ID']
            name = x['Name']
            dict.update({name:id})
        key_list = list(dict.keys())
        val_list = list(dict.values())
        m=int(bodyID)
        z=val_list.index(m)
        bodypart=key_list[z]
        bodypart=bodypart.title()
        print(bodypart)
        s2=body_loc1(med_bodyloc=bodypart,med_bodylocno=bodyID)
        s2.save()
        token=create_token()
        urlsublocation="https://sandbox-healthservice.priaid.ch/body/locations/"+str(bodyID)+"?token="+token+"&format=json&language=en-gb"
        response = requests.get(urlsublocation)
        document = json.loads(response.text)
        dict1={}
        for x in document:
            id = x['ID']
            name = x['Name']
            dict1.update({name:id})
        gender=gender.title()
        age=2020-int(y)
    return render(request, "subbody.html",{"dict1":dict1,'gender':gender,'age':age,'bodypart':bodypart})
#bodysymptoms
def bodydata(request):
    if request.method == 'POST':
        bodylo = request.POST['symid']
        token=create_token()
        val=body_loc1.objects.all()
        x=list(val)
        l1=[]
        for a in x:
            l1.append(a.med_bodyloc)
        bodystart=l1[-1]
        bodystart=bodystart.title()
        val=body_loc1.objects.all()
        x=list(val)
        l1=[]
        for a in x:
            l1.append(a.med_bodylocno)
        bodystartno=l1[-1]
        token=create_token()
        urlsublocation="https://sandbox-healthservice.priaid.ch/body/locations/"+str(bodystartno)+"?token="+token+"&format=json&language=en-gb"
        response = requests.get(urlsublocation)
        document = json.loads(response.content)
        dict={}
        for x in document:
            id = x['ID']
            name = x['Name']
            dict.update({name:id})
        key_list = list(dict.keys())
        val_list = list(dict.values())
        m=int(bodylo)
        z=val_list.index(m)
        bodysubpart=key_list[z]
        bodysubpart=bodysubpart.title()
        g1=sub_body1(med_subbody=bodysubpart,med_subbodyno=bodylo)
        g1.save()
        val=meddata.objects.all()
        x=list(val)
        l1=[]
        for a in x:
            l1.append(a.med_gender)
        gen=l1[-1]
        l2=[]
        if gen=="male":
            l2.append(0)
        else:
            l2.append(1)
        y=l2[0]
        val=meddata.objects.all()
        x=list(val)
        for a in x:
            l1.append(a.med_gender)
        gender=l1[-1]
        val=meddata.objects.all()
        x=list(val)
        for k in x:
            l1.append(k.med_age)
        age=l1[-1]
        gender=gender.title()
        age=2020-int(age)
        urlbodysymptom="https://sandbox-healthservice.priaid.ch/symptoms/"+str(bodylo)+"/"+str(y)+"?token="+token+"&format=json&language=en-gb"
        diag=requests.get(urlbodysymptom)
        z=json.loads(diag.text)
        dict2={}
        for x in range(len(z)):
            id = z[x]['ID']
            name = z[x]['Name']
            dict2.update({name:id})
        return render(request, 'bodydata.html', {"dict2":dict2,'bodystart':bodystart,'bodysubpart':bodysubpart,'gender':gender,'age':age})
#diagnosis result
def result(request):
    if request.method == 'POST':
        bodylo = request.POST['symid']
        token=create_token()
        val=meddata.objects.all()
        x=list(val)
        l1=[]
        for a in x:
            l1.append(a.med_gender)
        gen=l1[-1]
        l2=[]
        if gen=="male":
            l2.append(0)
        else:
            l2.append(1)
        y=l2[0]
        val=sub_body1.objects.all()
        x=list(val)
        l1=[]
        for a in x:
            l1.append(a.med_subbodyno)
        bodylono=l1[-1]
        urlbodysymptom="https://sandbox-healthservice.priaid.ch/symptoms/"+str(bodylono)+"/"+str(y)+"?token="+token+"&format=json&language=en-gb"
        response = requests.get(urlbodysymptom)
        document = json.loads(response.content)
        dict={}
        for x in document:
            id = x['ID']
            name = x['Name']
            dict.update({name:id})
        key_list = list(dict.keys())
        val_list = list(dict.values())
        m=int(bodylo)
        z=val_list.index(m)
        bodysymptom=key_list[z]
        bodysymptom=bodysymptom.title()
        val=meddata.objects.all()
        x=list(val)
        l1=[]
        for a in x:
            l1.append(a.med_gender)
        gen=l1[-1]
        l2=[]
        for b in x:
            l2.append(b.med_age)
        age=l2[-1]
        token=create_token()
        urldiag="https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=["+str(bodylo)+"]&gender="+gen+"&year_of_birth="+str(age)+"&token="+token+"&format=json&language=en-gb"
        diag=requests.get(urldiag)
        z=json.loads(diag.text)
        dict2={}
        for x in range(len(z)):
            k = z[x]['Issue']
            id=k["ID"]
            name = k['Name']
            dict2.update({name:id})
        val=body_loc1.objects.all()
        x=list(val)
        l1=[]
        for a in x:
            l1.append(a.med_bodyloc)
        bodystart=l1[-1]
        val=sub_body1.objects.all()
        x=list(val)
        l1=[]
        for a in x:
            l1.append(a.med_subbody)
        bodysubpart=l1[-1]
        bodystart=bodystart.title()
        bodysubpart=bodysubpart.title()
        val=meddata.objects.all()
        x=list(val)
        for a in x:
            l1.append(a.med_gender)
        gender=l1[-1]
        val=meddata.objects.all()
        x=list(val)
        for k in x:
            l1.append(k.med_age)
        age=l1[-1]
        gender=gender.title()
        age=2020-int(age)
        return render(request, 'result.html', {"dict2":dict2,'bodystart':bodystart,'bodysubpart':bodysubpart,'bodysymptom':bodysymptom,"gender":gender,'age':age})
#diagnose treatment
def diagme(request):
    if request.method == 'POST':
        bodylo = request.POST['symid']
        token=create_token()
        urldiag="https://sandbox-healthservice.priaid.ch/issues/"+str(bodylo)+"/info?token="+token+"&format=json&language=en-gb"
        diag=requests.get(urldiag)
        z=json.loads(diag.text)
        k=z['PossibleSymptoms']
        print(k)
        y=z['TreatmentDescription']
        m=k.split(',')
        l1=[]
        for i in m:

            l1.append(i.title())
        print(l1)
        return render(request, 'diagme.html', {'l1':l1,'TreatmentDescription':y})
#india data
def indiadata(request):
    url="https://api.covid19india.org/data.json"
    data=requests.get(url)
    document=json.loads(data.text)
    x=document['cases_time_series']
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    l6=[]
    l7=[]
    l8=[]
    l9=[]
    for i in x:
        date=i['date']
        l5.append(date)
        dailyrecovered=i['dailyrecovered']
        totalconfirmed=i['totalconfirmed']
        l1.append(totalconfirmed)
        dailyconfirmed=i['dailyconfirmed']
        totalrecoverded=i['totalrecovered']
        l2.append(totalrecoverded)
        totaldeath=i['totaldeceased']
        l3.append(totaldeath)
        l6=[date,totalconfirmed,totalrecoverded,totaldeath,dailyconfirmed,dailyrecovered]
        l7.append(l6)
        l8.append(int(dailyconfirmed))
        l9.append(date)
    l7.reverse()

    k=l1[-1]
    l=l2[-1]
    m=l3[-1]

    return render(request,'indiadata.html',{'totalconfirmed':k,'totalrecovered':l,'totaldeath':m,'dict':l7,'dictl8':l8,'dictl9':l9})
#covid-state data
def covidstate(request):
    url="https://api.covid19india.org/data.json"
    data=requests.get(url)
    document=json.loads(data.text)
    z=document['statewise']
    listt=[]
    l11=[]
    l12=[]
    l13=[]
    l14=[]
    for i in range(len(z)):
        if i==0:
            continue
        else:
            l1=z[i]['state']
            l2=z[i]['confirmed']
            l3=z[i]['active']
            l4=z[i]['deaths']
            l5=z[i]['lastupdatedtime']
            l6=l5[0:10]
            l7=z[i]['recovered']
            l8=[l1,l2,l3,l4,l7,l6]
            listt.append(l8)
            if int(l2)>2000:
                l11.append(l1)
                l12.append(l2)

            if int(l2)<25:
                l13.append(l1)
                l14.append(l2)


    return render(request,'covidstate.html',{'dict':listt,'dictmn':l13,'dictmn1':l14,'dictmx':l11,'dictmx1':l12})
#covid-world data
def covidworld(request):
    url="https://api.covid19api.com/summary"
    data=requests.get(url)
    document=json.loads(data.text)
    z=document['Global']
    totalconfirmedworld=z['TotalConfirmed']
    totalrecoveredworld=z['TotalRecovered']
    totaldeathworld=z['TotalDeaths']
    dat=document['Countries']
    listt=[]
    l3=[]
    l4=[]
    l2=[]
    l5=[]
    l6=[]
    l7=[]
    l8=[]
    l9=[]
    l10=[]
    for i in dat:
        country=i['Country']
        confirmed=i['TotalConfirmed']
        death=i['TotalDeaths']
        recovered=i['TotalRecovered']
        if confirmed<15:
            l2.append(country)
            l4.append(confirmed)
        if confirmed>200000:
            l5.append(country)
            l6.append(confirmed)
        if death>5000:
            l7.append(country)
            l8.append(death)
        if death==0:
            l9.append(country)
            l10.append(death)
        l1=[country,confirmed,recovered,death]
        listt.append(l1)
    print(len(l7))
    print(len(l9))



    return render(request,'covidworld.html',{"totalconfirmedworld":totalconfirmedworld,"totalrecoveredworld":totalrecoveredworld,"totaldeathworld":totaldeathworld,'dict':listt,'dict2':l2,'dict4':l4,'dict5':l5,'dict6':l6,'dict7':l7,'dict8':l8,'dict9':l9,'dict10':l10})

#contact-form
def contact1(request):
    if request.method=='POST':
        first_name=request.POST.get('firstname','')
        last_name=request.POST.get('lastname','')
        email=request.POST.get('email','')
        subject=request.POST.get('subject','')
        feedback=request.POST.get('feedback','')
        contact1=contact(contact_first=first_name,contact_last=last_name,contact_email=email,contact_subject=subject,contact_feedback=feedback)
        contact1.save()
        messages.success(request,'Your Query Successfully Submitted. ')
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')
#login-page
def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            request.session['username'] = username
            request.session['pk']=user.pk
            request.session.set_expiry(300)
            return render(request,'index.html',{"data":username,"Flag":True})
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html',{"status":"Invalid credentials"})
    else:
        return render(request,'login.html')
#logout
def logout(request):
    auth.logout(request)
    return redirect('/')
#registration
def registration(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        first_name=first_name.title()
        last_name=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['cpassword']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('registration.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('registration.html')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save();
                return render(request,'login.html')


        else:
            messages.info(request,"password doesnot match")
            return redirect('registration.html')
    else:
        return render(request,'registration.html')
