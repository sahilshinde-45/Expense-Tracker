import json

import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from tablib import Dataset

from .forms import FormProfile, MyUserCreationForm
from .models import *
from .resources import *

# Create your views here.


def register_user(request):
    fm  =  MyUserCreationForm()
    if request.method == "POST":
        fm = MyUserCreationForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    return render(request,'Tracker/Register.html',{'register_form':fm})

def login_user(request):
    login_message_error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') 
        login_message_error = "Username or Password is incorrect !!" 
    return render(request,'Tracker/login.html',{'login_message_error':login_message_error})

def logout_user(request):
    logout(request)
    return redirect('/login/')

response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=56c65b60f1b1854bf84066d5c4095969&format=1')
data = response.json()
temp = None
#print('temp-global',temp)


def trial(currency):
    final = data['rates'][currency]
    return final

@login_required(login_url='/login/')
def home_page(request):
    user  = request.user 
    #global temp
    fm = FormProfile()
    cur = None
    
    if request.method == "POST":
        cur = request.POST.get('currency')
        print(cur)
        rates = trial(cur)
        print(rates) 
        fm = FormProfile(request.POST)
        if fm.is_valid():
            fm.instance.user = request.user
            income = fm.cleaned_data['income']
            fm.instance.currency_type = cur
            fm.instance.curr_value = rates
            #print('income',income)
            balance = fm.cleaned_data['balance']
            #print('balance',balance)
            income1 = income//rates
            fm.instance.income = income1
            #print(income1)
            balance1 = balance//rates
            fm.instance.balance = balance1
            #print(balance1)
            
            fm.save()
            #temp = rates
            #print('inside-temp',temp)
            return redirect("/")
            
            
        else:
            messages.error(request,"SOMETHING WENT WRONG TRY AGAIN") 

    list_all = Profile.objects.filter(user = user)
    
    

    context = {'form':fm , 'list_all':list_all}
   
    return render(request,'Tracker/index.html',context)


""" def conversion(request):
    user = request.user
    data = json.loads(request.body)
    rates = data['conversion_rates']
    final_amt = data ['income']
    balance = data['balance']
    income_category = data['income_category']
   
    print(final_amt)
    print(rates)
    print(income_category)
    print(balance) 
   


    x =  Profile.objects.create(
        user = user,
        income = final_amt,
        income_category = income_category,
        balance = balance,
        

    )
    x.save() 
   
    
    
    return JsonResponse('conversion done successfully', safe=False) """

def upload_file(request):
    try:

        if request.method == "POST":
            add_Excel = Add_Excel_Resources()
            dataset = Dataset()
            new_file = request.FILES['myfile']
            if not new_file.name.endswith('xlsx'):
                messages.info(request,'wrong format')
            imported_data = dataset.load(new_file.read(),format='xlsx')
            print(len(imported_data))
            for data in imported_data:
                value = Add_Excel(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4]    
                )
                print(data[3])
                
                value.save()
        
            return redirect('/upload/')
        user = request.user
        list_all = Add_Excel.objects.filter(user = user)
        return render(request,'Tracker/upload.html',{'list_all': list_all})
    except:
        return HttpResponse("<center><strong> FIle should not be empty \n Format should be as mentioned </strong></center>")

@login_required(login_url='/login/')
def track_history(request,id):
    user = request.user
    expenses = Tracker.objects.filter(user = id)
    print(expenses)

    
    return render(request,'Tracker/track_history.html',{'expenses':expenses})

@login_required(login_url='/login/')
def edit_expenses(request,id):
    user  = request.user
    temp 
    profile_ = Profile.objects.get(id = id)
    value = profile_.curr_value
    print(value)
    expenses = Tracker.objects.filter(user = profile_)
    print('temp-edit',temp)
    print(type(temp))
    
    if request.method == "POST":
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('type')
        Category = request.POST.get('category')
        am = float(amount)
        print(type(am))
        amount1 = am//value
        print('edit-amount',amount)
       
        

        print(text , amount , expense_type)
        expense = Tracker(name = text, amount = amount1 , expence_type = expense_type ,user = profile_ , category = Category)
        expense.save()

        if expense_type == 'positive':
            profile_.balance += float(amount1)
        else:
            profile_.expenses += float(amount1)
            profile_.balance  -= float(amount1)
        profile_.save()
        return redirect ('/') 
    

    context = {'profile':profile_,'expenses':expenses}
    return render (request,'Tracker/edit-tracker.html',context)

@login_required(login_url='/login/')
def report(request):
    user = request.user
    profile_ = Profile.objects.filter(user = user)
   
    expenses = Tracker.objects.all()
    
    
    context = {'profile': profile_,'expenses':expenses , 'user':user}
    return render(request,'Tracker/barchartjs.html',context)
    
@login_required(login_url='/login/')
def report_data(request):
    user  =  request.user
    profile_ = Profile.objects.filter(user = user)

 
    

    context = {'expense':profile_}

    return render(request,'Tracker/report-data.html',context)
