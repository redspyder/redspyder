#! /user/bin/python

import MySQLdb as mdb
import sys
import subprocess

def reporter(student, assn):
	try:
		con = mdb.connect(host='mysql.cs.orst.edu', user='cs419_haroldl', passwd='8091', db='cs419_haroldl')
		cursor = con.cursor()
		cursor.execute("SELECT stage1, stage2, stage3 FROM Reports WHERE sid='%s' AND aid='%s'" % (student, assn))
		
		rows = cursor.fetchall()
		fd = open('report.txt','a')
		for itm in rows:
		    fd.write('---------------------------------------------------------------------------------------\n')
		    fd.write("Student: %s:\n" % student)
		    fd.write("Stage 1:\n")
		    fd.write("%s\n" % itm[0])
		    fd.write("Stage 2:\n")
		    fd.write("%s\n" % itm[1])
		    fd.write("Stage 3:\n")
		    fd.write("%s\n" % itm[2])
		    fd.write('---------------------------------------------------------------------------------------\n')

		fd.close()
		
	except (mdb.Error, IOError) as e:
		print "Error %d: %s" % (e.args[0], e.args[1])


reporter("jack", "HW2")
		
