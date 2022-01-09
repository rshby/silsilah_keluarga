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
</t>"id" : ....,<br>
   "nama" : "....",<br>
   "jenis_kelamin" : "....",<br>
   "nama_ortu" : "....",<br>
   "nama_kakek" : "...."
}
hasil =
{
    "status" : "OK",
    "message" : "data berhasil ditambahkan"
}

### Read
### Update
### Delete