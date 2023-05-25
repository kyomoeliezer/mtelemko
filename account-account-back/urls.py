from django.conf.urls import url,re_path
from account.views import *

urlpatterns= [
    url(r'^new-expense/$',RegisterExpense.as_view(),name="new_expense"),
    url(r'^expenses$',ExpenseList.as_view(),name="expenses"),
    url(r'^expensesgroups$',ExpenseInGroups.as_view(),name="expense_by_acc_category"),

    url(r'^payment/(?P<pk>[0-9]+)/delete$', DeleteTransaction.as_view(),name='delete_payment'),

    ###CHARTS
    url(r'^chartofaccounts$', ChartsList.as_view(),name='charts'),
    url(r'^new-chart$', CreateChart.as_view(),name='new_chart'),
    url(r'^chart/(?P<pk>[0-9]+)/update$', UpdateChartofAccount.as_view(),name='update_chart'),
    url(r'^chart/(?P<pk>[0-9]+)/delete$', ChartofaccountDelete.as_view(),name='delete_chart'),

    ###Account categories
    url(r'^account-categories', AccountcategoryList.as_view(),name='accountcategories'),
    url(r'^new-category', CreateAccountcategory.as_view(),name='new_acc_categoty'),
    url(r'^category/(?P<pk>[0-9]+)/update$', UpdateAccountcategory.as_view(),name='update_acc_categoty'),
    url(r'^category/(?P<pk>[0-9]+)/delete$', CategoryaccountDelete.as_view(),name='delete_acc_categoty'),

    ####ACCOUNTS
    url(r'^accounts', AccountList.as_view(),name='accounts'),
    url(r'^newaccount', CreateAccount.as_view(),name='new_account'),
    url(r'^account/(?P<pk>[0-9]+)/update$', UpdateAccount.as_view(),name='update_account'),
    url(r'^account/(?P<pk>[0-9]+)/delete$', AccountDelete.as_view(),name='delete_account'),

]

