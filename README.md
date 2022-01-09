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
### Delete