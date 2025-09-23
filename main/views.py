from django.http import HttpResponse, JsonResponse, HttpResponseRedirect #HttpResponse untuk menampilkan teks biasa, JsonResponse untuk menampilkan data dalam format JSON, jsonrespone Otomatis set content_type="application/json".
from django.core import serializers
from main.forms import ProductForm
from .models import Product
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user) #mengambil semua data dari model Product

    context = {
        'npm' : '2406358094',
        'name': 'Alya Nabilla Khamil',
        'class': 'PBP B',
        'products_list': products_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username_login' : request.user.username
    }

    return render(request, "main.html", context)

def show_xml(request): 
    data = Product.objects.all() #mengambil semua data dari model Product
    data_xml = serializers.serialize("xml", data) #mengubah data menjadi format XML
    return HttpResponse(data_xml, content_type="application/xml") #mengembalikan data dalam format XML

def show_xml_by_id(request, product_id): 
    try:
        data = Product.objects.filter(pk=product_id) #mengambil 1 data dari model Product berdasarkan ID (primary key)
        data_xml = serializers.serialize("xml", data) #mengubah data menjadi format XML
        return HttpResponse(data_xml, content_type="application/xml") #mengembalikan data dalam format XML
    except Product.DoesNotExist: #jika data tidak ditemukan
        return HttpResponse("<h1>Data not found</h1>", content_type="text/html", status=404) #return pesan data tidak ditemukan dan memuat halaman lain

def show_json(request):
    data = Product.objects.all() #mengambil semua data dari model Product
    data_json = serializers.serialize("json", data) #mengubah data menjadi format JSON
    return HttpResponse(data_json, content_type="application/json") #mengembalikan data dalam format JSON

def show_json_by_id(request, product_id):
    try:
        data = Product.objects.get(pk=product_id) #mengambil 1 data dari model Product berdasarkan ID (primary key)
        data_json = serializers.serialize("json", [data]) #mengubah data menjadi format JSON, data harus dalam bentuk list
        return HttpResponse(data_json, content_type="application/json") #mengembalikan data dalam format JSON
    except Product.DoesNotExist: #jika data tidak ditemukan
        return JsonResponse({"error": "Data not found"}, status=404) #mengembalikan pesan data tidak ditemukan dalam format JSON

def add_product(request):
    form = ProductForm(request.POST or None) #jika request methodnya POST maka form akan diisi dengan data yang dikirimkan, jika tidak maka form akan kosong
    #Post: method pengiriman data yang digunakan untuk mengirimkan data ke server, data yang dikirimkan tidak akan terlihat di URL

    if form.is_valid() and request.method == "POST": # .is_valid() untuk mengecek apakah data yang dikirimkan valid atau tidak sesuai dengan yang ada di model
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')#redirect ke halaman utama setelah data berhasil disimpan

    context = {'form': form} #mengirimkan form ke template
    return render(request, "add_product.html", context) #render untuk menampilkan template create_news.html dengan context yang berisi form

@login_required(login_url='/login')
def show_product(request, product_id):
    product  = get_object_or_404(Product, pk=product_id) #mengambil 1 data dari model Product berdasarkan ID (primary key), jika data tidak ditemukan maka akan menampilkan halaman 404
    product.increment_views() #menambah jumlah view setiap kali halaman diakses
    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')