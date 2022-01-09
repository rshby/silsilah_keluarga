from logging import debug
from flask import Flask, jsonify, request
from sqlalchemy.orm import properties
from controller import keluarga

app = Flask(__name__)

# route api yang digunakan untuk mendapatkan semua data
@app.route("/allkeluarga", methods=["GET"])
def allKeluarga():
    try:
        return keluarga.viewAll()
    except Exception as e:
        print(f"kesalahan pada routing allKeluarga : {e}")

# route api yang digunakan untuk mendapatkan data berdasarkan parameter nama_ortu
@app.route("/dataanak", methods=["POST"])
def dataAnak():
    try:
        params = request.json
        return keluarga.viewAnak(**params)
    except Exception as e:
        print(f"kesalahan pada routing dataAnak : {e}")

# route api yang digunakan untuk mendapatkan data berdasarkan parameter nama_ortu
@app.route("/datacucu", methods=["POST"])
def dataCucu():
    try:
        params = request.json
        return keluarga.viewCucu(**params)
    except Exception as e:
        print(f"kesalahan pada routing dataCucu : {e}")

# routing api yang digunakan untuk menamilkan data sepupu berdasarkan parameter nama dan jenis_kelamin
@app.route("/datasepupu",methods=["POST"])
def dataSepupu():
    try:
        params = request.json
        return keluarga.viewSepupu(**params)
    except Exception as e:
        print(f"kesalahan pada routing dataSepupu : {e}")

# routing api yang digunakan untuk menampilkan data bibi menggunakan parameter nama
@app.route("/databibi", methods=["POST"])
def dataBibi():
    try:
        params = request.json
        return keluarga.viewBibi(**params)
    except Exception as e:
        print(f"kesalahan pada routing dataBibi : {e}")

# routing api yang digunakan untuk menambahkan data ke dalam database
@app.route("/tambahdata", methods=["POST"])
def tambahData():
    try:
        params = request.json
        return keluarga.insertData(**params)
    except Exception as e:
        print(f"kesalahan pada routing tambahData : {e}")

# roouting api yang digunakan untuk mengubah data berdasarkan id
@app.route("/ubahdata", methods=["POST"])
def ubahData():
    try:
        params = request.json
        return keluarga.updateData(**params)
    except Exception as e:
        print(f"kesalahan pada routing ubahData : {e}")

# route api yang digunakan untuk menghapus data berdasarkan id atau nama
@app.route("/hapusdata", methods=["POST"])
def hapusData():
    try:
        params = request.json
        return keluarga.deleteData(**params)
    except Exception as e:
        print(f"kesalahan pada routing api hapusData : {e}")

# run aplikasi
if __name__ == "__main__":
    app.run(debug=True, port=5000)