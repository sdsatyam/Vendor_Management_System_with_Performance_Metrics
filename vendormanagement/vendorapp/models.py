from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=150)
    contact_details=models.TextField()
    address=models.TextField()
    vendor_code=models.CharField(max_length=150)
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()

    def __str__(self):
        return f"{self.name} (ID: {self.vendor_id})"

class PurchaseOrder(models.Model):
    po_number=models.CharField(max_length=150)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(max_length=150)
    quality_rating=models.FloatField()
    issue_date=models.DateTimeField()
    acknowledgment_date=models.DateTimeField()

    def __str__(self):
        return f"{self.po_number} - {self.vendor.name}"

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date=models.DateTimeField()
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()

