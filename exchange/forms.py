from django import forms
from exchange.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'inn', 'price']
        widgets = {
            # 'from_age': forms.Select(choices=[(i, str(i)) for i in AGE_FROM]),
            # 'to': forms.Select(choices=[(i, str(i)) for i in AGE_TO])
            'inn': forms.NumberInput()
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['user'].required = False
