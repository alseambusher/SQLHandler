#!/usr/bin/env python
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import simpleQuery
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__();
		self.initUi()
		self.resize(800,600)
		self.setWindowState(Qt.WindowMaximized)
	def openDock(self):
		logDockWidget=QDockWidget("Databases",self)
		logDockWidget.setObjectName("LogDockWidget")
		logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)

		self.listWidget=QListWidget()
		logDockWidget.setWidget(self.listWidget)

		self.browser=QTextBrowser()
		logDockWidget.setWidget(self.browser)

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
		self.splitter1.addWidget(simpleQuery.simpleQuery("select*from user_info"))
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
		self.openDock()

		self.toolbar=self.addToolBar("tool");
		self.toolbar.addAction(exitAction)

		self.statusBar().showMessage("Status Message");
		self.setGeometry(300,300,250,150)
		self.setWindowTitle("SQLmate")
		self.show()

def main():
	app=QApplication(sys.argv)
	ex=MainWindow()
	sys.exit(app.exec_())

#if __name__=='__main__':
	#main()
main()

