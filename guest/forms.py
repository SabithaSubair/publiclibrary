from django import forms

class GuestForm(forms.Form):
    guest_name=forms.CharField()
    library_name=forms.CharField()
    review=forms.CharField()

    #validation
    def clean(self):
        print("validation")