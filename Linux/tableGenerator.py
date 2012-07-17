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
	#item.addChild(item2)
	#self.list.addTopLevelItem(item)
	self.list.setSortingEnabled(False)
	self.list.setStyleSheet("font-size:12px")
	return self.list

#this returns the database list for dockWidget
def dbList():

	list=QTreeWidget()
	list.setObjectName("table")
	list.headerItem().setText(0,"Databases")

	from database import *
	db=mysql()
	databases=db.query("show databases")
	databases.pop()
	for row in range(0,len(databases)):
		item_0=QTreeWidgetItem(list)
		list.topLevelItem(row).setText(0,"%s"%databases[row][0])

		db.DB=databases[row][0]
		tables=db.query("show tables")
		tables.pop()
		for children in range(0,len(tables)):
			child=QTreeWidgetItem(["%s"%tables[children][0]])
			item_0.addChild(child)
	list.setSortingEnabled(False)
	list.setStyleSheet("font-size:12px")
	return list
