from .models import Friend
from django import forms
import datetime

class FriendForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FriendForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Friend
        fields = ("__all__")
        widgets = {'exam': forms.HiddenInput(), 'slate_id': forms.HiddenInput()} # still having the form in the html template but not showing a textarea
        labels = {'exam': '', 'slate_id': ''} # label of these models is nothing so it isn't shown

 
class ExamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FriendForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Friend
        fields = ("slate_id", "exam")
        # widgets = {'exam': forms.HiddenInput(), 'slate_id': forms.HiddenInput()} # still having the form in the html template but not showing a textarea
        # labels = {'exam': '', 'slate_id': ''} # label of these models is nothing so it isn't shown

        