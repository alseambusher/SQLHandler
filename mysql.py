#!/usr/bin/env python
import MySQLdb
def mySQLtest():
#$connect=mysqli_connect("sql309.0fees.net","fees0_9989115","t92q7nrwh5kc","fees0_9989115_project")or die("cant connect");
	DB = 'fees0_9989115_project'
        DB_HOST = 'sql309.0fees.net'
        DB_USER = 'fees0_9989115'
        DB_PASSWORD = 't92q7nrwh5kc'
	#DB = 'project'
        #DB_HOST = 'localhost'
        #DB_USER = 'root'
        #DB_PASSWORD = 'alse'
	#DB = 'nitk10it_99k_nitk10it'
        #DB_HOST = 'nitk10it.99k.org'
        #DB_USER = '534988_nitk10it'
        #DB_PASSWORD = 'beautifulminds'
	try:
        	conn = MySQLdb.Connection(db=DB, host=DB_HOST, user=DB_USER,passwd=DB_PASSWORD)
        	cursor = conn.cursor()
		#count the num of rows int(cursor.rowcount)
        	sql = """show tables;"""
        	cursor.execute(sql)
        	results = cursor.fetchall()
        	cursor.close()
        	conn.close()
        	return results
	except e:
		print "%s"%e
		#return "cannot connect"
print mySQLtest()
