from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path
from core.views import *

#! links the urls together

urlpatterns = [     
    path('admin/', admin.site.urls),
    path('home/', ReactView.as_view(), name="something"),
]
