from django.shortcuts import render,redirect
from generalpublic import forms

# Create your views here.

#8000/generalpublic/libraries/reviews
def library_viewreviews(request):
    form = forms.GeneralPublicForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = forms.GeneralPublicForm(request.POST)
        if form.is_valid():
            library_name = form.cleaned_data["library_name"]

            print(library_name)
            return render(request, "library_reviews.html",context)

    return render(request, "library_reviews.html", context)


