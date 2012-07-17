from PyQt4.QtCore import *
from PyQt4.QtGui import *
data= [['00','01','02'],
            ['10','11','12'],
            ['20','21','22']]

class tableGenerator(QWidget):
    def __init__(self,my_array=data,*args):
        QWidget.__init__(self, *args)

    def getTable(self,my_array=data):
    	if len(my_array)>0:
    		headers=my_array.pop()
	else:
		headers=[]
	self.list=QTreeWidget()
	self.list.setObjectName("table")
	for i in range(0,len(headers)):
		self.list.headerItem().setText(i,headers[i])
	for row in range(0,len(my_array)):
		item_0=QTreeWidgetItem(self.list)
		j=0
		for elements in my_array[row]:
			self.list.topLevelItem(row).setText(j,"%s"%elements)
			j+=1
	self.list.setSortingEnabled(True)
	self.list.setStyleSheet("font-size:12px")
	return self.list
