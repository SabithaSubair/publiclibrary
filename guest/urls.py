from django.urls import path
from guest import views

urlpatterns=[
    path('libraries/review',views.library_addreview,name="addreview"),

]