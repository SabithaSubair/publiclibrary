from django import forms

class LibraryForm(forms.Form):

    library_name=forms.CharField()
    address=forms.CharField()
    city=forms.CharField()

    #validation
    def clean(self):
        print("validation")
class RegistrationForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    address=forms.CharField()
    username=forms.CharField()
    password=forms.CharField()
    email=forms.CharField()
    mobile=forms.IntegerField()

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class LibraryEditForm(forms.Form):
    library_name = forms.CharField()
    address = forms.CharField()
    city = forms.CharField()

class LibrarySearchForm(forms.Form):
    library_name = forms.CharField()

class LibraryDeleteForm(forms.Form):
    library_name = forms.CharField()




