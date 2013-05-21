#! /user/bin/python

import MySQLdb as mdb
import sys
import subprocess
import os

def uploader(folder, student, assn, stage, upload_file):
	try:
		currentfolder = os.getcwd()
		os.chdir(folder)

		fd = open(upload_file)
		upload = fd.read()
		fd.close()
		os.chdir(currentfolder)
		
	except IOError, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)

	try:
		con = mdb.connect('mysql.cs.orst.edu', 'cs419_haroldl',
		'8091', 'cs419_haroldl')
	
		cursor = con.cursor()
		cursor.execute("SELECT * FROM Reports WHERE sid='%s' AND aid='%s'" % (student, assn))
		rows = cursor.fetchall()
		if len(rows) < 1:
			cursor.execute("INSERT INTO Reports(sid, aid, %s) VALUES('%s','%s','%s')" % (stage,student, assn, mdb.escape_string(upload)))
		else:
			cursor.execute(("UPDATE Reports SET %s = '%s' WHERE sid = '%s' AND aid = '%s'" % (stage, mdb.escape_string(upload), student, assn)))
		con.commit()
		
		cursor.close()
		
	except mdb.Error as e:
		print "Error %d: %s" % (e.args[0], e.args[1])

#uploader("jack","HW2", "stage1", "stage1.out")		

