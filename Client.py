import socket
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit, QPushButton, QMainWindow , QVBoxLayout, QLabel, QHBoxLayout, QComboBox, QGroupBox
import sys
from threading import *
import time
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def on_text_changed(self):
            self.iportekle.setEnabled(bool(self.ipekletext.text()) and bool(self.portekletext.text()))
            self.baslat.setEnabled(bool(self.packetlengthtext.text()) and bool(self.timeintervaltext.text()) and bool(self.paketsayitext.text()))


    '''
    def Main(self):
        host = '192.168.0.2'  # client ip
        port = 4005  # client port
        server = ('192.168.0.1', 4000)  # server ip ve port

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host, port))

        message = input("-> ")
        while  message != 'q':
            s.sendto(message.encode('utf-8'),server)
            data,addr=s.recvfrom(1024)
            data=data.decode('utf-8')
            print("received from server : "+data)
            message=input("-> ")
            self.bilgiekrani.append("client: "+self.gonderilecekmsg)
            self.yazmayeri.clear()
        s.close()
    '''
    def ipadresicin(self):
        global ipadres
        ipadres=('%s' %(self.ipekletext.text()))
        print(ipadres)
        self.bilgiekrani.append("ip Adresi: " + str(ipadres))

    def porticin(self):
        global portnumarasi
        portnumarasi=('%s' %(self.portekletext.text()))
        print(portnumarasi)
        self.bilgiekrani.append("Port Numarası : " + str(portnumarasi))

    def numofpacketicin(self):
        self.numofpacket=int(self.paketsayitext.text())
        print(self.numofpacket)
        self.bilgiekrani.append("Paket sayısı : " + str(self.numofpacket))


    def packetlengthicin(self):
        self.packetlengthbyte=int(self.packetlengthtext.text())
        print(self.packetlengthbyte)
        self.bilgiekrani.append("Paket Uzunluğu (Bytes) : " + str(self.packetlengthbyte))


    def timeintervalicin(self):
        self.timeintervalsayi=int(self.timeintervaltext.text())
        print(self.timeintervalsayi)
        self.bilgiekrani.append("time interval : " + str(self.timeintervalsayi))


    def baglanicin(self):
        self.host = ('%s' % ipadres)  # client ip
        print(type(self.host))
        self.port = int(portnumarasi)  # client port
        self.server = ('192.168.0.1', 4000)  # server ip ve port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((self.host, self.port))
        self.bilgiekrani.append("%s ip adresine" % ipadres )
        self.bilgiekrani.append("%s port numarasına" % portnumarasi)
        self.bilgiekrani.append("bağlanıldı")
        self.baglantus.setEnabled(True)
        self.iportekle.setEnabled(False)
        self.gondertus.setEnabled(True)

    def gonderme(self):

            self.gonderilecekmsg = self.yazmayeri.text()
            self.s.sendto(self.gonderilecekmsg.encode('utf-8'),self.server)
            self.yazmayeri.clear()


    def paketgonderme(self):
        for x in range(0, int(self.numofpacket), 1):
            randnums = np.random.randint(0, 2, size=(int(self.packetlengthbyte)))
            listToStr = ' '.join([str(elem) for elem in randnums])

            print(listToStr)
            print(type(listToStr))
            self.s.sendto(listToStr.encode('utf-8'), self.server)
            # self.gonderilecekmsg = self.yazmayeri.text()
            # self.s.sendto(self.gonderilecekmsg.encode('utf-8'),self.server)
            self.bilgiekrani.append("client : " + listToStr)
            time.sleep((int(self.timeintervalsayi)) / 100)
            # self.yazmayeri.clear()

    def alma(self):
       self.baglantus.setEnabled(False)
       while True:
            data, addr = self.s.recvfrom(8192)
            data = data.decode('utf-8')
            self.bilgiekrani.append("received from server : " + data)
            time.sleep(0.01)


    def thread(self):
        t1=Thread(target=self.alma)
        t1.start()

    def initUI(self):
        self.setGeometry(20,50,500,500)
        self.setWindowTitle("UDP Haberleşme Client")

        vboxana=QVBoxLayout()
        hbox0=QHBoxLayout()

        self.bilgiekrani=QTextEdit()
        self.bilgiekrani.setReadOnly(
            True)
        self.bilgiekrani.setFixedSize(720,400)
        hbox0.addWidget(self.bilgiekrani)
        vboxana.addLayout(hbox0)

        vboxana.addStretch()
        centralWidget=QWidget()
        centralWidget.setLayout(vboxana)
        self.setCentralWidget(centralWidget)

        hbox1=QHBoxLayout()

        self.yazmayeri=QLineEdit()
        self.yazmayeri.setFixedSize(500,100)
        hbox1.addWidget(self.yazmayeri)

        self.gondertus=QPushButton("Yazı Gönder")
        self.gondertus.setFixedSize(100,50)
        self.gondertus.setEnabled(False)
        hbox1.addWidget(self.gondertus)
        self.gondertus.clicked.connect(self.gonderme)

        self.baglantus=QPushButton('Alma için bağlan',self)
        self.baglantus.setFixedSize(100,50)
        hbox1.addWidget(self.baglantus)
        self.baglantus.clicked.connect(self.thread)
        self.baglantus.setEnabled(False)
        vboxana.addLayout(hbox1)

        hbox2=QHBoxLayout()
        self.ipekle=QPushButton("Client IP Address")
        self.ipekle.setFixedSize(400,30)
        self.ipekletext=QLineEdit()
        hbox2.addWidget(self.ipekletext)
        hbox2.addWidget(self.ipekle)

        vboxana.addLayout(hbox2)

        hbox3=QHBoxLayout()
        self.portekle=QPushButton("Client Port")
        self.portekle.setFixedSize(400,30)
        self.portekletext=QLineEdit()
        hbox3.addWidget(self.portekletext)
        hbox3.addWidget(self.portekle)

        vboxana.addLayout(hbox3)

        hbox7 = QHBoxLayout()
        self.iportekle = QPushButton("Port oluştur ve bağlan")
        self.iportekle.setEnabled(False)
        hbox7.addWidget(self.iportekle)

        vboxana.addLayout(hbox7)


        hbox4 = QHBoxLayout()
        self.paketsayi = QPushButton("Number of Packets")
        self.paketsayi.setFixedSize(400, 30)
        self.paketsayitext = QLineEdit()
        hbox4.addWidget(self.paketsayitext)
        hbox4.addWidget(self.paketsayi)

        vboxana.addLayout(hbox4)

        hbox5 = QHBoxLayout()
        self.packetlength = QPushButton("Packet Length (Bytes)")
        self.packetlength.setFixedSize(400, 30)
        self.packetlengthtext = QLineEdit()
        hbox5.addWidget(self.packetlengthtext)
        hbox5.addWidget(self.packetlength)

        vboxana.addLayout(hbox5)

        hbox6 = QHBoxLayout()
        self.timeinterval = QPushButton("Time İnterval (ms)")
        self.timeinterval.setFixedSize(400, 30)
        self.timeintervaltext = QLineEdit()
        hbox6.addWidget(self.timeintervaltext)
        hbox6.addWidget(self.timeinterval)
        vboxana.addLayout(hbox6)

        hbox8=QHBoxLayout()
        self.baslat=QPushButton("Paket Göndermeyi başlat")
        self.baslat.setEnabled(False)
        hbox8.addWidget(self.baslat)
        self.baslat.clicked.connect(self.paketgonderme)

        vboxana.addLayout(hbox8)


        self.ipekle.clicked.connect(self.ipadresicin)
        self.portekle.clicked.connect(self.porticin)
        self.paketsayi.clicked.connect(self.numofpacketicin)
        self.timeinterval.clicked.connect(self.timeintervalicin)
        self.packetlength.clicked.connect(self.packetlengthicin)
        self.iportekle.clicked.connect(self.baglanicin)

        self.packetlengthtext.textChanged.connect(self.on_text_changed)
        self.timeintervaltext.textChanged.connect(self.on_text_changed)
        self.paketsayitext.textChanged.connect(self.on_text_changed)
        self.ipekletext.textChanged.connect(self.on_text_changed)
        self.portekletext.textChanged.connect(self.on_text_changed)



def run():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    run()
