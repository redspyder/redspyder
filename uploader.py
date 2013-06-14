#! /user/bin/python

import MySQLdb as mdb
import sys
import subprocess
import os

def uploader(folder, student, assn, stage, upload_file, status):
	try:
		currentfolder = os.getcwd()
		os.chdir(folder)
		if os.path.isfile(upload_file):
			fd = open(upload_file)
			upload = fd.read()
			fd.close()
		else:
			upload = "No Output File"
		os.chdir(currentfolder)
		
	except IOError, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)

	try:
		con = mdb.connect('mysql.cs.orst.edu', 'cs419_haroldl','8091', 'cs419_haroldl')
		stagestatus = 'status' + stage[-1:]
		cursor = con.cursor()
		cursor.execute("SELECT * FROM Reports WHERE sid='%s' AND aid='%s'" % (student, assn))
		rows = cursor.fetchall()
		if len(rows) < 1:
			cursor.execute("INSERT INTO Reports(sid, aid, %s, %s) VALUES('%s','%s','%s', '%s')" % (stage,stagestatus, student, assn, mdb.escape_string(upload), status))
		else:
			cursor.execute(("UPDATE Reports SET %s = '%s', %s = '%s' WHERE sid = '%s' AND aid = '%s'" % (stage, mdb.escape_string(upload), stagestatus, status, student, assn)))
		con.commit()
		
		cursor.close()
		
	except mdb.Error as e:
		print "Error %d: %s" % (e.args[0], e.args[1])


