from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db.models import F

from exchange.forms import ProfileForm
from exchange.models import Profile


class IndexView(TemplateView):
    template_name = 'exchange/exchange.html'


def make_exchange_great_again(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            # get cleaned data
            user = form.cleaned_data['user']
            inn = form.cleaned_data['inn']
            price = form.cleaned_data['price']
            # reduce price of user
            profile = Profile.objects.get(user=user)
            profile.price -= price
            profile.save()
            # add price to selected users
            profiles_count = Profile.objects.filter(inn=inn).count()
            price_upd = price/profiles_count
            Profile.objects.filter(inn=inn).update(price=F("price") + price_upd)

            return redirect('exchange')
    else:
        form = ProfileForm()
    return render(request, 'exchange/exchange.html', {'form': form})
