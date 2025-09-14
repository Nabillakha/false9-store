from django.http import HttpResponse, JsonResponse #HttpResponse untuk menampilkan teks biasa, JsonResponse untuk menampilkan data dalam format JSON, jsonrespone Otomatis set content_type="application/json".
from django.core import serializers
from .models import Product
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406358094',
        'name': 'Alya Nabilla Khamil',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

def show_xml(request): 
    data = Product.objects.all() #mengambil semua data dari model Product
    data_xml = serializers.serialize("xml", data) #mengubah data menjadi format XML
    return HttpResponse(data_xml, content_type="application/xml") #mengembalikan data dalam format XML

def show_xml_by_id(request, product_id): 
    try:
        data = Product.objects.get(pk=product_id) #mengambil 1 data dari model Product berdasarkan ID (primary key)
        data_xml = serializers.serialize("xml", data) #mengubah data menjadi format XML
        return HttpResponse(data_xml, content_type="application/xml") #mengembalikan data dalam format XML
    except ValueError: #jika product_id bukan integer
        return HttpResponse("<h1>Invalid ID</h1>", content_type="text/html", status=400) #mengembalikan pesan ID tidak valid dan memuat halaman lain
    except data.DoesNotExist: #jika data tidak ditemukan
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
    except ValueError: #jika product_id bukan integer
        return JsonResponse({"error": "Invalid ID"}, status=400) #mengembalikan pesan ID tidak valid dalam format JSON 
    except data.DoesNotExist: #jika data tidak ditemukan
        return JsonResponse({"error": "Data not found"}, status=404) #mengembalikan pesan data tidak ditemukan dalam format JSON
