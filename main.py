import playfair
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

qtCreatorFile = "playFair.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class GUICKO(QMainWindow, Ui_MainWindow):  
    
    error = "error"
    varovanie = "Dlzka kluca musi byt minimalne 8 znakov"
    def default(self):
        self.kluc.setText('Playfair')
        self.vstupnyText.setText('Ahoj')
        

    def encryption(self):
        try:
            kluc = self.kluc.toPlainText()
            if len(kluc) < 8:
                self.kluc.setText(self.varovanie)
            else:
                self.sifrovanyText.setText(playfair.sifruj(self.vstupnyText.toPlainText(),kluc))
        except:
            self.sifrovanyText.setText(self.error)
    def decryption(self):
        try:
            kluc = self.kluc.toPlainText()
            if len(kluc) < 8:
                self.kluc.setText(self.varovanie)
            else:
                desifrovany = playfair.desifruj(self.sifrovanyText.toPlainText(),kluc)
                self.desifrovany.setText(desifrovany)
        except:
            self.sifrovanyText.setText(self.error)

    def tabulka(self):
        try:
            kluc = self.kluc.toPlainText()
            if len(kluc) < 8:
                self.kluc.setText(self.varovanie)
            else:
                self.Tabulka.setText(str(playfair.matrixGener(kluc)))
        except:
             self.sifrovanyText.setText(self.error)

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.sifruj.clicked.connect(self.encryption)
        self.desifruj.clicked.connect(self.decryption)
        self.generuj.clicked.connect(self.tabulka)
        self.default()
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUICKO()
    window.show()
    sys.exit(app.exec_())