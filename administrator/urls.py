from django.urls import path
from administrator import views

#libraries/add
#libraries...list all libraries
urlpatterns=[
    path('libraries/add',views.library_create,name="addlibrary"),
    path('accounts/signup',views.signupview,name="signup"),
    path('accounts/signin',views.signinview,name="signin"),
    path('libraries',views.library_list,name="listlibrary"),
    path('libraries/change/<int:id>',views.library_update,name="changelibrary"),
    path('libraries/remove/<int:id>',views.library_remove,name="removelibrary"),
]