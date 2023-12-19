"""
URL configuration for vendormanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from vendorapp.views import home,logout_view,signup_view
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendorapp/', include('vendorapp.urls')),
    path('api/', include('vendorapp.Api.urls')),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/',logout_view,),
    path('signup/', signup_view),
    path('get-api-token/',views.obtain_auth_token,name='get-api-token')
    # Add other app URLs as needed...
]

