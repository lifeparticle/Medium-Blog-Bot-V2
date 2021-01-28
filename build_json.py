import os
import re
import sys
import json
import pathlib
import requests

def compare_data(oldData, newData):
	data = []
	last_pub_date = oldData[-1]['pubDate']
	for nD in newData:
		if nD['pubDate'] > last_pub_date:
			data.insert(0, {"title": nD['title'], "link": nD['link'], "pubDate": nD['pubDate']})
		else:
			break
	return data

def read_json_file(filename):
	jsonFile = open(filename, "r")
	data = json.load(jsonFile)
	jsonFile.close()
	return data

def modify_json_file(filename, oldData, data):
	for d in data:
		oldData.append(d)
	jsonFile = open(filename, "w+")
	jsonFile.write(json.dumps(oldData, indent=4))
	jsonFile.close()

def fetch_blog_posts(link):
	result = []
	response = requests.get(link)
	if response.status_code == 200:
		posts = json.loads(response.text)["items"]
		for post in posts:
			# skip the comments
			if len(post["categories"]) != 0:
				result.append(post)
	elif response.status_code == 404:
		print('Not Found: ') + link
	return result

if __name__ == "__main__":
	filename = "blog_links.json"
	username = "@lifeparticle"
	blog_link = "https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/"+username

	newData = fetch_blog_posts(blog_link)
	oldData = read_json_file(filename)
	data = compare_data(oldData, newData)
	modify_json_file(filename, oldData, data)