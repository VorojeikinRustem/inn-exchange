from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView
from django.views.generic import FormView, TemplateView

from exchange.forms import ProfileForm

from exchange.models import Profile


class IndexView(TemplateView):
    template_name = 'exchange/exchange.html'


def make_exchange_great_again(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            print("form: " + str(form.cleaned_data))
            return redirect('exchange')
    else:
        form = ProfileForm()
    return render(request, 'exchange/exchange.html', {'form': form})


#
#
# class ExchangeView(FormView):
#     form_class = ProfileForm
#     template_name = "exchange/exchange.html"
#     success_url = "/"
#
#     # def post(self, request, *args, **kwargs):
#     #     resp = super().post(request, *args, **kwargs)
#     #     print("POST() METHOD")
#     #
#     #     return resp
#
#     def form_valid(self, form):
#         print("form_valid()")
#         return super().form_valid(form)
#
#     def get(self, request, *args, **kwargs):
#         resp = super().get(request, *args, **kwargs)
#         print("GET() METHOD")
#         return resp
#
