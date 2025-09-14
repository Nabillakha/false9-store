from django.urls import path
from main.views import show_main, show_xml, show_xml_by_id, show_json, show_json_by_id #import views yang sudah dibuat

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'), #menampilkan data dalam format XML berdasarkan ID
    path('xml/', show_xml, name='show_xml'), #menampilkan semua data dalam format XML
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'), #menampilkan data dalam format JSON berdasarkan ID
    path('json/', show_json, name='show_json'), #menampilkan semua data dalam format JSON
]