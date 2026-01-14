from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import sys

from api_client import APIClient


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Anamenu")
        MainWindow.resize(528, 575)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.label_modeline = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_modeline.setFont(font)
        self.label_modeline.setMouseTracking(False)
        self.label_modeline.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_modeline.setAutoFillBackground(False)
        self.label_modeline.setTextFormat(QtCore.Qt.AutoText)
        self.label_modeline.setAlignment(QtCore.Qt.AlignCenter)
        self.label_modeline.setObjectName("label_modeline")
        self.verticalLayout_2.addWidget(self.label_modeline)
        
        # Ürün ekle
        self.pushButton_urun_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_urun_ekle.setObjectName("pushButton_urun_ekle")
        self.verticalLayout_2.addWidget(self.pushButton_urun_ekle)
        self.pushButton_urun_ekle.clicked.connect(self.go_urun_ekle)
        
        # Ürün listele sil
        self.pushButton_urun_listele_sil = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_urun_listele_sil.setObjectName("pushButton_urun_listele_sil")
        self.verticalLayout_2.addWidget(self.pushButton_urun_listele_sil)
        self.pushButton_urun_listele_sil.clicked.connect(self.go_urun_listele_sil)

        # Maliyet Hesapla
        self.pushButton_maliyet_hesapla = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_maliyet_hesapla.setObjectName("pushButton_maliyet_hesapla")
        self.verticalLayout_2.addWidget(self.pushButton_maliyet_hesapla)
        self.pushButton_maliyet_hesapla.clicked.connect(self.go_maliyet_hesapla)
        
        # Fiyatlandırma düzenle
        self.pushButton_fiyatlama_duzenle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_fiyatlama_duzenle.setObjectName("pushButton_fiyatlama_duzenle")
        self.verticalLayout_2.addWidget(self.pushButton_fiyatlama_duzenle)
        self.pushButton_fiyatlama_duzenle.clicked.connect(self.go_fiyatlama_duzenle)
        
        # Excel çıktısı al
        self.pushButton_excel_cikti_al = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_excel_cikti_al.setObjectName("pushButton_excel_cikti_al")
        self.verticalLayout_2.addWidget(self.pushButton_excel_cikti_al)
        self.pushButton_excel_cikti_al.clicked.connect(self.go_excel_cikti_al)
        
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Anamenu", "Anamenu"))
        self.label_modeline.setText(_translate("MainWindow", "Modeline"))
        self.pushButton_urun_ekle.setText(_translate("MainWindow", "Ürün ekle"))
        self.pushButton_urun_listele_sil.setText(_translate("MainWindow", "Ürün listele ve sil"))
        self.pushButton_maliyet_hesapla.setText(_translate("MainWindow", "Maliyet hesapla"))
        self.pushButton_fiyatlama_duzenle.setText(_translate("MainWindow", "Fiyatlama düzenle"))
        self.pushButton_excel_cikti_al.setText(_translate("MainWindow", "Excel çıktısı al"))
        
    def go_urun_ekle(self):
        self.close()
        self.urun_ekle_window = UrunEkleWindow()
        self.urun_ekle_window.show()

    def go_urun_listele_sil(self):
        self.close()
        self.urun_listele_sil_window = UrunListeleSilWindow()
        self.urun_listele_sil_window.show()

    def go_maliyet_hesapla(self):
        self.close()
        self.maliyet_hesapla_window = MaliyetHesaplaWindow()
        self.maliyet_hesapla_window.show()

    def go_fiyatlama_duzenle(self):
        self.close()
        self.fiyatlama_duzenle_window = FiyatlamaDuzenleWindow()
        self.fiyatlama_duzenle_window.show()

    def go_excel_cikti_al(self):
        dosya_yolu, _ = QFileDialog.getSaveFileName(
            self,
            "Excel Kaydet",
            "",
            "Excel Dosyası (*.xlsx);;Tüm Dosyalar (*)"
        )
        if not dosya_yolu:
            return

        if not dosya_yolu.endswith(".xlsx"):
            dosya_yolu += ".xlsx"

        content = APIClient.excel_al()
        with open(dosya_yolu, "wb") as f:
            f.write(content)



class UrunEkleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Urun ekle")
        MainWindow.resize(988, 474)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.lineEdit_baski_suresi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_baski_suresi.setObjectName("lineEdit_baski_suresi")
        self.gridLayout.addWidget(self.lineEdit_baski_suresi, 2, 1, 1, 1)
        
        self.textEdit_aciklama = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_aciklama.setObjectName("textEdit_aciklama")
        self.gridLayout.addWidget(self.textEdit_aciklama, 4, 1, 1, 1)
        
        self.lineEdit_agirlik = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_agirlik.setObjectName("lineEdit_agirlik")
        self.gridLayout.addWidget(self.lineEdit_agirlik, 1, 1, 1, 1)
        
        self.label_basim_tarihi = QtWidgets.QLabel(self.centralwidget)
        self.label_basim_tarihi.setObjectName("label_basim_tarihi")
        self.gridLayout.addWidget(self.label_basim_tarihi, 3, 0, 1, 1)
        
        self.pushButton_kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kaydet.setObjectName("pushButton_kaydet")
        self.gridLayout.addWidget(self.pushButton_kaydet, 7, 1, 1, 1)
        self.pushButton_kaydet.clicked.connect(self.kaydet)
        
        self.label_musteri_adi = QtWidgets.QLabel(self.centralwidget)
        self.label_musteri_adi.setObjectName("label_musteri_adi")
        self.gridLayout.addWidget(self.label_musteri_adi, 0, 0, 1, 1)
        
        self.label_baski_suresi = QtWidgets.QLabel(self.centralwidget)
        self.label_baski_suresi.setObjectName("label_baski_suresi")
        self.gridLayout.addWidget(self.label_baski_suresi, 2, 0, 1, 1)
        
        self.label_malzeme = QtWidgets.QLabel(self.centralwidget)
        self.label_malzeme.setObjectName("label_malzeme")
        self.gridLayout.addWidget(self.label_malzeme, 6, 0, 1, 1)
        
        self.label_aciklama = QtWidgets.QLabel(self.centralwidget)
        self.label_aciklama.setObjectName("label_aciklama")
        self.gridLayout.addWidget(self.label_aciklama, 4, 0, 1, 1)
        
        self.comboBox_malzeme = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_malzeme.setObjectName("comboBox_malzeme")
        self.gridLayout.addWidget(self.comboBox_malzeme, 6, 1, 1, 1)
        self.comboBox_malzeme.clear()
        self.comboBox_malzeme.addItems(APIClient.malzemeler())

        
        self.lineEdit_basim_tarihi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_basim_tarihi.setObjectName("lineEdit_basim_tarihi")
        self.gridLayout.addWidget(self.lineEdit_basim_tarihi, 3, 1, 1, 1)
        
        self.label_agirlik = QtWidgets.QLabel(self.centralwidget)
        self.label_agirlik.setObjectName("label_agirlik")
        self.gridLayout.addWidget(self.label_agirlik, 1, 0, 1, 1)
        
        self.label_basim_zorlugu = QtWidgets.QLabel(self.centralwidget)
        self.label_basim_zorlugu.setObjectName("label_basim_zorlugu")
        self.gridLayout.addWidget(self.label_basim_zorlugu, 5, 0, 1, 1)
        
        self.lineEdit_musteri_adi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_musteri_adi.setObjectName("lineEdit_musteri_adi")
        self.gridLayout.addWidget(self.lineEdit_musteri_adi, 0, 1, 1, 1)
        
        self.comboBox_basim_zorlugu = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_basim_zorlugu.setObjectName("comboBox_basim_zorlugu")
        self.gridLayout.addWidget(self.comboBox_basim_zorlugu, 5, 1, 1, 1)
        self.comboBox_basim_zorlugu.clear()
        self.comboBox_basim_zorlugu.addItems(APIClient.zorluklar())

        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Urun ekle", "Urun ekle"))
        self.label_basim_zorlugu.setText(_translate("MainWindow", "Basım zorluğu:"))
        self.label_baski_suresi.setText(_translate("MainWindow", "Baskı süresi:"))
        self.pushButton_kaydet.setText(_translate("MainWindow", "Kaydet"))
        self.label_musteri_adi.setText(_translate("MainWindow", "Müşteri adı:"))
        self.label_malzeme.setText(_translate("MainWindow", "Malzeme:"))
        self.label_basim_tarihi.setText(_translate("MainWindow", "Basım tarihi:"))
        self.label_agirlik.setText(_translate("MainWindow", "Baskı ağırlığı:"))
        self.label_aciklama.setText(_translate("MainWindow", "Ürün açıklaması:"))
        
    def kaydet(self):
        try:
            payload = {
                "musteri_adi": self.lineEdit_musteri_adi.text(),
                "agirlik": float(self.lineEdit_agirlik.text()),
                "baski_suresi": float(self.lineEdit_baski_suresi.text()),
                "basim_zorlugu": self.comboBox_basim_zorlugu.currentText(),
                "malzeme": self.comboBox_malzeme.currentText(),
                "aciklama": self.textEdit_aciklama.toPlainText(),
                "basim_tarihi": self.lineEdit_basim_tarihi.text(),
            }

            APIClient.urun_ekle(payload)
            QtWidgets.QMessageBox.information(self, "Başarılı", "Kayıt başarılı")
            self.close()

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Hata", str(e))


class UrunListeleSilWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = APIClient.urunleri_getir()

        self.load_table()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(883, 464)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        self.verticalLayout.addWidget(self.tableWidget)
        
        self.pushButton_sil = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sil.setObjectName("pushButton_sil")
        self.verticalLayout.addWidget(self.pushButton_sil)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_sil.clicked.connect(self.delete_selected)

        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 883, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Seç"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Müşteri adı"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ağırlık"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Baskı süresi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Basım zorluğu"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Malzeme"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Açıklama"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Basım tarihi"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Filament maliyet"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Elektrik maliyet"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Baskı maliyet"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Ham maliyet"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Satış fiyatı"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Kar"))
        self.pushButton_sil.setText(_translate("MainWindow", "Sil"))

    def load_table(self):
        self.tableWidget.setRowCount(0)
        for index, urun in enumerate(self.data):
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            chk_item = QtWidgets.QTableWidgetItem()
            chk_item.setCheckState(QtCore.Qt.Unchecked)
            chk_item.setFlags(
                QtCore.Qt.ItemIsUserCheckable |
                QtCore.Qt.ItemIsEnabled
            )
            chk_item.setData(QtCore.Qt.UserRole, urun["id"])
            self.tableWidget.setItem(row, 0, chk_item)
            values = [
                urun["musteri_adi"],
                urun["agirlik"],
                urun["baski_suresi"],
                urun["basim_zorlugu"],
                urun["malzeme"],
                urun["aciklama"],
                urun["basim_tarihi"],
                urun["filament_maliyet"],
                urun["elektrik_maliyet"],
                urun["baski_maliyet"],
                urun["ham_maliyet"],
                urun["satis_fiyati"],
                urun["kar"],
            ]

            for col, value in enumerate(values, start=1):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem("" if value is None else str(value)))


    def delete_selected(self):
        silinecek_idler = []
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if item and item.checkState() == QtCore.Qt.Checked:
                silinecek_idler.append(item.data(QtCore.Qt.UserRole))
        if not silinecek_idler:
            return
        for uid in silinecek_idler:
            APIClient.urun_sil(uid)

        self.data = APIClient.urunleri_getir()

        self.load_table()
        self.go_main_window()

    def go_main_window(self):
        self.close()
        self.main_window = MainWindow()
        self.main_window.show()


class MaliyetHesaplaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 449)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        self.label_baski_maliyet_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_baski_maliyet_sonuc.setText("")
        self.label_baski_maliyet_sonuc.setObjectName("label_baski_maliyet_sonuc")
        self.gridLayout.addWidget(self.label_baski_maliyet_sonuc, 9, 1, 1, 1)
        
        self.label_filament_maliyet_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_filament_maliyet_sonuc.setText("")
        self.label_filament_maliyet_sonuc.setObjectName("label_filament_maliyet_sonuc")
        self.gridLayout.addWidget(self.label_filament_maliyet_sonuc, 7, 1, 1, 1)
        
        self.label_zorluk = QtWidgets.QLabel(self.centralwidget)
        self.label_zorluk.setObjectName("label_zorluk")
        self.gridLayout.addWidget(self.label_zorluk, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        
        self.label_satis_fiyati_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_satis_fiyati_sonuc.setText("")
        self.label_satis_fiyati_sonuc.setObjectName("label_satis_fiyati_sonuc")
        self.gridLayout.addWidget(self.label_satis_fiyati_sonuc, 11, 1, 1, 1)
        
        self.pushButton_hesapla = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hesapla.setObjectName("pushButton_hesapla")
        self.gridLayout.addWidget(self.pushButton_hesapla, 5, 1, 1, 1)
        self.pushButton_hesapla.clicked.connect(self.hesapla)
        
        self.label_agirlik = QtWidgets.QLabel(self.centralwidget)
        self.label_agirlik.setObjectName("label_agirlik")
        self.gridLayout.addWidget(self.label_agirlik, 0, 0, 1, 1)
        
        self.label_kar_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_kar_sonuc.setText("")
        self.label_kar_sonuc.setObjectName("label_kar_sonuc")
        self.gridLayout.addWidget(self.label_kar_sonuc, 12, 1, 1, 1)
        
        self.label_kar = QtWidgets.QLabel(self.centralwidget)
        self.label_kar.setObjectName("label_kar")
        self.gridLayout.addWidget(self.label_kar, 12, 0, 1, 1)
        
        self.label_satis_fiyati = QtWidgets.QLabel(self.centralwidget)
        self.label_satis_fiyati.setObjectName("label_satis_fiyati")
        self.gridLayout.addWidget(self.label_satis_fiyati, 11, 0, 1, 1)
        
        self.lineEdit_agirlik = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_agirlik.setObjectName("lineEdit_agirlik")
        self.gridLayout.addWidget(self.lineEdit_agirlik, 0, 1, 1, 1)
        
        self.label_baski_maliyet = QtWidgets.QLabel(self.centralwidget)
        self.label_baski_maliyet.setObjectName("label_baski_maliyet")
        self.gridLayout.addWidget(self.label_baski_maliyet, 9, 0, 1, 1)
        
        self.label_malzeme = QtWidgets.QLabel(self.centralwidget)
        self.label_malzeme.setObjectName("label_malzeme")
        self.gridLayout.addWidget(self.label_malzeme, 2, 0, 1, 1)
        
        self.label_ham_maliyet_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_ham_maliyet_sonuc.setText("")
        self.label_ham_maliyet_sonuc.setObjectName("label_ham_maliyet_sonuc")
        self.gridLayout.addWidget(self.label_ham_maliyet_sonuc, 10, 1, 1, 1)
        
        self.lineEdit_baski_suresi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_baski_suresi.setObjectName("lineEdit_baski_suresi")
        self.gridLayout.addWidget(self.lineEdit_baski_suresi, 1, 1, 1, 1)
        
        self.label_elektrik_maliyet_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_elektrik_maliyet_sonuc.setText("")
        self.label_elektrik_maliyet_sonuc.setObjectName("label_elektrik_maliyet_sonuc")
        self.gridLayout.addWidget(self.label_elektrik_maliyet_sonuc, 8, 1, 1, 1)
        
        self.label_baski_suresi = QtWidgets.QLabel(self.centralwidget)
        self.label_baski_suresi.setObjectName("label_baski_suresi")
        self.gridLayout.addWidget(self.label_baski_suresi, 1, 0, 1, 1)
        
        self.label_filament_maliyet = QtWidgets.QLabel(self.centralwidget)
        self.label_filament_maliyet.setObjectName("label_filament_maliyet")
        self.gridLayout.addWidget(self.label_filament_maliyet, 7, 0, 1, 1)
        
        self.label_elektrik_maliyet = QtWidgets.QLabel(self.centralwidget)
        self.label_elektrik_maliyet.setObjectName("label_elektrik_maliyet")
        self.gridLayout.addWidget(self.label_elektrik_maliyet, 8, 0, 1, 1)
        
        self.comboBox_malzeme = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_malzeme.setObjectName("comboBox_malzeme")
        self.gridLayout.addWidget(self.comboBox_malzeme, 2, 1, 1, 1)
        self.comboBox_malzeme.clear()
        self.comboBox_malzeme.addItems(APIClient.malzemeler())

        
        self.label_ham_maliyet = QtWidgets.QLabel(self.centralwidget)
        self.label_ham_maliyet.setObjectName("label_ham_maliyet")
        self.gridLayout.addWidget(self.label_ham_maliyet, 10, 0, 1, 1)
        
        self.comboBox_basim_zorlugu = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_basim_zorlugu.setObjectName("comboBox_basim_zorlugu")
        self.gridLayout.addWidget(self.comboBox_basim_zorlugu, 3, 1, 1, 1)
        self.comboBox_basim_zorlugu.clear()
        self.comboBox_basim_zorlugu.addItems(APIClient.zorluklar())

        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_zorluk.setText(_translate("MainWindow", "Zorluk: "))
        self.pushButton_hesapla.setText(_translate("MainWindow", "Hesapla"))
        self.label_agirlik.setText(_translate("MainWindow", "Ağrılık: "))
        self.label_kar.setText(_translate("MainWindow", "Kar: "))
        self.label_satis_fiyati.setText(_translate("MainWindow", "Satış fiyati: "))
        self.label_baski_maliyet.setText(_translate("MainWindow", "Baski maliyeti: "))
        self.label_malzeme.setText(_translate("MainWindow", "Malzeme: "))
        self.label_baski_suresi.setText(_translate("MainWindow", "Baskı süresi: "))
        self.label_filament_maliyet.setText(_translate("MainWindow", "Filament maliyeti: "))
        self.label_elektrik_maliyet.setText(_translate("MainWindow", "Elektrik maliyeti: "))
        self.label_ham_maliyet.setText(_translate("MainWindow", "Ham maliyet: "))
        
    def hesapla(self):
        try:
            sonuc = APIClient.maliyet_hesapla({
            "agirlik": float(self.lineEdit_agirlik.text()),
            "baski_suresi": float(self.lineEdit_baski_suresi.text()),
            "malzeme": self.comboBox_malzeme.currentText(),
            "basim_zorlugu": self.comboBox_basim_zorlugu.currentText()
            })

            self.label_filament_maliyet_sonuc.setText(f"{sonuc['filament_maliyet']:.2f} TL")
            self.label_elektrik_maliyet_sonuc.setText(f"{sonuc['elektrik_maliyet']:.2f} TL")
            self.label_baski_maliyet_sonuc.setText(f"{sonuc['baski_maliyet']:.2f} TL")
            self.label_ham_maliyet_sonuc.setText(f"{sonuc['ham_maliyet']:.2f} TL")
            self.label_satis_fiyati_sonuc.setText(f"{sonuc['satis_fiyati']:.2f} TL")
            self.label_kar_sonuc.setText(f"{sonuc['kar']:.2f} TL")

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Hata", "Lütfen geçerli değerler girin!")


class FiyatlamaDuzenleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.refresh_maliyetler()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 405)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        self.label_saat_basi_kw = QtWidgets.QLabel(self.centralwidget)
        self.label_saat_basi_kw.setObjectName("label_saat_basi_kw")
        self.gridLayout.addWidget(self.label_saat_basi_kw, 2, 0, 1, 1)
        
        self.label_saatlik_baski_katsayi = QtWidgets.QLabel(self.centralwidget)
        self.label_saatlik_baski_katsayi.setObjectName("label_saatlik_baski_katsayi")
        self.gridLayout.addWidget(self.label_saatlik_baski_katsayi, 5, 0, 1, 1)
        
        self.label_sabit_kurulum_ucreti = QtWidgets.QLabel(self.centralwidget)
        self.label_sabit_kurulum_ucreti.setObjectName("label_sabit_kurulum_ucreti")
        self.gridLayout.addWidget(self.label_sabit_kurulum_ucreti, 6, 0, 1, 1)
        
        self.label_kwh_fiyat = QtWidgets.QLabel(self.centralwidget)
        self.label_kwh_fiyat.setObjectName("label_kwh_fiyat")
        self.gridLayout.addWidget(self.label_kwh_fiyat, 3, 0, 1, 1)
        
        self.label_saatlik_baski_ucreti = QtWidgets.QLabel(self.centralwidget)
        self.label_saatlik_baski_ucreti.setObjectName("label_saatlik_baski_ucreti")
        self.gridLayout.addWidget(self.label_saatlik_baski_ucreti, 4, 0, 1, 1)
        
        self.label_kar_orani = QtWidgets.QLabel(self.centralwidget)
        self.label_kar_orani.setObjectName("label_kar_orani")
        self.gridLayout.addWidget(self.label_kar_orani, 7, 0, 1, 1)
        
        self.label_filament_kg_maliyet = QtWidgets.QLabel(self.centralwidget)
        self.label_filament_kg_maliyet.setObjectName("label_filament_kg_maliyet")
        self.gridLayout.addWidget(self.label_filament_kg_maliyet, 0, 0, 1, 1)
        
        self.label_filament_kg_maliyet_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_filament_kg_maliyet_sonuc.setText("")
        self.label_filament_kg_maliyet_sonuc.setObjectName("label_filament_kg_maliyet_sonuc")
        self.gridLayout.addWidget(self.label_filament_kg_maliyet_sonuc, 0, 1, 1, 1)
        
        self.label_saat_basi_kw_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_saat_basi_kw_sonuc.setText("")
        self.label_saat_basi_kw_sonuc.setObjectName("label_saat_basi_kw_sonuc")
        self.gridLayout.addWidget(self.label_saat_basi_kw_sonuc, 2, 1, 1, 1)
        
        self.label_kwh_fiyat_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_kwh_fiyat_sonuc.setText("")
        self.label_kwh_fiyat_sonuc.setObjectName("label_kwh_fiyat_sonuc")
        self.gridLayout.addWidget(self.label_kwh_fiyat_sonuc, 3, 1, 1, 1)
        
        self.label_saatlik_baski_ucreti_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_saatlik_baski_ucreti_sonuc.setText("")
        self.label_saatlik_baski_ucreti_sonuc.setObjectName("label_saatlik_baski_ucreti_sonuc")
        self.gridLayout.addWidget(self.label_saatlik_baski_ucreti_sonuc, 4, 1, 1, 1)
        
        self.label_saatlik_baski_katsayi_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_saatlik_baski_katsayi_sonuc.setText("")
        self.label_saatlik_baski_katsayi_sonuc.setObjectName("label_saatlik_baski_katsayi_sonuc")
        self.gridLayout.addWidget(self.label_saatlik_baski_katsayi_sonuc, 5, 1, 1, 1)
        
        self.label_sabit_kurulum_ucreti_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_sabit_kurulum_ucreti_sonuc.setText("")
        self.label_sabit_kurulum_ucreti_sonuc.setObjectName("label_sabit_kurulum_ucreti_sonuc")
        self.gridLayout.addWidget(self.label_sabit_kurulum_ucreti_sonuc, 6, 1, 1, 1)
        
        self.label_kar_orani_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_kar_orani_sonuc.setText("")
        self.label_kar_orani_sonuc.setObjectName("label_kar_orani_sonuc")
        self.gridLayout.addWidget(self.label_kar_orani_sonuc, 7, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.lineEdit_saat_basi_kw = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_saat_basi_kw.setObjectName("lineEdit_saat_basi_kw")
        self.gridLayout_3.addWidget(self.lineEdit_saat_basi_kw, 2, 1, 1, 1)
        
        self.lineEdit_sabit_kurulum_ucreti = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sabit_kurulum_ucreti.setObjectName("lineEdit_sabit_kurulum_ucreti")
        self.gridLayout_3.addWidget(self.lineEdit_sabit_kurulum_ucreti, 6, 1, 1, 1)
        
        self.label_saatlik_baski_katsayi_guncel = QtWidgets.QLabel(self.centralwidget)
        self.label_saatlik_baski_katsayi_guncel.setObjectName("label_saatlik_baski_katsayi_guncel")
        self.gridLayout_3.addWidget(self.label_saatlik_baski_katsayi_guncel, 5, 0, 1, 1)
        
        self.label_kar_orani_guncel = QtWidgets.QLabel(self.centralwidget)
        self.label_kar_orani_guncel.setObjectName("label_kar_orani_guncel")
        self.gridLayout_3.addWidget(self.label_kar_orani_guncel, 7, 0, 1, 1)
        
        self.lineEdit_kwh_fiyat = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kwh_fiyat.setObjectName("lineEdit_kwh_fiyat")
        self.gridLayout_3.addWidget(self.lineEdit_kwh_fiyat, 3, 1, 1, 1)
        
        self.lineEdit_kar_orani = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kar_orani.setObjectName("lineEdit_kar_orani")
        self.gridLayout_3.addWidget(self.lineEdit_kar_orani, 7, 1, 1, 1)
        
        self.label_saat_basi_kw_guncel = QtWidgets.QLabel(self.centralwidget)
        self.label_saat_basi_kw_guncel.setObjectName("label_saat_basi_kw_guncel")
        self.gridLayout_3.addWidget(self.label_saat_basi_kw_guncel, 2, 0, 1, 1)
        
        self.label_sabit_kurulum_ucreti_guncel = QtWidgets.QLabel(self.centralwidget)
        self.label_sabit_kurulum_ucreti_guncel.setObjectName("label_sabit_kurulum_ucreti_guncel")
        self.gridLayout_3.addWidget(self.label_sabit_kurulum_ucreti_guncel, 6, 0, 1, 1)
        
        self.lineEdit_filament_kg_maliyet = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filament_kg_maliyet.setObjectName("lineEdit_filament_kg_maliyet")
        self.gridLayout_3.addWidget(self.lineEdit_filament_kg_maliyet, 0, 1, 1, 1)
        
        self.lineEdit_saatlik_baski_ucreti = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_saatlik_baski_ucreti.setObjectName("lineEdit_saatlik_baski_ucreti")
        self.gridLayout_3.addWidget(self.lineEdit_saatlik_baski_ucreti, 4, 1, 1, 1)
        
        self.lineEdit_saatlik_baski_katsayi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_saatlik_baski_katsayi.setObjectName("lineEdit_saatlik_baski_katsayi")
        self.gridLayout_3.addWidget(self.lineEdit_saatlik_baski_katsayi, 5, 1, 1, 1)
        
        self.label_filament_kg_maliyet_guncel = QtWidgets.QLabel(self.centralwidget)
        self.label_filament_kg_maliyet_guncel.setObjectName("label_filament_kg_maliyet_guncel")
        self.gridLayout_3.addWidget(self.label_filament_kg_maliyet_guncel, 0, 0, 1, 1)
        
        self.label_kwh_fiyat_guncel = QtWidgets.QLabel(self.centralwidget)
        self.label_kwh_fiyat_guncel.setObjectName("label_kwh_fiyat_guncel")
        self.gridLayout_3.addWidget(self.label_kwh_fiyat_guncel, 3, 0, 1, 1)
        
        self.label_saatlik_baski_ucreti_guncel = QtWidgets.QLabel(self.centralwidget)
        self.label_saatlik_baski_ucreti_guncel.setObjectName("label_saatlik_baski_ucreti_guncel")
        self.gridLayout_3.addWidget(self.label_saatlik_baski_ucreti_guncel, 4, 0, 1, 1)
        
        self.pushButton_guncelle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_guncelle.setObjectName("pushButton_guncelle")
        self.gridLayout_3.addWidget(self.pushButton_guncelle, 8, 1, 1, 1)
        self.pushButton_guncelle.clicked.connect(self.guncellle_maliyetler)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 8, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_saat_basi_kw.setText(_translate("MainWindow", "Saat başı KW: "))
        self.label_saatlik_baski_katsayi.setText(_translate("MainWindow", "Saatlik baskı katsayısı: "))
        self.label_sabit_kurulum_ucreti.setText(_translate("MainWindow", "Sabit kurulum ücreti:"))
        self.label_kwh_fiyat.setText(_translate("MainWindow", "KW fiyatı: "))
        self.label_saatlik_baski_ucreti.setText(_translate("MainWindow", "Saatlik baskı ücreti: "))
        self.label_kar_orani.setText(_translate("MainWindow", "Kar oranı:"))
        self.label_filament_kg_maliyet.setText(_translate("MainWindow", "Filament kg maliyet:"))
        self.label_saatlik_baski_katsayi_guncel.setText(_translate("MainWindow", "Saatlik baskı katsayısı: "))
        self.label_kar_orani_guncel.setText(_translate("MainWindow", "Kar oranı:"))
        self.label_saat_basi_kw_guncel.setText(_translate("MainWindow", "Saat başı KW: "))
        self.label_sabit_kurulum_ucreti_guncel.setText(_translate("MainWindow", "Sabit kurulum ücreti:"))
        self.label_filament_kg_maliyet_guncel.setText(_translate("MainWindow", "Filament kg maliyet:"))
        self.label_kwh_fiyat_guncel.setText(_translate("MainWindow", "KW fiyatı: "))
        self.label_saatlik_baski_ucreti_guncel.setText(_translate("MainWindow", "Saatlik baskı ücreti: "))
        self.pushButton_guncelle.setText(_translate("MainWindow", "Güncelle"))

    def guncellle_maliyetler(self):
        APIClient.sabitleri_guncelle({
            "filament_kg_maliyet": float(self.lineEdit_filament_kg_maliyet.text()),
            "saat_basi_kw": float(self.lineEdit_saat_basi_kw.text()),
            "kwh_fiyat": float(self.lineEdit_kwh_fiyat.text()),
            "saatlik_baski_ucreti": float(self.lineEdit_saatlik_baski_ucreti.text()),
            "saatlik_baski_katsayi": float(self.lineEdit_saatlik_baski_katsayi.text()),
            "sabit_kurulum_ucreti": float(self.lineEdit_sabit_kurulum_ucreti.text()),
            "kar_orani": float(self.lineEdit_kar_orani.text())
        })

        self.refresh_maliyetler()
    
    def refresh_maliyetler(self):
        sabitler = APIClient.sabitleri_getir()

        self.label_filament_kg_maliyet_sonuc.setText(
            f"{sabitler['filament_kg_maliyet']:.2f} TL"
        )
        self.label_saat_basi_kw_sonuc.setText(
            f"{sabitler['saat_basi_kw']:.2f} KW"
        )
        self.label_kwh_fiyat_sonuc.setText(
            f"{sabitler['kwh_fiyat']:.2f} TL"
        )
        self.label_saatlik_baski_ucreti_sonuc.setText(
            f"{sabitler['saatlik_baski_ucreti']:.2f} TL"
        )
        self.label_saatlik_baski_katsayi_sonuc.setText(
            f"{sabitler['saatlik_baski_katsayi']:.2f}"
        )
        self.label_sabit_kurulum_ucreti_sonuc.setText(
            f"{sabitler['sabit_kurulum_ucreti']:.2f} TL"
        )
        self.label_kar_orani_sonuc.setText(
            f"{sabitler['kar_orani']:.2f} %"
        )

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
    
    
    