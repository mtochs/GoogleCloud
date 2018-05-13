from __future__ import print_function
from bs4 import BeautifulSoup
import pandas as pd
import requests
import xml.etree.ElementTree as ET
# Important function that converts text to speech with Google Cloud
from txt2mp3.txt2mp3 import synthesize_text

def remove_html_tags(text):
	# Removes html tags but might not remove extra white space
	return ''.join(ET.fromstring(text).itertext())

def remove_whitespace(text):
	return ' '.join(text.split())

def make_ssml(text):
	last_was_readmore = 0
	output = ['<speak>']
	for l in text.split("\n")[1:]:
		# Remove "Read More" notes at the end of entries
		if "Read more: " not in remove_whitespace(l):
			output.append(l)
			last_was_readmore = 0
		else:
			if last_was_readmore == 0:
					output.append('<break time="3s"/>')
					last_was_readmore = 1
	output.append('</speak>')
	return '\n'.join(output)

def cleanup(text):
	text = remove_html_tags(text)
	text = make_ssml(text)
	return text

def get_latest_import_ai():
	# Import AI Site
	import_ai = requests.get("https://jack-clark.net/")
	soup = BeautifulSoup(import_ai.content,'lxml')
	# Get latest date
	date = remove_whitespace(remove_html_tags(str(soup.find("abbr", {"class": "published"}))))
	# Get latest title
	title = remove_html_tags(str(soup.find("h3", {"class": "entry-title"})))
	# Get latest content
	content = cleanup(str(soup.find("div", {"class": "entry-content"})))
	
	return date, title, content

if __name__ == "__main__":
	date, title, content = get_latest_import_ai()
	print(content)


	#synthesize_text(content[0:5000], date + '.mp3')
	#print(content)