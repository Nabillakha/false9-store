from django.urls import path
from main.views import show_main, show_xml, show_xml_by_id, show_json, show_json_by_id,add_product,show_product, register , login_user, logout_user, edit_product, delete_product, add_product_ajax, edit_product_ajax, register_ajax, login_ajax
 #import views yang sudah dibuat


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'), #menampilkan data dalam format XML berdasarkan ID
    path('xml/', show_xml, name='show_xml'), #menampilkan semua data dalam format XML
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'), #menampilkan data dalam format JSON berdasarkan ID
    path('json/', show_json, name='show_json'), #menampilkan semua data dalam format JSON
    path('add-product/', add_product, name='add_product'), #menambahkan data baru
    path('product/<str:product_id>/', show_product, name='show_product'), #menampilkan detail produk berdasarkan ID
    path('register/', register, name='register'), #menampilkan halaman register
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),   
    path('product/<uuid:id>/edit', edit_product, name='edit_product'), #menampilkan halaman edit news berdasarkan ID  ,
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path("category/<str:category>/", show_main, name="filter_category"),
    path('add-product-ajax', add_product_ajax, name='add_product_ajax'),
    path('product/<uuid:id>/edit/', edit_product_ajax, name='edit_product_ajax'),
    path('register/ajax/', register_ajax, name='register_ajax'),
    path('login/ajax/', login_ajax, name='login_ajax'),
    path('delete-product/<uuid:id>/', delete_product, name='delete_product'),

]