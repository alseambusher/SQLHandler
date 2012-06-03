#!/usr/bin/env python
import MySQLdb
#this class handles all kinds of mysql queries of non proxy type
class mysql_handler():
	def __init__(self,DB=None,DB_HOST=None,DB_USER=None,DB_PASSWORD=None):
		#self.DB = 'project'
        	#self.DB_HOST = 'localhost'
        	#self.DB_USER = 'root'
        	#self.DB_PASSWORD = 'alse'
		self.DB =DB
        	self.DB_HOST =DB_HOST
        	self.DB_USER =DB_USER
        	self.DB_PASSWORD =DB_PASSWORD
	def test_connection(self):
		try:
        		conn = MySQLdb.Connection(db=self.DB, host=self.DB_HOST, user=self.DB_USER,passwd=self.DB_PASSWORD)
			return True
		except:
			#return "%s"%e TODO make this alert the error and return false
			return False
	def query(self,query):
		try:
        		conn = MySQLdb.Connection(db=self.DB, host=self.DB_HOST, user=self.DB_USER,passwd=self.DB_PASSWORD)
        		cursor = conn.cursor()
        		cursor.execute(query)
        		results = cursor.fetchall()
        		cursor.close()
        		conn.close()
        		return results
		except e:
			print "%s"%e
