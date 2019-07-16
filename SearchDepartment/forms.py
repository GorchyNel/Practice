from django import forms


class SearchForm(forms.Form):
    RequestNumber = forms.IntegerField(label="Номер заявки:", min_value=0, max_value=2147483647, widget=
    forms.NumberInput(attrs={"class": "form-control", "placeholder": "Номер заявки"}))
