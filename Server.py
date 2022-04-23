import socket
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
from threading import *
import time
'''
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
'''
'''
AF_INET soketin iletişim kurabileceği adreslerin türünü belirlemek için kullanılan adres ailesi
Burada İnternet Protocol v4 adresi. Soket oluşturduğumuz aman türünü belirlememiz lazım ve belirlendikten sonra o soket sadece o türde kullanılabilir.
Soket oluşturuyoruz çünkü iletişim kurmak için gerekli

sock_dgram datagram tabanlı bir protokol.Bir tane datagram yollanır ve bir tane datagram alınır daha sonra bağlantı sonlandırılır.

varış saati, düzeni,ve teslimi garanti edilemeten paket anahtarlamalı bir ağ ile ilişkilendirilmiş aktarım ünitesine datagram denir.

'''
'''
sock.bind(('192.168.0.1',12345))
#bind komutu sayesinde socketin ip adresi ve port numarası atanır
'''
'''
while True:
    data,addr=sock.recvfrom(4096) # diğer taraftan gelen paket alınır. recvfrom sayesinde udp sokete yollanan bytes ı okur. parantez içine yazdığımı sayıda
    #kaç tane byte okuduğunu gösteriyor.

    print(str(data))
    message="hello I am udp server".encode('utf-8') #mesajımızı utf-8 formatına çeviriyoruz.
    sock.sendto(message,addr) #mesajı belirlenen adresden alıyor.
'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.host='192.168.0.1' #Server ip
        self.port=4000 #server port
        self.server=('192.168.0.1',4000) #server ip ve port
        self.client=('192.168.0.2',4005) #client ip ve port
        self.clientip='192.168.0.2' #client ip
        self.clientport=4005 #client port


        self.s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((self.host,self.port))


    def gonderme(self):
        self.gonderilecekmsg=self.yazmayeri.text()
        self.s.sendto(self.gonderilecekmsg.encode('utf-8'),self.client)
        self.bilgiekrani.append("Server: "+ self.gonderilecekmsg)
        self.yazmayeri.clear()

    def alma(self):
        self.baglantus.setEnabled(False)
        while True:
            data, addr=self.s.recvfrom(4096*4)
            data=data.decode('utf-8')
            self.bilgiekrani.append("Received from client :"+data)
            if bool(data):
                print("x")
            time.sleep(0.01)

    def thread(self):
        t1=Thread(target=self.alma)
        t1.start()

    def initUI(self):
        self.setGeometry(20,50,500,500)
        self.setWindowTitle("UDP haberleşme server")

        vboxana=QVBoxLayout()
        hbox0=QHBoxLayout()

        self.bilgiekrani=QTextEdit()
        self.bilgiekrani.setReadOnly(
            True
        )
        self.bilgiekrani.setFixedSize(600,400)
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

        self.gondertus=QPushButton("Gönder")
        self.gondertus.setFixedSize(100,50)
        hbox1.addWidget(self.gondertus)
        self.gondertus.clicked.connect(self.gonderme)

        self.baglantus=QPushButton('Bağlan', self)
        self.baglantus.setFixedSize(100,50)
        hbox1.addWidget(self.baglantus)
        self.baglantus.clicked.connect(self.thread)

        vboxana.addLayout(hbox1)

def run():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    run()



'''
print("server started")
host='192.168.0.1'
port =4000

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host, port))


while True:
    #data, addr=s.recvfrom(1024)
    #data=data.decode('utf-8')
    #print("message from "+str(addr))
    #print("from connected user:"+data)
    #data=data.upper()
    #print("sending :"+data)
    print("x")
    s.sendto("oldu heralde".encode('utf-8'),('192.168.0.2',4005))
    time.sleep(1)
c.close()
'''

