# README — Django Project: `false9-store` 

**Pemilik / Pembuat:** Alya Nabilla Khamil (Nabillakha)

## Link Aplikasi (PWS)

> Aplikasi yang sudah berhasil di-deploy dapat diakses melalui tautan berikut: **\https://alya-nabilla-false9store.pbp.cs.ui.ac.id/**

---

## Ringkasan singkat

Proyek ini merupakan tugas dari mata kuliah Pemrograman Berbasis Platform (PBP). Aplikasi yang dikembangkan bernama False9 Store, yaitu sebuah aplikasi Football Shop sederhana berbasis Django yang saat ini masih dalam tahap pengembangan.

## Implementasi proyek step-by-step

1. **Membuat proyek Django baru**

   1. **Membuat Direktori & Virtual Environment**  
      Pertama, saya membuat direktori baru khusus untuk proyek ini agar terpisah dari repositori sebelumnya. Lalu membuat virtual environment serta mengaktifkannya. Virtual environment penting untuk mengisolasi dependencies proyek ini dari proyek Python lain di komputer. Jadi kalau ada perbedaan versi library, tidak akan saling mengganggu.

      *Membuat folder baru dan masuk ke dalamnya:*
      ```bash
      cd ~
      mkdir false9-store
      cd false9-store
      ```

      *Membuat virtual environment untuk isolasi dependencies:*
      ```bash
      python -m venv env
      ```

      *Mengaktifkan virtual environment:*
      ```bash
      env\Scripts\activate
      ```

   2. **Menambahkan Dependencies**  
      Saya membuat file `requirements.txt` berisi daftar dependencies utama:
      ```text
      django
      gunicorn
      whitenoise
      psycopg2-binary
      requests
      urllib3
      python-dotenv
      ```
      Masing-masing library punya fungsinya sendiri: Django sebagai framework inti, gunicorn sebagai web server untuk production, whitenoise untuk mengatur file statis, psycopg2-binary sebagai driver PostgreSQL, requests dan urllib3 untuk kebutuhan HTTP request, serta python-dotenv agar proyek bisa membaca environment variables dari file `.env`.

      Instalasi dilakukan dengan:
      ```bash
      pip install -r requirements.txt
      ```

   3. **Inisiasi Proyek Django**  
      Saya membuat proyek Django bernama `false9_store` dengan:
      ```bash
      django-admin startproject false9_store .
      ```
      Titik di akhir perintah berguna supaya struktur file langsung dibuat di root folder, sehingga file `manage.py` tidak berada di dalam subdirektori tambahan. Inisiasi ini menghasilkan file penting seperti `settings.py`, `urls.py`, dan konfigurasi dasar Django.

   4. **Konfigurasi Environment Variables**  
      Untuk memisahkan pengaturan development dan production, saya menambahkan dua file environment:
      - `.env` → untuk development lokal (SQLite).  
      - `.env.prod` → untuk production (PostgreSQL di server PWS).  

      File `.env` berisi `PRODUCTION=False`, sedangkan `.env.prod` berisi kredensial PostgreSQL dari PWS dengan `PRODUCTION=True`. Dengan pemisahan ini, saya tidak perlu mengubah kode setiap kali berpindah environment, cukup mengganti file environment yang dipakai.

   5. **Konfigurasi Settings Django**  
      Saya memodifikasi `settings.py` supaya bisa membaca konfigurasi dari file `.env` menggunakan python-dotenv.  
      Selain itu:  
      - Menambahkan `ALLOWED_HOSTS` agar proyek hanya bisa diakses dari host tertentu (misalnya `localhost` dan `127.0.0.1`).  
      - Menambahkan variabel `PRODUCTION` untuk menentukan apakah Django akan menggunakan SQLite (development) atau PostgreSQL (production).  

   6. **Migrasi Database & Menjalankan Server**  
      Setelah konfigurasi selesai, saya melakukan migrasi awal dengan:
      ```bash
      python manage.py migrate
      ```
      Proses ini membuat struktur database bawaan Django seperti tabel user, autentikasi, dan session.  
      Lalu menjalankan server lokal dengan:
      ```bash
      python manage.py runserver
      ```
      Jika membuka `http://localhost:8000` muncul tampilan default Django, artinya proyek berhasil dibuat.

   7. **Menghentikan Server & Menonaktifkan Virtual Environment**  
      Untuk menghentikan server cukup tekan `Ctrl + C` di terminal, lalu menonaktifkan virtual environment dengan:
      ```bash
      deactivate
      ```

   8. **Membuat Repositori GitHub**  
      - Membuat repositori baru bernama `false9-store` dengan visibilitas public.  
      - Inisialisasi repositori lokal dengan:
        ```bash
        git init
        ```

   9. **Menambahkan .gitignore**  
      Membuat file `.gitignore` untuk mengabaikan file yang tidak perlu, seperti `db.sqlite3`, file log, virtual environment, dan file konfigurasi editor.

   10. **Menghubungkan ke GitHub**  
       - Menambahkan remote ke GitHub:
         ```bash
         git remote add origin <url-repo>
         ```
       - Membuat branch utama `master`.  
       - Menambahkan file, commit, lalu push ke GitHub.

   11. **Deployment ke PWS**  
       - Login ke PWS menggunakan akun SSO UI.  
       - Membuat proyek baru bernama `false9store`.  
       - Menyimpan Project Credentials dan menjalankan Project Command.

   12. **Menambahkan Environment Variables**  
       - Menyalin isi `.env.prod` ke tab *Environs* di PWS.  
       - Memastikan `PRODUCTION=True` dan `SCHEMA=tugas_individu`.

   13. **Menyesuaikan settings.py**  
       Menambahkan URL PWS ke dalam `ALLOWED_HOSTS`.

   14. **Push ke PWS**  
       - Melakukan `git add`, `git commit`, dan:
         ```bash
         git push pws master
         ```
       - Mengecek status deployment hingga `Running` agar aplikasi bisa diakses melalui URL PWS.

2. **Membuat aplikasi `main`**

   * `python manage.py startapp main`. Direktori baru akan dengan nama `main` akan terbentuk
   * Menambahkan `'main'` ke `INSTALLED_APPS` pada `settings.py` agar Django mengenali app.

3. **Routing**

   Dibuat file `urls.py` di dalam aplikasi main untuk memetakan fungsi view yang sudah ada. Kemudian, di `urls.py` proyek, routing ditambahkan dengan `include('main.urls')` agar aplikasi main bisa diakses dari URL utama.

4. **Mendesain model `Product`**

   * Di `main/models.py` dibuat class `Product(models.Model)` dengan field sesuai checklist.

5. **Membuat fungsi view sederhana**

    Di `views.py`, ditambahkan fungsi `show_main` yang mengirimkan data (seperti nama aplikasi, nama, dan kelas) ke template HTML. Data ini ditampilkan dengan menggunakan variabel konteks di template.

6. **Migrasi database lokal**

   * `python manage.py makemigrations main`
   * `python manage.py migrate`
   * Saya juga membuat migration terpisah setiap kali mengubah model agar histori perubahan jelas.

7. **Routing fungsi view ke `urls.py` aplikasi**

    Fungsi `show_main` tadi dihubungkan melalui urls.py aplikasi main, sehingga ketika URL tertentu diakses, template yang sudah dibuat bisa muncul di browser.

8. **Deployment ke PWS dan push ke GitHub**

   Setelah aplikasi berjalan secara lokal, proyek dihubungkan ke PWS (Pacil Web Service) dengan membuat proyek baru di dashboard PWS, menambahkan environment variables, mengatur `ALLOWED_HOSTS`, lalu melakukan `git push pws master`. Setelah status deployment berubah menjadi Running, maka aplikasi bisa diakses melalui URL PWS. Dan juga untuk push semua ke GitHub


## Bagan request-response dan keterkaitan berkas (urls.py, views.py, models.py, HTML)

```scss
    [Client / Browser]
        │
        ▼
   Mengirim Request
        │
        ▼
  urls.py (Routing)
        │
        ▼
  views.py (Logic)
        │
        ▼
 models.py (Database)  ←→  Database (SQLite/PostgreSQL)
        │
        ▼
   Template HTML (Rendering)
        │
        ▼
 [Response kembali ke Client]
```

**Penjelasan singkat:**

* `urls.py` berfungsi sebagai peta jalan. Request yang masuk akan diarahkan ke fungsi tertentu di `views.py`
* `views.py` berisi logika untuk memproses request, bisa mengambil/memanipulasi data dari models.py.`models.py` .
* `models.py` menjadi representasi tabel database. Jika view butuh data, ia akan mengambil lewat model.
* Setelah data siap, view akan memanggil template HTML. Template ini digunakan untuk menampilkan data dalam bentuk halaman web.
* Hasil akhirnya berupa response HTML yang dikirim balik ke browser client.

## Peran `settings.py` dalam proyek Django

`settings.py` adalah pusat konfigurasi proyek Django. Beberapa peran dan konfigurasi penting:

* `INSTALLED_APPS`: daftar app yang aktif dalam proyek — harus berisi `'main'` agar model dan admin-nya terdeteksi.
* `DATABASES`: konfigurasi koneksi database (default: SQLite untuk development).
* `ALLOWED_HOSTS`: domain atau host yang diizinkan mengakses aplikasi (penting untuk produksi).
* `DEBUG`: mode debug (harus `False` di produksi).
* `SECRET_KEY`: kunci rahasia proyek (jangan di-commit ke publik).
* `TEMPLATES`: lokasi dan pengaturan engine template.
* `STATIC_URL`, `STATIC_ROOT`: pengaturan file statis untuk collectstatic di produksi.
* `MIDDLEWARE`, `ROOT_URLCONF`, `WSGI_APPLICATION` dan pengaturan lain yang mengontrol lifecycle request, keamanan, dan integrasi eksternal.

     `settings.py` mengatur bagaimana aplikasi berperilaku (database, app, file statis, host, middleware, dll.).Tanpa `settings.py`, proyek Django tidak bisa tahu bagaimana cara berjalan di environment tertentu.

## Cara kerja migrasi database di Django

Migrasi di Django adalah cara untuk menyamakan kode model Python dengan struktur database:

1. Saat menulis/ubah model di `models.py`, Django belum langsung mengubah database.  
2. Dengan perintah `python manage.py makemigrations`, Django membuat file migrasi (seperti “catatan perubahan”).  
3. Dengan `python manage.py migrate`, Django mengeksekusi file migrasi itu untuk membuat atau mengubah tabel di database.  
4. Proses ini bisa dilakukan berkali-kali sesuai perubahan model, jadi database selalu sinkron dengan kode.  

## Kenapa Django sering dipilih sebagai permulaan belajar framework web?

Beberapa alasan yang membuat Django cocok sebagai starting-point:

* **Batteries-included**: Django menyediakan banyak fitur bawaan (ORM, authentication, admin, forms, templating) sehingga pembelajar tidak harus merakit banyak komponen sendiri.
* **Konvensi yang jelas**: struktur proyek yang teratur (settings, urls, views, models, templates) memudahkan pemahaman arsitektur web.
* **Keamanan**: Django otomatis melindungi banyak celah umum (CSRF, XSS, SQL injection) bila digunakan sesuai dokumentasi.
* **Dokumentasi & komunitas besar**: banyak tutorial, paket pihak ketiga, dan contoh nyata.
* **Scale & praktik industri**: Django digunakan di startup dan perusahaan besar sehingga apa yang dipelajari relevan di dunia kerja.

## Feedback untuk asisten dosen (Tutorial 1)

Berikut contoh feedback yang bisa kamu pakai / edit sebelum dikirim:

* Hal-hal yang sudah baik:

  * Penjelasan langkah-langkah sangat sistematis dan ada contoh potongan kode.
  * Checklist tugas jelas dan terukur.

* Hal yang bisa diperbaiki:
.
  * Diberi lebih banyak contoh praktis (misalnya contoh views dengan konteks yang lebih variatif).

  * Disediakan ringkasan materi di akhir tutorial agar mudah direview.
  * Memberikan sedikit tips best practice agar mahasiswa tidak hanya mengikuti langkah, tapi juga mengerti alasannya.
---

# Tugas 3

## Pentingnya Data Delivery dalam Pengimplementasian Platform
Data delivery sangat penting dalam pengimplementasian sebuah platform karena data tidak hanya perlu disimpan, tetapi juga harus dikirim dan disajikan dengan aman, cepat, reliabel, dan konsisten kepada pengguna maupun komponen lain yang membutuhkan. Mekanisme ini memastikan informasi sampai ke tujuan yang tepat, tetap sinkron antar pengguna, terjaga dari gangguan atau kebocoran, efisien dalam penggunaan sumber daya, serta mendukung skalabilitas ketika platform berkembang. Tanpa data delivery, platform hanya menjadi tempat penyimpanan pasif tanpa nilai interaktif. Contohnya pada tugas kali ini, data tidak hanya diakses oleh satu program saja, sehingga keberadaan data delivery menjadi sangat krusial.

## XML vs JSON: Mana yang Lebih Baik?
Menurut saya, JSON lebih baik dibandingkan XML karena strukturnya lebih sederhana, modern, dan tidak membutuhkan banyak tag seperti XML. JSON juga lebih mudah dibaca dan dipahami oleh programmer, sekaligus memiliki proses parsing yang lebih cepat karena dapat langsung diproses oleh hampir semua bahasa pemrograman tanpa library tambahan. Inilah yang membuat JSON lebih populer dibanding XML.  
Meskipun begitu, XML masih digunakan pada sistem lama atau aplikasi yang membutuhkan fitur kompleks seperti schema, namespace, dan validasi dokumen. Namun, untuk kebutuhan web maupun mobile yang menuntut efisiensi dan kecepatan, JSON jauh lebih unggul dan lebih banyak digunakan.

## Fungsi Method `is_valid()` pada Form Django
Di Django, method `is_valid()` pada form digunakan untuk memeriksa apakah data yang dimasukkan sesuai dengan aturan validasi yang telah ditentukan. Jika semua field sudah benar sesuai tipe data, panjang karakter, format (misalnya email valid), maupun aturan khusus lainnya, maka `is_valid()` akan mengembalikan `True`. Jika terdapat kesalahan, method ini akan mengembalikan `False` dan detail error dapat diakses melalui `form.errors`.  
Method ini penting untuk mencegah data yang tidak valid masuk ke database serta memberikan feedback otomatis kepada pengguna ketika terjadi kesalahan input, sehingga data yang disimpan tetap aman, bersih, dan sesuai standar.

## Pentingnya `csrf_token` pada Form Django
`csrf_token` di Django digunakan untuk mencegah serangan **Cross-Site Request Forgery (CSRF)**, yaitu serangan ketika penyerang mencoba memanipulasi user agar tanpa sadar mengirimkan request berbahaya ke server (misalnya transfer uang atau mengubah password) dengan memanfaatkan sesi login yang masih aktif.  

Jika kita tidak menambahkan `csrf_token` pada form, maka form tersebut rentan terhadap serangan CSRF. Server tidak bisa membedakan apakah request benar-benar berasal dari form sah di aplikasi kita atau dari situs berbahaya yang dibuat oleh penyerang.  
Penyerang dapat memanfaatkan celah ini dengan cara membuat halaman berisi form tersembunyi yang otomatis mengirim request ke server kita. Jika user sedang login, request tersebut akan dieksekusi dengan hak akses user tersebut tanpa sepengetahuan mereka.

## Implementasi Checklist Step-by-Step

1. **Mengimplementasikan skeleton sebagai kerangka views**  
   Membuat berkas `base.html` di dalam direktori `templates` pada root project. File ini digunakan sebagai template dasar yang nantinya akan diwarisi oleh halaman-halaman lain agar konsisten dalam tampilan.

2. **Membuat 4 fungsi untuk mengembalikan data model dalam format XML dan JSON**  
   Menambahkan fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` pada `views.py` di direktori `main`.  
   - Fungsi `show_xml` dan `show_json` mengembalikan seluruh data produk.  
   - Fungsi `show_xml_by_id` dan `show_json_by_id` menerima parameter `product_id` untuk mengambil data berdasarkan ID.  
   Data kemudian diserialisasi menjadi format XML atau JSON sebelum dikembalikan sebagai response.

3. **Melakukan routing URL untuk keempat fungsi di atas**  
   Pada `urls.py` di direktori `main`, import fungsi-fungsi tersebut lalu menambahkan path pada `urlpatterns`.

4. **Membuat halaman utama untuk menampilkan data dengan tombol Add dan Detail**  
   - Pada fungsi `show_main` ditambahkan data `product_list` berisi semua produk, kemudian diteruskan ke `context`.  
   - Pada `main.html`, data produk ditampilkan dengan loop (`{% for product in product_list %}`).  
   - Ditambahkan tombol **Add** untuk menambahkan produk baru dan tombol **Detail** untuk melihat detail tiap produk.

5. **Membuat halaman form untuk menambahkan produk baru**  
   - Membuat `forms.py` di direktori `main` dengan class `ProductForm` yang mendefinisikan field yang harus diisi user.  
   - Menambahkan fungsi `add_product` pada `views.py` untuk menampilkan dan memproses form.  
   - Membuat template `add_product.html` untuk menampilkan form tersebut, dengan menyertakan `{% csrf_token %}` sebagai keamanan.  
   - Menambahkan path ke fungsi `add_product` pada `urls.py`.  
   - Pada `main.html`, tombol **Add** diarahkan ke halaman form menggunakan `{% url 'main:add_product' %}`.

6. **Membuat halaman detail produk**  
   - Membuat `product_detail.html` di `main/templates` untuk menampilkan informasi detail produk.  
   - Menambahkan fungsi `show_product` pada `views.py` yang menerima `product_id`, mengambil objek produk sesuai ID, dan me-render halaman detail.  
   - Menambahkan path `show_product` pada `urls.py`.  
   - Pada `main.html`, tombol **Detail** ditambahkan atribut `href="{% url 'main:show_product' product.id %}"`.

7. **Menambahkan domain deployment pada CSRF Trusted Origins**  
   Pada `settings.py`, menambahkan domain deployment project PWS ke dalam `CSRF_TRUSTED_ORIGINS`. Seperti dibawah:  
   ```python
   CSRF_TRUSTED_ORIGINS = [ 
    'http://alya-nabilla-false9store.pbp.cs.ui.ac.id',
   ]

## Hasil akses URL pada postman

![alt text](images/all-product-xml.png)
![alt text](images/all-product-json.png)
![alt text](images/specific-product-xml.png)
![alt text](images/specific-product-json.png)

---

## Penutup

README ini dibuat agar direktif tugas dapat dipahami oleh teman, asisten doesen dan dosen yang menilai. 

---

## Catatan tugas 3    
1. membuat 2 fungsi yang dapat menampilkan data dari model dalam format xml dan json.
2. membuat 2 fungsi yang dapat menampilkan data berdasarkan ID dari model dalam format xml dan json. 
agar dapat di akses di URL nya oleh pengguna maka saya daftarkan URL dg mngedit di file urls.py yang berada di direktori main (biar nggak notfound halamannya) 
3. mengimplementasikan skeleton sbg kerangka views
4. membuat form input data agar kita dapat menambah data
5. membuat halaman utama menampilkan produk, dan menambahkan button add dan detail dengan daapat render ke halaman add product dan detail produk