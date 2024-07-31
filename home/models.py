from django.db import models
class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100) 
    info  = models.CharField(max_length = 100, default = '')
    price = models.IntegerField(blank=True, null=True)

class BeltAnalysis(models.Model):
    alert_status  = models.CharField(max_length = 100) 
    location  = models.CharField(max_length = 1000, default = '')
    reason  = models.CharField(max_length = 1000, default = '')
    measure  = models.CharField(max_length = 1000, default = '')
    uploaded_at = models.DateTimeField(auto_now_add=True)
