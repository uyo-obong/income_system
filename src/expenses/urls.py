from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import index, ExpensesView, ExpenseUpdateView, ExpenseDeleteView, SearchView

urlpatterns = [
    path('', index, name="index"),
    path('add/expense', ExpensesView.as_view(), name="add_expenses"),
    path('update/expense/<int:user_id>', ExpenseUpdateView.as_view(), name="update_expenses"),
    path('delete/expense/<int:user_id>', ExpenseDeleteView.as_view(), name="delete_expenses"),
    path('expense/search', csrf_exempt(SearchView.as_view()), name="search_expenses")
]
