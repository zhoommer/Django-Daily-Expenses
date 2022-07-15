from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404
from django.contrib import messages
from .models import Expenses
from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum
# Create your views here.


def home(request):
##################### PAGINATOR ############################################################
    
    expenses = Expenses.objects.all().order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(expenses, 10)
    try:
        expenses = paginator.page(page)
    except PageNotAnInteger:
        expenses = paginator.page(1)
    except EmptyPage:
        expenses = paginator.page(paginator.num_pages)
#############################################################################################
########################### GET CATEGORIES ##################################################
    categories = Expenses.objects.values_list('category', flat=True).distinct()
#############################################################################################
################################ GET SUM AMOUNT #########################################

    amount = Expenses.objects.filter(category='Electronics').aggregate(Sum('amount'))
    print(amount)

###########################################################################################
    content = {
        'expenses': expenses,
        'categories' : categories
            }
################### ADD EXPENSE ###############################
    if request.method == 'POST':
        # get form values
        payment_method = request.POST.get('payment_method')
        category = request.POST.get('category')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')

        if amount.isalpha() == True:
            messages.add_message(request, messages.ERROR, 'Amount can only be numbers!')
        else:

            expense = Expenses.objects.create(payment_method=payment_method,
                    category=category, item=item, quantity=quantity,
                    amount=amount)

            expense.save()
            messages.add_message(request, messages.SUCCESS, 'The record was created successfully.')
            return redirect('home')
##########################################################################

    return render(request, 'core/home.html', content)


def delete(request):
    expenses = Expenses.objects.all().order_by('-date')
    if request.method == 'POST':
        id_list = request.POST.getlist('checkbox')
        for x in id_list:
            expenses.filter(id=x).delete()
        messages.add_message(request, messages.SUCCESS, 'The selected expenses have been deleted successfully.')
        return redirect('home')
    else:
        pass
        #messages.add_message(request, messages.ERROR, 'Something is wrong...!')
    content = {
        'expenses': expenses,
            }
    return render(request, 'core/delete.html', content)
