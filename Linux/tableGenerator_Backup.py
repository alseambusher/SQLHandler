from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import datetime
import operator
data= [['00','01','02'],
            ['10','11','12'],
            ['20','21','22']]

class tableGenerator(QWidget):
    def __init__(self,my_array=data,*args):
        QWidget.__init__(self, *args)

        #self.tablemodel = MyTableModel(my_array, self)
        #self.tableview = QTableView()
        #self.tableview.setModel(self.tablemodel)

    def getTable(self,my_array=data):
    	if len(my_array)>0:
    		headers=my_array.pop()
	else:
		headers=[]
        self.tablemodel = MyTableModel(my_array,headers,self)
        self.tableview = QTableView()
	self.tableview.setStyleSheet("font-size:12px")
        self.tableview.setModel(self.tablemodel)
	self.tableview.resizeColumnsToContents()
	#self.tableview.resizeRowsToContents()
	self.tableview.setSortingEnabled(True)
	QObject.connect(self.tableview,SIGNAL("clicked(QModelIndex)"),self.cellClicked)
    	return self.tableview
    def cellClicked(self,qmodelIndex):
    	#print qmodelIndex.column()
	#print qmodelIndex.row()
    	#print qmodelIndex.data(Qt.DisplayRole).toString()
	print self.tablemodel.arraydata[qmodelIndex.row()]

class MyTableModel(QAbstractTableModel):
    def __init__(self, datain,headerdata,parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
	self.headerdata=headerdata
    def rowCount(self, parent):#sets number of rows
        return len(self.arraydata)

    def columnCount(self, parent):#sets number of columns
        return len(self.arraydata[0])

    def data(self, index, role):#this will set values
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
	if type(self.arraydata[index.row()][index.column()]) is datetime.datetime:
	    return QVariant(self.arraydata[index.row()][index.column()].strftime("%d-%m-%Y %H:%M:%S"))
        return QVariant(self.arraydata[index.row()][index.column()])
    def headerData(self, section, orientation, role):#this will set headers
	if orientation == Qt.Horizontal and role == Qt.DisplayRole:
	    return QVariant(self.headerdata[section])
	if orientation == Qt.Vertical and role == Qt.DisplayRole:
	    return QVariant(section+1)
	return QVariant()
    def sort(self,Ncol,order):
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))
