# your_app_name/urls.py
from django.urls import path,include
from .views import (
    on_time_delivery_rate,
    quality_rating_average,
    average_response_time,
    fulfilment_rate,home,vendor_performance,logout_view,signup_view,redirect_to_vendor_urls,redirect_to_vendor_urls2,redirect_to_vendor_urls3,redirect_to_vendor_urls4,redirect_to_vendor_urls5,
)

urlpatterns = [
    path('on_time_delivery_rate/<int:vendor_id>/', on_time_delivery_rate, name='on_time_delivery_rate'),
    path('quality_rating_average/<int:vendor_id>/', quality_rating_average, name='quality_rating_average'),
    path('average_response_time/<int:vendor_id>/', average_response_time, name='average_response_time'),
    path('fulfilment_rate/<int:vendor_id>/', fulfilment_rate, name='fulfilment_rate'),
    path('vendor_performance/<int:vendor_id>/',vendor_performance,name='vendor_performance'),
    path('home/', home, name='home'),
    path('', redirect_to_vendor_urls, name='redirect_to_vendor_urls'),
    path('1', redirect_to_vendor_urls2, name='redirect_to_vendor_urls2'),
    path('2', redirect_to_vendor_urls3, name='redirect_to_vendor_urls3'),
    path('3', redirect_to_vendor_urls4, name='redirect_to_vendor_urls4'),
    path('4', redirect_to_vendor_urls5, name='redirect_to_vendor_urls5'),

]
