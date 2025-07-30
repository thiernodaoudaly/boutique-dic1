from django.shortcuts import render
from store.models import Product

# Create your views here.

def home(request):
    products = Product.objects.all().filter(is_available = True)

    context = {
        'products':products,
    }
    return render (request, 'store/store.html',context)

def ValidationView(request):
    return render(request, 'validation.html')

def ProfilView(request):
    return render(request, 'profil-utilisateur.html')

def SettingProfilView(request):
    return render(request, 'profil-parametres.html')