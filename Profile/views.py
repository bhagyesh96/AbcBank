from django.shortcuts import render,redirect
from . import models
from .models import Profile 
from . import forms
import random
from AbcBank import utils
from django.http import HttpResponse
import csv


# Create your views here.
def randomGen():
    # return a 6 digit random number
    return int(random.uniform(100000, 999999))

def index(request):
    
    curr_user = request.user.satus_user.first()
        
    if curr_user == None:
        # if no details exist (new user), create new details
        curr_user = Profile()
        curr_user.account_number = randomGen() # random account number for every new user
        curr_user.balance = 0
        curr_user.user = request.user
        curr_user.save()
    if curr_user.role == 0 :   
        return render(request, "profiles/profile.html", {"curr_user": curr_user})
    else:
        return  redirect("profiles:manager_dash")   


def account_service(request):
    if request.method == "POST":
        
        account_number_receiver = request.POST['account_number']
        amount = request.POST['amount']
        account_receiver = Profile.objects.filter(account_number=account_number_receiver).first()
        account_receiver.balance += int(amount)
        sender_status = request.user.satus_user.all().first()
        sender_status.balance -=  int(amount)
        sender_status.save()
        account_receiver.save()
        transaction = {
            "source":request.user.id,
            "receiver":account_receiver.user.id,
            "amount":amount
        }
        form = forms.MoneyTransferForm(transaction)
        if form.is_valid():
            form.save()
            utils.SendTransactionEmail(account_receiver.user.username,amount,account_number_receiver)

        return redirect("profiles:account_status")
    else:
        return render(request, "profiles/account_service.html")

def add_fund(request):
    if request.method == "POST":
        curr_stat = request.user.satus_user.first()
        curr_stat.balance += int(request.POST['amount'])
        curr_stat.save()
        transaction = {
            "source":request.user.id,
            "receiver":request.user.id,
            "amount":request.POST['amount']
        }
        form = forms.MoneyTransferForm(transaction)
        if form.is_valid():
            form.save()
            utils.SendTransactionEmail(request.user.username,int(request.POST['amount']),curr_stat.account_number)

        return redirect("profiles:account_status")
    else:
        return render(request, "profiles/add_fund.html")

def statement(request):
    if request.method == "POST":
        curr_stat = request.user.satus_user.first()
        from_date =(request.POST['from'])+"T00:00:00"
        to_date =(request.POST['to'])+"T23:59:59"
        transactions = models.Transections.objects.filter(source=request.user,created_datetime__range=[from_date, to_date])
        print(transactions)
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse('text/csv')
        response['Content-Disposition'] = 'attachment; filename=statement.xls'
        # Create the CSV writer using the HttpResponse as the "file"
        writer = csv.writer(response)
        writer.writerow(['id', 'From','To','Amount','Transaction Date'])
        for transaction in transactions:
            writer.writerow([transaction.id, transaction.source.email,transaction.receiver.email,transaction.amount,transaction.created_datetime])
        return response
    else:
        return render(request, "profiles/statement.html")

def managerBank(request):
    if request.method == "POST":
        ac_no =int(request.POST['ac_no'])
        curr_stat = Profile.objects.get(account_number=ac_no)
        from_date =(request.POST['from'])+"T00:00:00"
        to_date =(request.POST['to'])+"T23:59:59"
        transactions = models.Transections.objects.filter(source=curr_stat.user,created_datetime__range=[from_date, to_date])
        print(transactions)
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse('text/csv')
        response['Content-Disposition'] = 'attachment; filename=statement.xls'
        # Create the CSV writer using the HttpResponse as the "file"
        writer = csv.writer(response)
        writer.writerow(['id', 'From','To','Amount','Transaction Date'])
        for transaction in transactions:
            writer.writerow([transaction.id, transaction.source.email,transaction.receiver.email,transaction.amount,transaction.created_datetime])
        return response
    else:
        return render(request, "profiles/bank.html")