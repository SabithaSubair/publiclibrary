from django.shortcuts import render,redirect
from administrator import forms

# Create your views here.
def signupview(request):
    form=forms.RegistrationForm()
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("signin")
    return render(request, "register.html",context)

def signinview(request):
    form = forms.LoginForm()
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("addlibrary")

    return render(request, "signin.html", context)

#8000/administrator/librariess/add
def library_create(request):
    form=forms.LibraryForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.LibraryForm(request.POST)
        if form.is_valid():
            library_name=form.cleaned_data["library_name"]
            address=form.cleaned_data["address"]
            city=form.cleaned_data["city"]
            print(library_name,address,city)
            return render(request, "library_add.html")


    return render(request,"library_add.html",context)


#8000/administrator/libraries
def library_list(request):
    return render(request,"library_list.html")

#8000/administrator/libraries/change/{id}
def library_update(request,id):
    return render(request,"library_edit.html")

#8000/administrator/libraries/remove/{id}
def library_remove(request,id):
    return render(request,"library_remove.html")


