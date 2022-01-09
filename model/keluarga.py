from sqlalchemy import create_engine, Column, String, Integer, and_
from sqlalchemy.orm import properties, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.selectable import subquery

Base = declarative_base()

class Keluarga(Base):
    __tablename__ = "keluarga"
    id = Column(Integer, primary_key=True)
    nama = Column(String)
    jenis_kelamin = Column(String)
    nama_ortu = Column(String)
    nama_kakek = Column(String)

class Database():
    # method yang digunakan untuk koneksi
    def __init__(self):
        try:
            self.engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/keluarga", echo=True)
            self.Session = sessionmaker(bind=self.engine)
            self.session =  self.Session()
            print("Sukses Koneksi Dengan sqlalchemy")
        except Exception as e:
            print(f"kesalahan koneksi database : {e}")

    # mehtod yang digunakan untuk melihat semua data
    def showAll(self):
        try:
            hasil = self.session.query(Keluarga).all()
            return hasil
        except Exception as e:
            print(f"kesalahan pada method showAll : {e}")

    # method yang digunakan untuk melihat data sesuai dengan parameter nama_ortu
    def showAnak(self, **params):
        try:
            hasil = self.session.query(Keluarga).filter(Keluarga.nama_ortu == params["nama_ortu"]).all()
            return hasil
        except Exception as e:
            print(f"kesalahan method showAnak : {e}")

    # method yang digunakan untuk melihat data sesuai dengan parameter nama_kakek, opsional jenis kelamin
    def showCucu(self, **params):
        try:
            if "jenis_kelamin" not in params.keys():
                hasil = self.session.query(Keluarga).filter(Keluarga.nama_kakek == params["nama_kakek"]).all()
            else:
                hasil = self.session.query(Keluarga).filter(and_(Keluarga.nama_kakek==params["nama_kakek"], Keluarga.jenis_kelamin==params["jenis_kelamin"])).all()
            return hasil
        except Exception as e:
            print(f"kesalahan method showAnak : {e}")

    # method yang digunakan untuk mendapatkan data saudara sepupu berdasarkan parameter nama, opsional jenis_kelamin
    def showSepupu(self, **params):
        try:
            subquery = self.session.query(Keluarga).filter(Keluarga.nama==params["nama"]).one()
            name = subquery.nama_kakek
            if "jenis_kelamin" in params.keys():
                hasil = self.session.query(Keluarga).filter(and_(Keluarga.nama_kakek==name, Keluarga.jenis_kelamin==params["jenis_kelamin"], Keluarga.nama!=params["nama"])).all()
            else:
                hasil = self.session.query(Keluarga).filter(and_(Keluarga.nama_kakek==name, Keluarga.nama!=params["nama"])).all()
            return hasil
        except Exception as e:
            print(f"kesalahan method showSepupu : {e}")

    # method yang digunakan untuk mendapatkan bibi
    def showBibi(self, **params):
        try:
            subquery = self.session.query(Keluarga).filter(Keluarga.nama==params["nama"]).one()
            nama = subquery.nama_ortu
            hasil = self.session.query(Keluarga).filter(and_(Keluarga.jenis_kelamin=="Perempuan", Keluarga.nama!=nama, Keluarga.nama_ortu=="Budi")).all()
            return hasil
        except Exception as e:
            print(f"kesalahan method showBibi : {e}")

    # method yang digunakan untuk menambahkan data ke dalam database
    def insertData(self, **params):
        try:
            self.session.add(Keluarga(**params))
            self.session.commit()
        except Exception as e:
            print(f"kesalahan pada method insertData : {e}")

    # method yang digunakan untuk update data
    def updateData(self, **params):
        try:
            dataUpdate = self.session.query(Keluarga).filter(Keluarga.id==params["id"]).one()  #mengambil data
            if "nama" in params.keys():
                dataUpdate.nama = params["nama"]
            if "jenis_kelamin" in params.keys():
                dataUpdate.jenis_kelamin = params["jenis_kelamin"]
            if "nama_ortu" in params.keys():
                dataUpdate.nama_ortu = params["nama_ortu"]
            if "nama_kakek" in params.keys():
                dataUpdate.nama_kakek = params["nama_kakek"]
            self.session.commit()  # memberi tahu server
        except Exception as e:
            print(f"kesalahan pada method updateData : {e}")

    # method yang digunakan untuk menghapus data
    def deleteData(self, **params):
        try:
            if "id" in params.keys():
                data = self.session.query(Keluarga).filter(Keluarga.id==params["id"]).one()
            if "nama" in params.keys():
                data = self.session.query(Keluarga).filter(Keluarga.nama==params["nama"]).one()
            self.session.delete(data)
            self.session.commit()
        except Exception as e:
            print(f"kesalahan pada method deleteData : {e}")