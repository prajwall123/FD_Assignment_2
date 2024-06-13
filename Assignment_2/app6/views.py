from django.shortcuts import render,get_object_or_404
from app6.forms import inputform
from .models import Accounts,CustomerAccount
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()
            try:
                last_account = Accounts.objects.latest('id')
                new_customer_id = last_account.customer_id
            except Accounts.DoesNotExist:
                new_customer_id = 8001
            return render(request,'app6/index.html',{'form':form1,'cus_id':new_customer_id})
    else:
        form1=inputform() #if it is a GET Request present an empty form
    return render(request,'app6/index.html',{'form':form1})


def openaccount(request, cus_id):
    customer = get_object_or_404(Accounts, customer_id=cus_id)
    if request.method == "POST":
        account_type = request.POST.get('account_type')
        initial_amount = float(request.POST.get('initial_amount'))
        if account_type == 'LOAN':
            initial_amount = -abs(initial_amount)
        account=CustomerAccount.objects.create(customer=customer, account_type=account_type, balance=initial_amount)
        return render(request, 'app6/success.html', {'customer': customer,'account':account})
    return render(request, 'app6/account.html', {'customer': customer})


# Create your views here.
