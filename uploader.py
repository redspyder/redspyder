#! /user/bin/python

import MySQLdb as mdb
import sys
import subprocess

def uploader(student, assn, stage, upload_file):
	try:
		fd = open(upload_file)
		upload = fd.read()
		fd.close()
		
	except IOError, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)

	try:
		con = mdb.connect('mysql.cs.orst.edu', 'cs419_haroldl',
		'8091', 'group6_db')
	
		cursor = con.cursor()
		cursor.execute("SELECT * FROM Reports WHERE sid='student' AND aid='assn'")
		numrows = cursor.rowcount
		if rowcount < 1:
			cursor.execute("INSERT INTO Reports ('%s') VALUES('%s')\
                        WHERE sid = '%s' AND aid = '%s'" %
                        mdb.escape_string(stage), mdb.escape_string(upload),
                        student, assn)
		else:
			cursor.execute("UPDATE Reports SET '%s' = '%s'\
                        WHERE sid = '%s' AND aid = '%s'" %
                        mdb.escape_string(stage), mdb.escape_string(upload),
                        student, assn)
		con.commit()
		
		cursor.close()
		
	except mdb.Error as e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		

def reporter(student, assn):
	try:
		con = mdb.connect(host='mysql.cs.orst.edu', user='cs419_haroldl',
			passwd='8091', db='group6_db')
			
		cursor = con.cursor
		
		cursor.execute("SELECT stage1, stage2, stage3, stage4 FROM Reports\
		WHERE sid='student', and aid='assn' DESC")
		
		numrows = cursor.rowcount
		row = cursor.fetchone()
		
		fd = open('report.txt','a')
		
		for col in row:
				fd.write("%s\n" % col)
				fd.write('------------------------------------------------\
					---------------------------------------')
		
	except (mdb.Error, IOError) as e:
		print "Error %d: %s" % (e.args[0], e.args[1])
