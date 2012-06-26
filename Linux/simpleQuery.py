from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import database
def simpleQuery(query):
	textbrowser=QTextBrowser()
	db=database.mysql_handler("project","localhost","root","alse")
	result=db.query(query)
	resultstr=""
	resultstr=resultstr.__add__("<table style='background-color:gray'>")
	for i in result:
		resultstr=resultstr.__add__("<tr>")
		for j in i:
			resultstr=resultstr.__add__("<td style='padding:5px'><a style='color:white'>%s</a></td>"%j)
		resultstr=resultstr.__add__("</tr>")
	resultstr=resultstr.__add__("</table>")
	textbrowser.append(resultstr)
	hbox=QHBoxLayout()
	hbox.addStretch(1)
	hbox.addWidget(textbrowser)
	return textbrowser
