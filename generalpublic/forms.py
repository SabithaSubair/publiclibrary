from django import forms

class GeneralPublicForm(forms.Form):

    library_name=forms.CharField()


    #validation
    def clean(self):
        print("validation")