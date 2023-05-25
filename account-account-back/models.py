from django.db import models
from invoice.models import Invoice
from payment.models import User,Payment
###BASE MODELS
class BaseDB(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        abstract = True

###journal MODELS
class BaseJournal(BaseDB):
    date=models.DateField()
    desc=models.CharField(max_length=300,null=True)
    cr=models.FloatField(null=True,blank=True)
    dr = models.FloatField(null=True, blank=True)


    class Meta:
        abstract = True



# chart of account.
class Chartofaccount(models.Model):
    name=models.CharField(max_length=300)
    accountno=models.IntegerField(null=True)
    def __str__(self):
        return self.name

# chartcategory.
class Accountcategory(models.Model):
    name=models.CharField(max_length=300)
    accountno=models.CharField(max_length=200,null=True)
    chart=models.ForeignKey(Chartofaccount,on_delete=models.CASCADE,related_name='chartofaccount')
    def __str__(self):
        return self.name

# accounts.
class Account(models.Model):
    name=models.CharField(max_length=300)
    accountno=models.CharField(max_length=200,null=True)
    chart=models.ForeignKey(Chartofaccount,on_delete=models.CASCADE,null=True)
    accountcategory = models.ForeignKey(Accountcategory, on_delete=models.CASCADE)
    is_cashaccount=models.BooleanField(verbose_name='Is Cash Account',default=False)
    is_bankaccount=models.BooleanField(verbose_name='Is Bank Account',default=False)

    def __str__(self):
        return self.name


# received accounts.
class Receivedjournal(BaseJournal):
    invoice = models.ForeignKey(Invoice, verbose_name="invoice husika", on_delete=models.CASCADE,related_name='rcv_invpoice')
    champion = models.ForeignKey(User, verbose_name="Champion", on_delete=models.CASCADE,related_name='rcv_champion')
    payment = models.ForeignKey(Payment, verbose_name="Payment", on_delete=models.CASCADE,related_name='rcv_payment')
    account = models.ForeignKey(Account, verbose_name="Account", on_delete=models.CASCADE, related_name='account_payment',null=True)
    def __str__(self):
        self.desc + ' CR: ' + str(self.cr) + '  DR: ' + str(self.dr)

# bank accounts.
class Bankjournal(BaseJournal):
    invoice = models.ForeignKey(Invoice, verbose_name="invoice husika", on_delete=models.CASCADE,
                                related_name='bank_invpoice')
    champion = models.ForeignKey(User, verbose_name="Champion", on_delete=models.CASCADE,
                                 related_name='bank_champion')
    payment = models.ForeignKey(Payment, verbose_name="Payment", on_delete=models.CASCADE, related_name='bank_payment')
    account = models.ForeignKey(Account, verbose_name="Account", on_delete=models.CASCADE,
                                related_name='bank2journal',null=True)
    def __str__(self):
        self.desc + ' CR: ' + str(self.cr) + '  DR: ' + str(self.dr)

# expenses accounts.
class Expensejournal(BaseJournal):
    invoice = models.ForeignKey(Invoice, verbose_name="invoice husika", on_delete=models.CASCADE,
                                related_name='ex_invpoice')
    champion = models.ForeignKey(User, verbose_name="Champion", on_delete=models.CASCADE,
                                 related_name='ex_champion')
    payment = models.ForeignKey(Payment, verbose_name="Payment", on_delete=models.CASCADE, related_name='ex_payment')
    account = models.ForeignKey(Account, verbose_name="Account", on_delete=models.CASCADE,
                                related_name='account2journal',null=True)
    def __str__(self):
        self.desc + ' CR: ' + str(self.cr) + '  DR: ' + str(self.dr)

# expenses accounts.
class Journal(BaseJournal):
    invoice = models.ForeignKey(Invoice, verbose_name="invoice husika", on_delete=models.CASCADE,
                                related_name='jn_invpoice')
    champion = models.ForeignKey(User, verbose_name="Champion", on_delete=models.CASCADE,
                                 related_name='jn_champion')
    payment = models.ForeignKey(Payment, verbose_name="Payment", on_delete=models.CASCADE, related_name='jn_payment')

    account = models.ForeignKey(Account, verbose_name="Account", on_delete=models.CASCADE,
                                related_name='journal',null=True)

    def __str__(self):
        self.desc + ' CR: ' + str(self.cr) + '  DR: ' + str(self.dr)

# chartcategory.
class Withdraw(models.Model):
    cr_account=models.ForeignKey(Payment, verbose_name="Cr account", on_delete=models.CASCADE, related_name='acc06')

    dr_account=models.ForeignKey(Account, verbose_name="Dr Account", on_delete=models.CASCADE, related_name='accr')

    desc=models.TextField()
    amount=models.FloatField()
    date=models.DateField()
    created_at= models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.desc