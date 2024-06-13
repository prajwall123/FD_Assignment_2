from django.db import models
class Accounts(models.Model):
        firstname=models.CharField(max_length=50)
        lastname=models.CharField(max_length=50)
        aadhaar=models.BigIntegerField()
        phone=models.IntegerField()
        customer_id=models.PositiveIntegerField(unique=True)
        
        
        def save(self, *args, **kwargs):
            if not self.customer_id:
                last_customer=Accounts.objects.order_by('-customer_id').first()
                self.customer_id=8001 if not last_customer else last_customer.customer_id+1
            super().save(*args,**kwargs)
        
        def __str__(self):
            return f"{self.firstname} {self.lastname}"
 
       
class CustomerAccount(models.Model):
    ACCOUNT_TYPES = (
        ('SAVINGS', 'Savings Account'),
        ('LOAN', 'Loan Account'),
    )

    customer = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.customer.customer_id} - {self.account_type}"
# Create your models here.
