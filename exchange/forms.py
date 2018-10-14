from django import forms
from django.contrib.auth.models import User

from exchange.models import Profile, Inn


users = Profile.objects.all().values_list("user__id", "user__username")


class ProfileForm(forms.Form):
    user = forms.ChoiceField(choices=users)
    inn = forms.IntegerField(widget=forms.NumberInput())
    price = forms.IntegerField(widget=forms.NumberInput())

    def clean_price(self):
        price = self.cleaned_data.get("price")
        user = self.cleaned_data.get("user")
        profile = Profile.objects.filter(user=user, price__gte=price)

        if not profile.exists():
            raise forms.ValidationError(
                "The user does not have so much money!"
            )
        return price


    def clean_user(self):
        username_id = self.cleaned_data.get("user")
        user = User.objects.filter(id=username_id)
        if not user.exists():
            raise forms.ValidationError(
                "User does not exist"
            )
        return user[0]

    def clean_inn(self):
        inn_number = self.cleaned_data.get("inn")

        inn = Inn.objects.filter(inn=inn_number).exists()

        if not inn:
            raise forms.ValidationError(
                "Inn does not exist"
            )

        return inn

