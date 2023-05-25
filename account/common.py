from account.models import *

def insert_on_receivedjournal(payment_id,date,desc,dr,cr,invoice_id,champion_id,account_id):
    Receivedjournal.objects.create(
        date=date,
        desc = desc,
        cr = cr,
        dr = dr,
        invoice_id=invoice_id,
        #champion_id=champion_id,
        payment_id=payment_id,
        account_id=account_id
    )

def insert_on_bankjournal(payment_id,date,desc,dr,cr,invoice,champion,account):
    Bankjournal.objects.create(
        date=date,
        desc = desc,
        cr = cr,
        dr = dr,
        invoice=invoice,
        #champion=champion,
        payment_id=payment_id,
        account_id=account
    )

def insert_on_expensejournal(payment_id,date,desc,dr,cr,invoice,champion,account_id):
    Expensejournal.objects.create(
        date=date,
        desc = desc,
        cr=cr,
        dr = dr,
        invoice=invoice,
        #champion=champion,
        payment_id=payment_id,
        account_id=account_id
    )

def insert_on_journal(payment_id,date,desc,dr,cr,invoice,champion,dr_account_id,cr_account_id):
    Journal.objects.create(
        date=date,
        desc = desc,
        cr = cr,
        #invoice=invoice,
        #champion=champion,
        payment_id=payment_id,
        account_id=cr_account_id
    )
    Journal.objects.create(
        date=date,
        desc=desc,
        dr=dr,
        #invoice=invoice,
        #champion=champion,
        payment_id=payment_id,
        account_id=dr_account_id
    )

def transact_account(type='cash'):
    if type =='bank':
        return Account.objects.filter(is_bankaccount=True).id
    else:
        return Account.objects.filter(is_cash=True).id

def delete_transaction(payment_id):
    Journal.objects.filter(payment_id=payment_id).delete()
    Expensejournal.objects.filter(payment_id=payment_id).delete()
    Bankjournal.objects.filter(payment_id=payment_id).delete()
    Receivedjournal.objects.filter(payment_id=payment_id).delete()
    Payment.objects.filter(id=payment_id).delete()