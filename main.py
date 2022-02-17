# ! /usr/bin/python3
from sys import exit as sysExit
import sys
import os.path

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QFileDialog

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("main.ui", self)
        self.is_file = True
        self.is_encrypt = True
        self.filename = ""
        self.extension = "txt"
        self.arrCB = None
        self.arrPB = None
        self.jenis_file.setChecked(True)
        self.metode_encrypt.setChecked(True)
        self.input_key.setPlaceholderText("Masukkan kunci")
        self.input.setPlaceholderText("Masukkan pesan")
        self.save_filename.setPlaceholderText("Masukkan nama file")
        self.button.clicked.connect(self.generate)
        self.jenis_file.clicked.connect(self.change_jenis_pesan)
        self.jenis_plainteks.clicked.connect(self.change_jenis_pesan)
        self.metode_encrypt.clicked.connect(self.change_method)
        self.metode_decrypt.clicked.connect(self.change_method)
        self.save_button.clicked.connect(self.save_file)
        self.browse_button.clicked.connect(self.browse_file)
    
    def change_jenis_pesan(self):
        if(self.jenis_plainteks.isChecked()):
            self.is_file = False
            self.save_name = ""
            self.filename = ""
            self.extension = "txt"
        else:
            self.is_file = True
        self.alert.setText("")
        self.alert.setStyleSheet("color: black;")
    
    def save_file(self):
        self.save_name = self.save_filename.text()
        if(self.is_encrypt):
            if(self.arrCB is None):
                self.alert.setText("Enkripsi dulu!")
                self.alert.setStyleSheet("color: red;")
            else:
                w=open(self.save_name + "." + self.extension, "wb")
                w.write(self.arrCB)
                self.alert.setText("File berhasil disimpan!")
                self.alert.setStyleSheet("color: black;")
        else:
            if(self.arrPB is None):
                self.alert.setText("Dekripsi dulu!")
                self.alert.setStyleSheet("color: red;")
            else:
                w=open(self.save_name + "." + self.extension, "wb")
                w.write(self.arrPB)
                self.alert.setText("File berhasil disimpan!")
                self.alert.setStyleSheet("color: black;")

    def change_method(self):
        if(self.metode_encrypt.isChecked()):
            self.is_encrypt = True
            self.judul_input.setText("Plainteks")
            self.judul_output.setText("Cipherteks")
            self.button.setText("Encrypt")
        else:
            self.is_encrypt = False
            self.judul_input.setText("Cipherteks")
            self.judul_output.setText("Plainteks")
            self.button.setText("Decrypt")
        self.input.setText("")
        self.output.setText("")
        self.alert.setText("")
        self.alert.setStyleSheet("color: black;")
        self.arrCB = None
        self.arrPB = None
        self.browse_filename.setText("")
        
    def generate(self):
        if self.jenis_file.isChecked():
            self.is_file = True
        else:
            self.is_file = False
            self.input_text = self.input.toPlainText()
        
        if self.metode_encrypt.isChecked():
            self.is_encrypt = True
            if(self.is_file and (self.filename == "")):
                self.browse_filename.setText("Upload file dulu!")
            else:
                if(not self.is_file):
                    self.extension = "txt"
                self.encrypt()
        else:
            self.is_encrypt = False
            if(self.is_file and (self.filename == "")):
                self.browse_filename.setText("Upload file dulu!")
            else:
                if(not self.is_file):
                    self.extension = "txt"
                self.decrypt()
        
    def browse_file(self):
        file = QFileDialog.getOpenFileName(self)
        self.filename = file[0]
        self.browse_filename.setText(self.filename)
        self.extension = os.path.splitext(file[0])[1][1:]
        self.alert.setText("")
        self.alert.setStyleSheet("color: black;")
        
        if(self.extension == "txt"):
            arr = []
            f=open(self.filename,"rb")
            file_bytes = f.read()
            f.close()
            
            for byte in file_bytes:
                arr.append(chr(byte))
            self.input.setText(''.join(arr))

    def generate_key(self):
        self.key = self.input_key.toPlainText()
        self.S = [0 for i in range (256)]

        # Key-Scheduling Algorithm (KSA)
        # Inisialisasi array S dengan bilangan genap lalu diikuti bilangan ganjil
        for i in range(128):
            self.S[i] = i*2

        for i in range(128, 256):
            self.S[i] = 1 + (i-128)*2

        # Menambahkan LFSR yang dimodifikasi untuk menghasilkan keystream
        """
            1. Inisialisasi LFSR menggunakan kunci masukan pengguna
            2. Bit paling kiri di-XOR dengan bit paling kanan
            3. Keystream diambil dari bit paling kiri yang akan digeser keluar
            4. Menggeser setiap bit ke kiri
            5. Hasil XOR akan dimasukkan ke bit paling kanan
        """
        K = self.key
        KinB = bytes(K,'latin-1')
        arr = []
        for byte in KinB:
            arr.append(byte)
        
        # Memutarbalikkan key
        arr.reverse()
        
        Ks = []
        for i in range(len(arr)):
            temp = arr[len(arr)-1] ^ arr[0]
            Ks.append(arr[0])
            
            for j in range(len(arr)-1):
                arr[j] = arr[j+1]
            arr[len(arr)-1] = (temp)

        # Permutasi elemen array S berdasarkan kunci K
        j = 0
        for i in range(256):
            j = (j + self.S[i] + arr[i % len(arr)]) % 256
            
            # Swap
            temp = self.S[i]
            self.S[i] = self.S[j]
            self.S[j] = temp

    def encrypt(self):
        self.generate_key()
        if(self.is_file):
            f=open(self.filename,"rb")
            file_bytes = f.read()
            f.close()
            PinB = file_bytes
        else:
            P = self.input_text
            PinB = bytes(P,'latin-1')
        
        arrP = []
        for byte in PinB:
            arrP.append(byte)

        arrC = []
        strC = []

        # Pseudo-random Generation Algorithm (PRGA)
        """
            PRGA dimodifikasi pada bagian penentuan indeks keystream
            yang didapatkan dengan S[i] * S[j] 
        """
        i = 0
        j = 0

        for idx in range(len(arrP)):
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            
            # Swap
            temp = self.S[i]
            self.S[i] = self.S[j]
            self.S[j] = temp

            t = (self.S[i] * self.S[j]) % 256
            u = self.S[t]
            C = u ^ arrP[idx]
            strC.append(chr(C))
            arrC.append(C)

        self.arrCB = bytearray(arrC)
        self.output.setText(''.join(strC))

    def decrypt(self):
        self.generate_key()
        if(self.is_file):
            f=open(self.filename,"rb")
            file_bytes = f.read()
            f.close()
            CinB = file_bytes
        else:
            C = self.input_text
            CinB = bytes(C,"latin-1")
        
        arrC = []
        for byte in CinB:
            arrC.append(byte)

        arrP = []
        strP = []

        # Pseudo-random Generation Algorithm (PRGA)
        """
            PRGA dimodifikasi pada bagian penentuan indeks keystream
            yang didapatkan dengan S[i] * S[j] 
        """
        i = 0
        j = 0
        
        for idx in range(len(arrC)):
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            
            # Swap
            temp = self.S[i]
            self.S[i] = self.S[j]
            self.S[j] = temp

            t = (self.S[i] * self.S[j]) % 256
            u = self.S[t]
            P = u ^ arrC[idx]
            strP.append(chr(P))
            arrP.append(P)
            
        self.arrPB = bytearray(arrP)
        self.output.setText(''.join(strP))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("My Own Stream Cipher")

    main = MainScreen()
    
    widget = QStackedWidget()
    widget.addWidget(main)
    widget.setMinimumHeight(688)
    widget.setMinimumWidth(480)

    widget.show()
    
    sys.exit(app.exec_())