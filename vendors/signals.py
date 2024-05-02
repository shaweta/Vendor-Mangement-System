from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor
from django.db.models import Avg, Count, Q, F

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_metrics(sender, instance, **kwargs):
    vendor = instance.vendor
    update_vendor_on_time_delivery_rate(vendor)
    update_vendor_quality_rating_average(vendor)
    update_vendor_average_response_time(vendor)
    update_vendor_fulfillment_rate(vendor)

def update_vendor_on_time_delivery_rate(vendor):
    completed_pos = vendor.purchase_orders.filter(status='completed')
    on_time_deliveries = completed_pos.filter(delivery_date__gte=F('order_date')).count()
    if completed_pos.count() > 0:
        vendor.on_time_delivery_rate = (on_time_deliveries / completed_pos.count()) * 100
        vendor.save()

def update_vendor_quality_rating_average(vendor):
    completed_ratings = vendor.purchase_orders.filter(status='completed').exclude(quality_rating__isnull=True)
    average_rating = completed_ratings.aggregate(Avg('quality_rating'))['quality_rating__avg']
    vendor.quality_rating_avg = average_rating or 0.0
    vendor.save()

def update_vendor_average_response_time(vendor):
    acknowledged_pos = vendor.purchase_orders.exclude(acknowledgment_date__isnull=True)
    total_response_time = sum(
        (po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos
    )
    if acknowledged_pos.count() > 0:
        average_response_time_seconds = total_response_time / acknowledged_pos.count()
        vendor.average_response_time = average_response_time_seconds / 3600  # Convert to minutes
        vendor.save()

def update_vendor_fulfillment_rate(vendor):
    total_pos = vendor.purchase_orders.count()
    successful_pos = vendor.purchase_orders.filter(status='completed').count()
    if total_pos > 0:
        vendor.fulfillment_rate = (successful_pos / total_pos) * 100
        vendor.save()
