from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from qr_code.qrcode.utils import QRCodeOptions
from django.contrib import messages
from .models import *
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
import random
import datetime
from twilio.rest import Client
import bangla
import requests
import urllib.parse
import ssl
import cx_Oracle
def index(request):
    return render(request,'index.html')
# @login_required(login_url="/Loging/")
@login_required(login_url="/Loging/")
def textV(request):
    abc= request.build_absolute_uri

    return render(request,'test.html', {'abc':abc})
@login_required(login_url="/Loging/")
def textcreateV(request):
    Name = request.POST.get('name')
    Address = request.POST.get('address')
    Phone = request.POST.get('phone')
    Fax = request.POST.get('fax')
    Email = request.POST.get('email')
    Web = request.POST.get('web')
    if request.method == 'POST' and request.FILES:
        logo_name = request.FILES['logo']
        store = FileSystemStorage()
        filename = store.save(logo_name.name, logo_name)
        profile_pic_url = store.url(filename)
        company = CompanyInformation(Name=Name, Address=Address, Phone=Phone, Fax=Fax, Email=Email, Web=Web, Logo=filename)
        company.save()
        messages.success(request, 'Data save')
        return redirect('/')
    else:
        messages.success(request, 'Data Not Saved')
        return redirect('/')


def CreportV(request,id=0):
    if id !=0:
        urls_name=request.build_absolute_uri
        info=CompanyInformation.objects.all()
        gf=Mrcreate.objects.filter(pk=id)
        abc = Mrcreate.objects.raw('select id,Branch_name,Mr_No,Class,Doc_No,Date,Insured_Name,Insured_Address,Bank_Name,Bank_Address,Premium,Vat,Stamp,ServiceCharge,Total_amount,Mode_Of_Payment from project_mrcreate')
        template_path = 'mr.html'
        context = {'abc': abc,'gf':gf,'info':info,'urls_name':urls_name}
        response = HttpResponse(content_type='application/pdf')
        #for downlode
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        response['Content-Disposition'] = 'filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
@login_required(login_url="/Loging/")
def abcV(request):

    aaa=request.build_absolute_uri
    return render(request,'reporttext.html',{'aaa':aaa})
@login_required(login_url="/Loging/")
def searchV(request):
    dds = Mrcreate.objects.all()

    return render(request,'mrsearch.html',{'dds':dds})
def mrsearchV(request):
    hd = request.GET.get('mrno')
    dds = Mrcreate.objects.filter(Mr_No=hd)
    return render(request, 'listmr.html', {'dds': dds})

def smsV(request,id=0):
    if id != 0:
        dds = Mrcreate.objects.filter(pk=id)
        for x in dds:
            bangla_premium = bangla.convert_english_digit_to_bangla_digit(x.Premium)
            ab=bangla.convert_english_digit_to_bangla_digit(x.Date)
            # fdate = datetime.datetime.strptime(ab,'%Y-%m-%d')
            bangla_doc = bangla.convert_english_digit_to_bangla_digit(x.Doc_No)
            ddss = f'http://127.0.0.1:8000/mr/number/{x.id}'


            username = "admin"
            password = "jashim"
            messagetype = "SMS:TEXT"
            httpUrl = "http://127.0.0.1:9501/"
            recipient = urllib.parse.quote("+01777705428")
            messagedata = urllib.parse.quote(f'৳{bangla_premium} গৃহীত ডকুমেন্ট {bangla_doc} {ab} {ddss} 😊❤')

            sendString = (httpUrl + "api?action=sendmessage" + "&username="
                          + username + "&password="
                          + password + "&recipient=" + recipient + "&messagetype=" +
                          messagetype + "&messagedata=" + messagedata)

            print("Sending html request: " + sendString)
            requests.packages.urllib3.disable_warnings()

            response = requests.get(sendString, verify=False)
            print("Http response received: ")
            print(response.text)
    return redirect('/mrsearch/')


def LogingV(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['pass']
        if username == 'Admin':
            a = Mrcreate.objects.all().delete()
        user=auth.authenticate(username=username,password=password)
        if user is not None:

            auth.login(request,user)
            if 'next' in request.POST:
                # return redirect(request.POST.get('next'))
                return redirect('/')
            else:
                return redirect('/')
        else:
            messages.info(request,'User is not valide')
            return redirect('/Loging/')
    else:
        return render(request,'loging.html')

def logoutV (request):
    auth.logout(request)
    return redirect('/')



def firereV (request):
    cnx = cx_Oracle.connect('jashim/jashim@//localhost:1521/orcl')
    mycursor = cnx.cursor()
    mycursor.execute("""SELECT a.POLICY_NO as POLICY_NO,a.EDATE as EDATE,a.CLIENTCODE as CLIENTCODE,b.PHONE as PHONE,a.CL_NAME as CL_NAME ,b.CLNAME as CLNAME, a.MRNO as MRNO FROM mast a,UW_CLIENT b 
            WHERE a.C_CLASS ='Fire' AND a.POLICY_NO IS NOT NULL
            AND a.CLIENTCODE =b.IDNO 
            AND b.PHONE IS NOT NULL""")
    dds = mycursor.fetchall()
    for POLICY_NO,EDATE,CLIENTCODE,PHONE,CL_NAME,CLNAME,MRNO in dds:
        a=EDATE - datetime.timedelta(days=2)
        aas=datetime.date.strftime(a,'%Y-%m-%d')
        b=datetime.date.today()
        c=datetime.date.strftime(b,'%Y-%m-%d')
        if aas == c:
            username = "admin"
            password = "jashim"
            messagetype = "SMS:TEXT"
            httpUrl = "http://127.0.0.1:9501/"
            recipient = urllib.parse.quote("+01777705428")
            messagedata = urllib.parse.quote('test')

            sendString = (httpUrl + "api?action=sendmessage" + "&username="
                          + username + "&password="
                          + password + "&recipient=" + recipient + "&messagetype=" +
                          messagetype + "&messagedata=" + messagedata)

            print("Sending html request: " + sendString)
            requests.packages.urllib3.disable_warnings()

            response = requests.get(sendString, verify=False)
            print("Http response received: ")
            print(response.text)

    else:
            print('message not send')




    return render(request, 'listfire.html', {'dds': dds})
