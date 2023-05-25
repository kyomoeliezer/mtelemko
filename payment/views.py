from django.shortcuts import render
from payment.models import Payment
# Create your views here.
def create_payment(amount,desc,date,user,type1,trans_account_dr_id,trans_account_cr_id):
    return Payment.objects.create(
        created_by=user,
        amount=amount,
        desc=desc,
        type=type1,
        trans_account_cr_id=trans_account_cr_id,
        trans_account_dr_id=trans_account_dr_id,
        date=date
    )



