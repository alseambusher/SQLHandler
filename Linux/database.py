#!/usr/bin/env python
import MySQLdb
import config
import sys
#this class handles all kinds of mysql queries of non proxy type
class mysql():
	def __init__(self,DB_HOST=config.MYSQL_DB_HOST,DB_USER=config.MYSQL_DB_USER,DB_PASSWORD=config.MYSQL_DB_PASSWORD,DB=config.MYSQL_DB_DB):
		self.DB =DB
        	self.DB_HOST =DB_HOST
        	self.DB_USER =DB_USER
        	self.DB_PASSWORD =DB_PASSWORD
	def test_connection(self):
		try:
        		conn = MySQLdb.Connection(db=self.DB, host=self.DB_HOST, user=self.DB_USER,passwd=self.DB_PASSWORD)
			return True
		except:
			return False
	def query(self,query):
		try:
        		conn = MySQLdb.Connection(db=self.DB, host=self.DB_HOST, user=self.DB_USER,passwd=self.DB_PASSWORD)
        		cursor = conn.cursor()
        		cursor.execute(query)
			num_fields = len(cursor.description)
			field_names = [i[0] for i in cursor.description]
        		results = list(cursor.fetchall())
			#results.insert(num_fields,field_names)
			results.append(field_names)
        		cursor.close()
        		conn.close()
        		return results
		except MySQLdb.Error,e:
			return [["%s"%e.args[0],e.args[1]],['id','error']]
class SQLite():
	def __init__(self):
		print "SQLite not yet implemented"
