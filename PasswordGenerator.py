from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random
import pyperclip
from PassGeneratorlowerandupper import Ui_MainWindow

class PassGeneratorMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.clear_btn.clicked.connect(self.clear_all)
        self.ui.generate_btn.clicked.connect(self.generate)
        self.ui.pushButton.clicked.connect(self.clipboard_copy)
        self.show()

    def clear_all(self):
        self.ui.lower.setChecked(False)
        self.ui.upper.setChecked(False)
        self.ui.check_num.setChecked(False)
        self.ui.check_syms.setChecked(False)
        self.ui.generated_pass.setText("")
        self.ui.pass_length.setText("")
        
    def clipboard_copy(self):
        if len(self.ui.generated_pass.toPlainText()) > 0:
            pyperclip.copy(self.ui.generated_pass.toPlainText())
        else:
            return







    def check(self):
        if ((self.ui.lower.isChecked() == False) and 
            (self.ui.upper.isChecked() == False) and
            (self.ui.check_num.isChecked()==False)and
            (self.ui.check_syms.isChecked()==False)):
            return False
         
        return True 

    def generate(self):
        if self.check() == True:
            cap_letters = 'ABCDEFGHIKJLMNOPQRSTVWXYZ'
            small_letters = cap_letters.lower()
            numbers = '0123456789'
            syms = '!.@#$%^&*()_+<>?|\/'



            chosen_types = ''
            if self.ui.upper.isChecked() == True:
                chosen_types += cap_letters 
            if self.ui.lower.isChecked() == True:
                chosen_types += small_letters

            if self.ui.check_num.isChecked() == True:
                chosen_types += numbers
            if self.ui.check_syms.isChecked() == True:
                chosen_types += syms    
            
            pass_length = int(self.ui.pass_length.toPlainText())
            first_char = random.choice(cap_letters + small_letters)
            rest_char = "".join(random.sample(chosen_types,pass_length ))
            password = first_char + rest_char
            self.ui.generated_pass.setText(password)

           
           

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    root= PassGeneratorMain()
    sys.exit(app.exec_())                            
    