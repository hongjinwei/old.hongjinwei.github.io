# -*- coding: utf-8 -*-

import json
import datetime
import sys,os
FILE = 'main.json'

def new_post(filename,postname,tag):

	try:
		f = open(FILE,'r')
	except Exception,e:
		print Exception,";",ex
		sys.exit(0)

	try:
		data = f.read()
	except Exception,e:
		print "read json file failed!"
		f.close()
		sys.exit(0)
	
	f.close()

	try:
		f = open(FILE,'w')
	except Exception,e:
		print Exception,";",ex
		sys.exit(0)

	json_data = json.loads(data)

	now = datetime.datetime.now()
	timeStr = now.strftime("%Y-%m-%d")
	postList = json_data.get("posts")

	new_info = {}	
	new_info['title'] = postname.decode('gbk').encode('utf-8')
	new_info['date'] = timeStr
	new_info['tags'] = tag.decode('gbk').encode('utf-8')
	new_info['path'] = filename
	new_info['num'] = len(postList);
	new_info['type'] = u"post"
	new_info['active'] = u"false"
	json_data.get("posts").append(new_info)
	
	data = json.dumps(json_data)
	print data
	f.write(data)
	f.close()
	


if __name__ == '__main__':
	
	try:
		#filename = sys.argv[0];
		#postname = sys.argv[1];
		filename = raw_input("Enter the html filename:")
		postname = raw_input("Enter the post name:")
		tag = raw_input("Give this post a tag:")
		print filename,postname,tag
	except Exception,e:
		print "Lack essential args!"
		sys.exit(0)
	
	PATH = "../"
	files = os.listdir(PATH)
	flag = 0
	for item in files:
		if filename in item:
			print "find this file!"
			flag = 1;
			break
	if(flag == 0):
		print "No file named" + filename + "found! \nexit"
		sys.exit(0)
	new_post(filename,postname,tag)


	
