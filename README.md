# Penjelasan Aplikasi API Silsilah Keluarga

## Cara menjalankan
buka command prompt, masuk ke dalam direktori repository ini<br>
ketikkan `python app.py`

## Route API
### Create
url endpoint = localhost:5000/tambahdata<br>
methods = POST<br>
parameter body json =<br> 
{<br>
"id" : ....,<br>
   "nama" : "....",<br>
   "jenis_kelamin" : "....",<br>
   "nama_ortu" : "....",<br>
   "nama_kakek" : "...."<br>
}<br><br>
hasil =<br>
{<br>
    "status" : "OK",<br>
    "message" : "data berhasil ditambahkan"<br>
}<br>

### Read
### Update
url endpoint = localhost:5000/ubahdata<br>
methods = POST<br>
parameter body json =<br> 
{<br>
"id" : ....,<br>
"nama" : "....",<br>
"jenis_kelamin" : "....",<br>
"nama_ortu" : "....",<br>
"nama_kakek" : "...."<br>
}<br><br>
Hasil =<br>
{<br>
    "status" : "OK",<br>
    "message" : "data berhasil diupdate"<br>
}
### Delete
url endpoint = localhost:5000/hapusdata<br>
methods = POST<br>
parameter body json =<br> 
{<br>
"id" : ....,<br>
}<br>
atau<br>
{<br>
"nama" : "....",<br>
}<br><br>
Hasil =<br>
{<br>
    "status" : "OK",<br>
    "message" : "data berhasil dihapus"<br>
}