from django import forms

class todo_form(forms.Form):
    text = forms.CharField(label='', required=True)

    text.widget.attrs.update({
            "class": "form-control mb-2 mr-sm-2",
            "placeholder": "What would you like to do today?",
            "name": "new_todo",
    })

     