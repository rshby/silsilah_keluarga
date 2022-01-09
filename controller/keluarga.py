from model.keluarga import Database
from flask import json, jsonify

db = Database()

# function yang digunakan untuk melihat semua anggota keluarga
def viewAll():
    try:
        hasil = db.showAll()
        data_list = []
        for data in hasil:
            anggota_keluarga = {
                "id" : data.id,
                "nama" : data.nama,
                "jenis_kelamin" : data.jenis_kelamin,
                "nama_ortu" : data.nama_ortu,
                "nama_kakek" : data.nama_kakek
            }
            data_list.append(anggota_keluarga)
        return jsonify(data_list)
    except Exception as e:
        print(f"kesalahan pada function viewAll : {e}")

# function yang digunakan untuk melihat data berdasarkan parameter nama orang tua
def viewAnak(**params):
    try:
        hasil = db.showAnak(**params)
        data_list = []
        for data in hasil:
            anggota_keluarga = {
                "id" : data.id,
                "nama" : data.nama,
                "jenis_kelamin" : data.jenis_kelamin,
                "nama_ortu" : data.nama_ortu,
                "nama_kakek" : data.nama_kakek
            }
            data_list.append(anggota_keluarga)
        return jsonify(data_list)
    except Exception as e:
        print(f"kesalahan pada fucntion viewAnak : {e}")

# function yang digunakan untuk melihat data berdasarkan parameter nama kakek
def viewCucu(**params):
    try:
        hasil = db.showCucu(**params)
        data_list = []
        for data in hasil:
            anggota_keluarga = {
                "id" : data.id,
                "nama" : data.nama,
                "jenis_kelamin" : data.jenis_kelamin,
                "nama_ortu" : data.nama_ortu,
                "nama_kakek" : data.nama_kakek
            }
            data_list.append(anggota_keluarga)
        return jsonify(data_list)
    except Exception as e:
        print(f"kesalahan pada fucntion viewCucu : {e}")

# function yang digunakan untuk mendapatkan data sepupu
def viewSepupu(**params):
    try:
        hasil = db.showSepupu(**params)
        data_list = []
        for data in hasil:
            anggota_keluarga = {
                "id" : data.id,
                "nama" : data.nama,
                "jenis_kelamin" : data.jenis_kelamin
            }
            data_list.append(anggota_keluarga)
        return jsonify(data_list)
    except Exception as e:
        print(f"kesalahan function viewSepupu : {e}")

# function yang digunakan untuk mendapatkan bibi berdasarkan parameter nama
def viewBibi(**params):
    try:
        hasil = db.showBibi(**params)
        data_list = []
        for data in hasil:
            anggota_keluarga = {
                "id" : data.id,
                "nama" : data.nama,
                "jenis_kelamin" : data.jenis_kelamin,
                "nama_ortu" : data.nama_ortu
            }
            data_list.append(anggota_keluarga)
        return jsonify(data_list)
    except Exception as e:
        print(f"kesalahan pada function viewBibi : {e}")

# function yang digunakan untuk menambahkan data ke dalam database
def insertData(**params):
    try:
        db.insertData(**params)
        data = {
            "status" : "OK",
            "message" : "data berhasil ditambahkan"
        }
        return jsonify(data)
    except Exception as e:
        print(f"kesalahan pada function inserData : {e}") 

# function yang digunakan untuk melakukan update data
def updateData(**params):
    try:
        db.updateData(**params)
        data = {
            "status" : "OK",
            "message" : "data berhasil diupdate"
        }
        return jsonify(data)
    except Exception as e:
        print(f"kesalahan pada function updateData : {e}")

# function yang digunakan untuk menhapus data
def deleteData(**params):
    try:
        db.deleteData(**params)
        data = {
            "status" : "OK",
            "message" : "data berhasil dihapus"
        }
        return jsonify(data)
    except Exception as e:
        print(f"kesalahan pada function deleteData : {e}")