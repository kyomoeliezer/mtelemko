from django.db import models
from user.models import User

class Payment(models.Model):
    """TYPE+1-Expense, 2-Account Transfer, 3-Sales,4-other receivings"""
    desc=models.CharField(max_length=300,verbose_name='Paymant narration')
    amount=models.FloatField()
    date=models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type=models.IntegerField(null=True,verbose_name="TYPE+1-Expense, 2-Account Transfer, 3-Sales,4-other receivings")
    created_by = models.ForeignKey(User, verbose_name="Created by", on_delete=models.CASCADE,related_name='useerpayment',null=True)
    trans_account_cr_id=models.IntegerField(null=True)
    trans_account_dr_id = models.IntegerField(null=True)

    def __str__(self):
        self.desc
