# your_app_name/views.py
from django.shortcuts import render,redirect
from.models import Vendor
from django.contrib.auth.decorators import login_required
from .metrice import (
    calculate_on_time_delivery_rate,
    calculate_quality_rating_average,
    calculate_average_response_time,
    calculate_fulfilment_rate,update_vendor_performance_metrics
)


# your_app_name/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'model/home.html')
@login_required()
def on_time_delivery_rate(request, vendor_id):
    on_time_delivery_rate = calculate_on_time_delivery_rate(vendor_id)
    vendor = Vendor.objects.get(vendor_id=vendor_id)
    return render(request, 'model/on_time_delivery_rate.html', {'vendor': vendor, 'on_time_delivery_rate': on_time_delivery_rate})
@login_required()
def quality_rating_average(request, vendor_id):
    quality_rating_average = calculate_quality_rating_average(vendor_id)
    vendor = Vendor.objects.get(vendor_id=vendor_id)
    return render(request, 'model/quality_rating_average.html', {'vendor': vendor, 'quality_rating_average': quality_rating_average})
@login_required()
def average_response_time(request, vendor_id):
    average_response_time = calculate_average_response_time(vendor_id)
    vendor = Vendor.objects.get(vendor_id=vendor_id)
    return render(request, 'model/average_response_time.html', {'vendor': vendor, 'average_response_time': average_response_time})
@login_required()
def fulfilment_rate(request, vendor_id):
    fulfilment_rate = calculate_fulfilment_rate(vendor_id)
    vendor = Vendor.objects.get(vendor_id=vendor_id)
    return render(request, 'model/fulfilment_rate.html', {'vendor': vendor, 'fulfilment_rate': fulfilment_rate})
@login_required()
def vendor_performance(request, vendor_id):
    vendor = Vendor.objects.get(vendor_id=vendor_id)
    update_vendor_performance_metrics(vendor)
    # Other view logic...
    return render(request, 'model/vendor_performance.html', {'vendor': vendor})

from django.http import HttpResponseRedirect
from .forms import SignUpForm

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'model/signup.html',{'form':form})
def logout_view(request):
    return render(request,'model/logout.html')




def redirect_to_vendor_urls(request):
    vendor_id = request.GET.get('vendor_id')

    if vendor_id:
        return redirect('on_time_delivery_rate', vendor_id=vendor_id)

def redirect_to_vendor_urls2(request):
    vendor_id = request.GET.get('vendor_id')

    if vendor_id:
        return redirect('quality_rating_average', vendor_id=vendor_id)

def redirect_to_vendor_urls3(request):
    vendor_id = request.GET.get('vendor_id')

    if vendor_id:
        return redirect('average_response_time', vendor_id=vendor_id)

def redirect_to_vendor_urls4(request):
    vendor_id = request.GET.get('vendor_id')

    if vendor_id:
        return redirect('fulfilment_rate', vendor_id=vendor_id)

def redirect_to_vendor_urls5(request):
    vendor_id = request.GET.get('vendor_id')

    if vendor_id:
        return redirect('vendor_performance', vendor_id=vendor_id)

    return render(request, 'home.html')
