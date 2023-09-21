from django.db import models
from datetime import datetime

# Create your models here.

class Stock(models.Model):
    category = models.CharField( default= 0,max_length=50, blank=False, null=False)
    item_name = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.IntegerField(default=0, blank=False, null=False)
    price = models.FloatField(default=0, blank=False, null=False)
    order_date = models.DateField(default = datetime.now)
    receive_quantity = models.IntegerField(default=0, blank=False, null=False)
    receive_by = models.CharField(max_length=50, blank=False, null=False)
    issue_quantity = models.IntegerField(default=0, blank=False, null=False)
    issue_by = models.CharField(max_length=50, blank=False, null=False)
    issue_to = models.CharField(max_length=50, blank=False, null=False)
    phone_number= models.CharField(max_length=50, blank=False, null=False)
    created_by = models.CharField(max_length=50, default="Oche", null=False)
    reorder_level = models.IntegerField(default=0, blank=False, null=False)
    last_updated = models.DateTimeField(auto_now_add=True, null=False)
    export_to_CSV = models.BooleanField(default=True)
    
    
    #this will show the name of the item in the admin panel
    def __str__(self):       
        return self.item_name + ' ' + str(self.quantity)