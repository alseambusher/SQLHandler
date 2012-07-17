#!/usr/bin/env python
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from tabs import *
import tableGenerator
from database import *
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__();
		self.db=mysql()
		self.initUi()
		self.resize(800,600)
		self.center()
		self.setWindowState(Qt.WindowMaximized)
	def openDock(self,tool="databases"):
		logDockWidget=QDockWidget(self)
		logDockWidget.setObjectName("LogDockWidget")
		logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
		#self.databases=tableGenerator.tableGenerator()
		#select_db=self.databases.getTable(self.db.query("show databases"))
		logDockWidget.setMinimumWidth(300)
		logDockWidget.setWidget(tableGenerator.dbList())

		self.addDockWidget(Qt.LeftDockWidgetArea,logDockWidget)

	def initUi(self):
		#exitAction=QAction(QIcon('../widget.png'),'&Exit',self)
		exitAction=QAction('&Exit',self)
		exitAction.setShortcut("Alt+F4")
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(qApp.quit)

		showDock=QAction("Show &Dock",self)
		showDock.setStatusTip("Show Dock")
		showDock.triggered.connect(self.openDock)

		#frames
		topleft=QFrame(self)
		topright=QFrame(self)
		bottom=QFrame(self)
		topleft.setFrameShape(QFrame.StyledPanel)
		topright.setFrameShape(QFrame.StyledPanel)
		bottom.setFrameShape(QFrame.StyledPanel)
		self.splitter1=QSplitter(Qt.Horizontal)
		#self.splitter1.addWidget(topleft)
		self.browser=QTextBrowser()
		self.splitter1.addWidget(self.browser)
		#self.splitter1.addWidget(topright)
		#self.splitter1.addWidget(simpleQuery.simpleQuery("select*from user_info"))
		self.splitter2=QSplitter(Qt.Vertical)
		self.splitter2.addWidget(self.splitter1)
		self.splitter2.addWidget(bottom)
		self.setCentralWidget(self.splitter2)

		#Menu bar
		menubar=self.menuBar()
		filemenu=menubar.addMenu("&File")
		filemenu.addAction(exitAction)
		tools=menubar.addMenu("&Tools")
		tools.addAction(showDock)
		self.openDock()#by default databases dock is opened

		self.toolbar=self.addToolBar("tool");
		self.toolbar.addAction(exitAction)

		self.statusBar().showMessage("Status Message");

		#tabs
		self.newTab=tabClass()
		self.setCentralWidget(self.newTab.tab)
		
		self.setGeometry(300,300,250,150)
		self.setWindowTitle("SQLmate")
		self.show()
	def center(self): 
        	screen = QDesktopWidget().screenGeometry() 
        	size = self.geometry() 
        	self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2) 


def main():
	app=QApplication(sys.argv)
	ex=MainWindow()
	sys.exit(app.exec_())

#if __name__=='__main__':
	#main()
main()

