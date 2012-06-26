from PyQt4.QtCore import *
from PyQt4.QtGui import *
from database import *
from tableGenerator import *
import sys
class tabClass():
	def __init__(self):
		self.db=mysql(DB="alse")
		self.tab=QTabWidget()
		STRUCTURE=QWidget()
		BROWSE=QWidget()
		SQL=QWidget()
		SEARCH=QWidget()
		QUERY=QWidget()
		EXPORT=QWidget()
		IMPORT=QWidget()
		OPERATIONS=QWidget()
		#to add widgets tab_structure.addWidget() can be used
		#self.tab_structure=tabs.structure(STRUCTURE)
		#self.tab_browse=tabs.browse(BROWSE)
		self.tab_sql=QVBoxLayout(SQL)
		self.tab_sql.addLayout(self.sql())
		#self.tab_search=tabs.search(SEARCH)
		#self.tab_query=tabs.query(QUERY)
		#self.tab_export=tabs.exportSql(EXPORT)
		#self.tab_import=tabs.importSql(IMPORT)
		#self.tab_operations=tabs.operations(OPERATIONS)

		self.tab.addTab(STRUCTURE,"Structure")
		self.tab.addTab(BROWSE,"Browse")
		self.tab.addTab(SQL,"SQL")
		self.tab.addTab(SEARCH,"Search")
		self.tab.addTab(QUERY,"Query")
		self.tab.addTab(EXPORT,"Export")
		self.tab.addTab(IMPORT,"Import")
		self.tab.addTab(OPERATIONS,"Operations")
	def structure(self):
		widget=QVBoxLayout(tab)
		return widget
	def browse(self):
		widget=QVBoxLayout(tab)
		return widget
	def sql(self):
		widget=QVBoxLayout()
		self.sqlQuery=QTextEdit()
		self.submitQuery=QPushButton("Execute")
		self.clearQuery=QPushButton("Clear")
		self.table=tableGenerator(self.db.query("show tables"))
		self.submitQuery.clicked.connect(self.sqlResult)
		self.clearQuery.clicked.connect(self.sqlQuery.clear)
		buttonLayout=QHBoxLayout()
		buttonLayout.addWidget(self.submitQuery)
		buttonLayout.addWidget(self.clearQuery)
		widget.addWidget(self.sqlQuery)
		self.resultTable=self.table.getTable([])
		widget.addLayout(buttonLayout)
		return widget
	def sqlResult(self):
		result=self.db.query(unicode(self.sqlQuery.toPlainText()))
		self.tab_sql.removeWidget(self.resultTable)
		if result!=():
			self.resultTable=self.table.getTable(result)
		else:
			self.resultTable=self.table.getTable(['query did not return anything'])
		self.tab_sql.addWidget(self.resultTable)
	def search(self):
		widget=QVBoxLayout(tab)
		return widget
	def query(self):
		widget=QVBoxLayout(tab)
		return widget
	def exportSql(self):
		widget=QVBoxLayout(tab)
		return widget
	def importSql(self):
		widget=QVBoxLayout(tab)
		return widget
	def operations(self):
		widget=QVBoxLayout(tab)
		return widget
