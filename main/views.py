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
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
@login_required(login_url='/login')
def show_main(request, category=None):
    
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if category:
        products_list = Product.objects.filter(category=category)
    elif filter_type == "all":
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406358094',
        'name': 'Alya Nabilla Khamil',
        'class': 'PBP B',
        'products_list': products_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username_login' : request.user.username,
        "categories": Product.CATEGORY_CHOICES,
        "selected_category": category,
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
    products_list = Product.objects.all() 
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'stock' : product.stock,
            'sold' : product.sold,
            'price' : product.price,
            'view': product.view,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in products_list
    ]
    return JsonResponse(data, safe=False) 

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id) #mengambil 1 data dari model Product berdasarkan ID (primary key)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'stock' : product.stock,
            'sold' : product.sold,
            'price' : product.price,
            'view': product.view,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)#mengembalikan data dalam format JSON
    except Product.DoesNotExist: #jika data tidak ditemukan
        return JsonResponse({'detail': 'Not found'}, status=404)#mengembalikan pesan data tidak ditemukan dalam format JSON

def add_product(request):
    form = ProductForm(request.POST or None) #jika request methodnya POST maka form akan diisi dengan data yang dikirimkan, jika tidak maka form akan kosong
    #Post: method pengiriman data yang digunakan untuk mengirimkan data ke server, data yang dikirimkan tidak akan terlihat di URL

    if form.is_valid() and request.method == "POST": # .is_valid() untuk mengecek apakah data yang dikirimkan valid atau tidak sesuai dengan yang ada di model
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')#redirect ke halaman utama setelah data berhasil disimpan

    context = {'form': form} #mengirimkan form ke template
    return render(request, "add_product.html", context) #render untuk menampilkan template add_product.html dengan context yang berisi form

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
    return redirect('/login?logout=1')

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

@login_required
@csrf_exempt
def delete_product(request, id):
    if request.method == "POST":
        try:
            product = Product.objects.get(id=id, user=request.user)
            product.delete()
            return JsonResponse({'status': 'success'})
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Produk tidak ditemukan.'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'}, status=400)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    price = request.POST.get("price")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    stock = request.POST.get("stock")
    user = request.user 

    # Buat objek baru
    new_product = Product(
        name=name,
        description=description,
        price=price,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        stock=stock if stock else 0,
        user=user
    )

    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    """Edit product via AJAX request"""
    product = get_object_or_404(Product, pk=id)

    # Ambil data dari form AJAX
    name = request.POST.get("name")
    description = request.POST.get("description")
    price = request.POST.get("price")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    stock = request.POST.get("stock")
    sold = request.POST.get("sold")
    view = request.POST.get("view")

    # Update field yang diubah
    product.name = name
    product.description = description
    product.price = price
    product.category = category
    product.thumbnail = thumbnail
    product.is_featured = is_featured
    product.stock = stock if stock else 0
    product.sold = sold if sold else product.sold
    product.view = view if view else product.view

    product.save()

    return JsonResponse({
        "status": "success",
        "message": "Product updated successfully!",
        "id": product.id
    }, status=200)


@csrf_exempt
def register_ajax(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            # Kirim pesan error form (contoh: username sudah ada)
            error_message = next(iter(form.errors.values()))[0]
            return JsonResponse({"success": False, "error": error_message})
    return JsonResponse({"success": False, "error": "Invalid request method."})


@csrf_exempt
def login_ajax(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({"success": True})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            error_message = "Invalid username or password."
            return JsonResponse({"success": False, "error": error_message})
    return JsonResponse({"success": False, "error": "Invalid request method."})