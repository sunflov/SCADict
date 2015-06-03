from PyQt4 import QtCore, QtGui

class SCADictMain(QtGui.QWidget):
    def __init__(self, parent = None):
        super(SCADictMain, self).__init__(parent)

        qinput = QtGui.QLineEdit()
        qbutton = QtGui.QPushButton('Query')

        splitter = QtGui.QSplitter(parent)
        treeview = QtGui.QTreeView()
        textedit = QtGui.QTextEdit()
        splitter.addWidget(treeview)
        splitter.addWidget(textedit)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(qinput)
        layout.addWidget(qbutton)
        
        vlayout = QtGui.QVBoxLayout()
        vlayout.addLayout(layout)
        vlayout.addWidget(splitter)
        
        self.setLayout(vlayout)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    scadictmain = SCADictMain()
    scadictmain.show()
    sys.exit(app.exec_())
