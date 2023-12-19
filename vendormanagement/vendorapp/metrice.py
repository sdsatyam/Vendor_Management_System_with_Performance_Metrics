# metrics.py
from django.shortcuts import render
from django.db.models import Count, Avg, F, ExpressionWrapper, fields
from django.db.models.functions import Coalesce
from .models import PurchaseOrder, Vendor, HistoricalPerformance



def calculate_on_time_delivery_rate(vendor_id):
    completed_pos = PurchaseOrder.objects.filter(vendor_id=vendor_id, status='completed',
                                                 delivery_date__lte=F('delivery_date'))
    total_completed_pos = completed_pos.count()
    if total_completed_pos == 0:
        return 0
    on_time_deliveries = completed_pos.filter(delivery_date__lte=F('delivery_date'))
    on_time_delivery_rate = on_time_deliveries.count() / total_completed_pos
    return on_time_delivery_rate


def calculate_quality_rating_average(vendor_id):
    completed_pos = PurchaseOrder.objects.filter(vendor_id=vendor_id, quality_rating__isnull=False)
    if not completed_pos.exists():
        return None
    quality_rating_average = completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg']
    return quality_rating_average



def calculate_average_response_time(vendor_id):
    acknowledged_pos = PurchaseOrder.objects.filter(vendor_id=vendor_id, acknowledgment_date__isnull=False)

    if not acknowledged_pos.exists():
        return None

    response_times = acknowledged_pos.annotate(
        response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'),
                                        output_field=fields.DurationField()))
    average_response_time = response_times.aggregate(Avg('response_time'))['response_time__avg']

    return average_response_time.total_seconds() / 3600  # Convert to hours



def calculate_fulfilment_rate(vendor_id):
    all_pos = PurchaseOrder.objects.filter(vendor_id=vendor_id)
    successful_fulfillments = all_pos.filter(status='completed', issue_date__isnull=True)

    total_pos = all_pos.count()
    if total_pos == 0:
        return 0

    fulfilment_rate = successful_fulfillments.count() / total_pos

    return fulfilment_rate

def update_vendor_performance_metrics(vendor):

    if not isinstance(vendor, Vendor):
        # Handle the case where 'vendor' is not an instance of Vendor
        return
    vendor_id = vendor.vendor_id
    # Calculate and update performance metrics
    Vendor.on_time_delivery_rate = calculate_on_time_delivery_rate(vendor_id)
    Vendor.quality_rating = calculate_quality_rating_average(vendor_id)
    Vendor.response_time = calculate_average_response_time(vendor_id)
    Vendor.fulfillment_rate = calculate_fulfilment_rate(vendor_id)

    # Save the updated metrics to the vendor model
    vendor.save()