import sys
from PyQt5 import QtWidgets
import sqlite3

class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.baglanti_olusturma()
        self.init_ui()

    def baglanti_olusturma(self):
        self.baglanti = sqlite3.connect("database.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("Create table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")

        self.baglanti.commit()

    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.sifre = QtWidgets.QLineEdit()
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş")
        self.yazi_alani = QtWidgets.QLabel("")
        self.kayit_ol =QtWidgets.QPushButton("Kayıt ol")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.sifre)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.kayit_ol)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()




        self.setLayout(h_box)
        self.kayit_ol.clicked.connect(self.login)
        self.giris.clicked.connect(self.login)
        self.show()
        
    def login(self):
        adi = self.kullanici_adi.text()
        pas = self.sifre.text()
        sender = self.sender()
        if sender.text() == "Giriş":
            self.cursor.execute("select * from üyeler where kullanıcı_adı = ? and parola = ?",(adi,pas))
            data = self.cursor.fetchall()

            if len(data) == 0:
                self.yazi_alani.setText("Böyle bir kullanıcı bulunamadı")
            else:
                self.yazi_alani.setText("Giriş yapılıyor..")
        else:
            self.cursor.execute("insert into üyeler values(?,?)",(adi,pas))
            self.baglanti.commit()
            self.yazi_alani.setText("Başarıyla kayıt yapıldı..")






app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())