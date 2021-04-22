import json
import pdb

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from src.expenses.models import Category, Expenses


@login_required(login_url='/auth/login')
def index(request):
    expenses = Expenses.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 2)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    return render(request, 'expenses/index.html', context={
        'expenses': expenses,
        'page_obj': page_obj,
    })


class ExpensesView(View):
    def get(self, request):
        context = self.context(request)
        return render(request, 'expenses/add_expenses.html', context)

    def post(self, request):
        context = self.context(request)

        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['date']
        category = request.POST['category']
        owner = request.user

        if amount:
            Expenses.objects.create(amount=amount, description=description,
                                    date=date, category=category, owner=owner)
            messages.success(request, 'You have successfully add your expenses')
            return redirect('index')
        else:
            messages.error(request, 'Oops! amount can not be empty')
            return render(request, 'expenses/add_expenses.html', context)

    @staticmethod
    def context(request):
        categories = Category.objects.all()
        return {
            'categories': categories,
            'old': request.POST
        }


class ExpenseUpdateView(View):
    @method_decorator(login_required(login_url='/auth/login'))
    def get(self, request, user_id):
        expense = Expenses.objects.get(pk=user_id)
        categories = Category.objects.all()
        context = {
            'categories': categories,
            'expense': expense
        }
        return render(request, 'expenses/update_expenses.html', context)

    def post(self, request, user_id):
        amount = request.POST['amount']
        expense = Expenses.objects.get(pk=user_id)

        if amount:

            expense.amount = amount
            expense.category = request.POST['category']
            expense.description = request.POST['description']
            expense.date = request.POST['date'] if request.POST['date'] != '' else expense.date
            expense.save()

            messages.success(request, 'Expenses has been updated successfully')
            return redirect('index')
        else:
            messages.error(request, 'Oops! amount can not be empty')
            return render(request, 'expenses/update_expenses.html')


class ExpenseDeleteView(View):
    def get(self, request, user_id):
        expense = Expenses.objects.get(pk=user_id)
        expense.delete()
        messages.success(request, 'Expense has been deleted')
        return redirect('index')


class SearchView(View):
    def post(self, request):
        search_str = json.loads(request.body).get('searchText')

        expenses = Expenses.objects.filter(amount__istartswith=search_str, owner=request.user) or Expenses.objects.filter(date__istartswith=search_str, owner=request.user) or Expenses.objects.filter(description__icontains=search_str, owner=request.user) or Expenses.objects.filter(category__icontains=search_str, owner=request.user)

        data = expenses.values()
        return JsonResponse(list(data), safe=False)
