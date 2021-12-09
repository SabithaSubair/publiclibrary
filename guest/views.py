
from django.shortcuts import render,redirect
from guest import forms

# Create your views here.


#8000/guest/libraries/review
def library_addreview(request):
    form=forms.GuestForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.GuestForm(request.POST)
        if form.is_valid():
            guest_name=form.cleaned_data["guest_name"]
            library_name=form.cleaned_data["library_name"]
            review=form.cleaned_data["review"]
            print(guest_name,library_name,review)
            return render(request, "review.html")


    return render(request,"review.html",context)
