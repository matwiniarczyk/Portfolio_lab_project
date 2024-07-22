from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from myapp.models import Donation, Institution


class LandingPageView(View):
    def get(self, request):
        return render(request, 'base.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class IndexView(View):
    def get(self, request):
        bags = Donation.objects.aggregate(total_bags=Sum('quantity'))
        # aggregate zwraca słownik, klucze nazywają się 'total bags'
        total_bags = bags['total_bags']
        institutions = Donation.objects.values('institution').distinct()
        # values zwraca listę słowników klucz-wartość; tutaj klucz to institution
        total_institutions = institutions.count()
        return render(request, 'index.html', {'liczba_worków': total_bags, 'liczba_instytucji': total_institutions})

