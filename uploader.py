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
		'8091', 'cs419_haroldl')
	
		cursor = con.cursor()
		cursor.execute("SELECT * FROM Report WHERE sid='%s' AND aid='%s'" % (student, assn))
		rows = cursor.fetchall()
	
		if len(rows) < 1:
			cursor.execute("INSERT INTO Report(sid, aid, %s) VALUES('%s','%s','%s')" % (stage,student, assn, mdb.escape_string(upload)))
		else:
			cursor.execute(("UPDATE Report SET %s = '%s' WHERE sid = '%s' AND aid = '%s'" % (stage, mdb.escape_string(upload), student, assn)))
		con.commit()
		
		cursor.close()
		
	except mdb.Error as e:
		print "Error %d: %s" % (e.args[0], e.args[1])

uploader("jack","HW2", "stage1", "stage1.out")		
"""
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

"""		
		
