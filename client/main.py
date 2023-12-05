import sys
from socket import *
from PySide2.QtWidgets import QApplication,QMainWindow,QComboBox,QPushButton,QPlainTextEdit,QLabel

class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow,self).__init__()
        self.window = QMainWindow()
        self.window.resize(1000,750)
        self.window.setWindowTitle("QE-GUI")

        self.jobtype = QComboBox(self.window)
        self.jobtype.addItems(['Job Type','GeometryOptimization','Tc'])
        self.jobtype.resize(300,30)
        self.jobtype.move(20,20)

        self.poscar = QPlainTextEdit(self.window)
        self.poscar.setPlaceholderText("POSCAR")
        self.poscar.move(20,70)
        self.poscar.resize(400,400)

        self.pseudo = QComboBox(self.window)
        self.pseudo.addItems(['Pseudo Potential','PAW','ultrasoft'])
        self.pseudo.move(20,490)
        self.pseudo.resize(300,30)

        self.kpoints = QPlainTextEdit(self.window)
        self.kpoints.setPlaceholderText("Kpoints : 10*10*10")
        self.kpoints.move(20,540)
        self.kpoints.resize(300,30)

        self.ip = QPlainTextEdit(self.window)
        self.ip.setPlaceholderText("ip : 10.193.255.37")
        self.ip.move(20,590)
        self.ip.resize(300,30)

        self.port = QPlainTextEdit(self.window)
        self.port.setPlaceholderText("port : 10000")
        self.port.move(20,630)
        self.port.resize(300,30)

        self.run = QPushButton(self.window)
        self.run.setText("Run")
        self.run.move(20,690)
        self.run.resize(100,30)

        self.jobstate = QLabel(self.window)
        self.jobstate.setText("Job State :")
        self.jobstate.move(470,20)
        self.jobstate.resize(300,30)

        self.jobstateshow = QPlainTextEdit(self.window)
        self.jobstateshow.move(470,50)
        self.jobstateshow.resize(500,100)

        self.result = QLabel(self.window)
        self.result.setText("Result :")
        self.result.move(470,160)
        self.result.resize(300,30)

        self.resultshow = QPlainTextEdit(self.window)
        self.resultshow.move(470,200)
        self.resultshow.resize(500,500)
    
    def catchJobtype(self):
        jobtypeTxt = self.jobtype.currentText()
        with open("QEFILE.txt","w+") as filefd:
            filefd.write(jobtypeTxt)
            filefd.write("\n")
    
    def catchPoscar(self):
        poscarText = self.poscar.toPlainText()
        with open("QEFILE.txt","a") as filefd:
            filefd.write(poscarText)
            filefd.write("\n")

    def catchPseudo(self):
        pseudoText = self.pseudo.currentText()
        with open("QEFILE.txt","a") as filefd:
            filefd.write(pseudoText)
            filefd.write("\n")
    
    def catchKpoints(self):
        kpointsText = self.kpoints.toPlainText()
        with open("QEFILE.txt","a") as filefd:
            filefd.write(kpointsText)
            filefd.write("\n")

    def catchIp(self):
        self.IP = self.ip.toPlainText()

    def catchPort(self):
        self.PORT = self.port.toPlainText()

    def jobRun(self):
        self.run.clicked.connect(self.catchJobtype)
        self.run.clicked.connect(self.catchPoscar)
        self.run.clicked.connect(self.catchPseudo)
        self.run.clicked.connect(self.catchKpoints)
        self.run.clicked.connect(self.catchIp)
        self.run.clicked.connect(self.catchPort)
        self.run.clicked.connect(self.runSocket)

    def jobStateShow(self):
        pass

    def resultShow(self):
        pass

    def runSocket(self):
        fd = socket(AF_INET,SOCK_STREAM)
        fd.connect((self.IP,int(self.PORT)))
        with open("QEFILE.txt","r") as readfile:
            for tmp in readfile.readlines():
                fd.send(tmp.encode())
        fd.close()
        




if __name__ == '__main__':
    app =   QApplication([])

    jobgui = myWindow()

    jobgui.jobRun()

    jobgui.window.show()
    app.exec_()
