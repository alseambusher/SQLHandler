from __future__ import division
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import subprocess
from math import *
class Form(QDialog):
	def __init__(self,parent=None):
		super(Form,self).__init__(parent)
		self.browser=QTextBrowser()
		self.lineedit=QLineEdit("type command and press Enter")
		self.lineedit.selectAll()
		layout=QBoxLayout(QBoxLayout.BottomToTop)
		layout.addWidget(self.browser)
		layout.addWidget(self.lineedit)
		self.setLayout(layout)
		self.lineedit.setFocus()
		self.connect(self.lineedit,SIGNAL("returnPressed()"),self.updateUi)
		self.setWindowTitle("Shell")
	def updateUi(self):
		if unicode(self.lineedit.text())=="clear":
			self.browser.setText("")
		elif unicode(self.lineedit.text())=="exit":
			exit()
		else:
			text=subprocess.Popen(unicode(self.lineedit.text()),shell=True,stdout=subprocess.PIPE)
			EOC="success"
			for i in text.stdout.readlines():
				EOC="~~~~~~~~~~~"
				self.browser.append("%s"%i.strip())
			self.browser.append(EOC)
		self.lineedit.setText("")
		#try:
			#text=unicode(self.lineedit.text())
			#self.browser.append("%s=<b>%s</b>"%(text,eval(text)))
		#except:
			#self.browser.append("<font color=red>%s is invalid</font>"%text)
app=QApplication(sys.argv)
form=Form()
form.show()
app.exec_()
