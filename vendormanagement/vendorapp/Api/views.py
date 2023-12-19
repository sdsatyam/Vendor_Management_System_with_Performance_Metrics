# views.py
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,RetrieveAPIView
from vendorapp.models import Vendor,PurchaseOrder
from .serializers import VendorPerformanceSerializer,VendorSerializer,PurchaseOrderSerializer
from vendorapp.metrice import update_vendor_performance_metrics


class VendorPerformanceView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(vendor_id=vendor_id)
            update_vendor_performance_metrics(vendor)
            serializer = VendorPerformanceSerializer(vendor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)


class VendorListCreateView(ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_url_kwarg = 'vendor_id'


class PurchaseOrderListCreateView(ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = 'po_id'


class VendorPerformanceView(RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_url_kwarg = 'vendor_id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        update_vendor_performance_metrics(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AcknowledgePurchaseOrder(APIView):
    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
            purchase_order.acknowledgment_date = timezone.now()  # assuming acknowledgment_date is a DateTimeField
            purchase_order.save()

            # Recalculate average_response_time for the vendor
            update_vendor_performance_metrics(purchase_order.vendor)

            return Response({'success': 'Purchase order acknowledged successfully.'}, status=status.HTTP_200_OK)
        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'Purchase order not found.'}, status=status.HTTP_404_NOT_FOUND)