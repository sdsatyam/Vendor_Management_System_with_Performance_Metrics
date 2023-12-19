# serializers.py
from rest_framework import serializers
from vendorapp.models import Vendor,PurchaseOrder


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_id', 'vendor_code', 'name', 'contact_details', 'address']
        read_only_fields = ['id']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['vendor_id', 'po_number', 'vendor', 'order_date', 'items', 'quantity', 'status']
        read_only_fields = ['id']


class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_id', 'on_time_delivery_rate', 'quality_rating', 'response_time', 'fulfillment_rate']


