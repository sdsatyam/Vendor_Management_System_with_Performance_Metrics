from django.urls import path,include
from .views import (
    VendorPerformanceView,VendorListCreateView, VendorRetrieveUpdateDestroyView,
    PurchaseOrderListCreateView, PurchaseOrderRetrieveUpdateDestroyView, AcknowledgePurchaseOrder)
from rest_framework.authtoken import views


urlpatterns = [
    path('api/vendors/<str:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:vendor_id>/', VendorRetrieveUpdateDestroyView.as_view(), name='vendor-retrieve-update-destroy'),
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:po_id>/', PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrder.as_view(), name='acknowledge-purchase-order'),
]
