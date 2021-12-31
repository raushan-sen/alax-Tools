
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home),
    path('mcq',views.mcq),
    path('uploads',views.uploads),
    path('admin/', admin.site.urls),
]
