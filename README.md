# Penjelasan Aplikasi API Silsilah Keluarga

## Cara menjalankan
buka command prompt, masuk ke dalam direktori repository ini<br>
ketikkan `python app.py`

## Route API
### Create
url endpoint = localhost:5000/tambahdata
methods = POST
parameter body json = 
{
    "id" : ....,<br>
    "nama" : "....",
    "jenis_kelamin" : "....",
    "nama_ortu" : "....",
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