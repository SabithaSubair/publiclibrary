from django.urls import path
from generalpublic import views

#libraries
#libraries...list all libraries
urlpatterns=[
    path('libraries/reviews',views.library_viewreviews,name="viewreviews"),

]