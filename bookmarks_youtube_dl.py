#!/usr/bin/env python3
# -*- coding: utf-8 -*-
  
from __future__ import unicode_literals
import json
import youtube_dl
 
def retrieve_urls(filename, folder="Musics"):
	"""Return a list of retrieved youtube urls.

    Keyword arguments:
    filename -- the bookmarks json file exported from chrome
    folder -- the folder containing the videos (default "Musics")
    """
	data = {}
	youtube_urls = []
	url_length = len("https://www.youtube.com/watch?v=iy7mmbdau-g")
	with open(filename, encoding="utf8") as f:
		data = json.load(f)
	for bookmark in data['roots']['bookmark_bar']['children']:
		if 'children' in bookmark and bookmark['name'] == 'Musics':
			for url in bookmark['children']:
				youtube_urls.append(url['url'][:url_length])
	return youtube_urls

def download_videos(urls):
	"""Download videos from the given list
	
	Keyword arguments:
    urls -- the list of url to be downloaded
    """
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(urls)
 
def main():
	urls = retrieve_urls("bookmarks.json")
	download_videos(urls);
 
if __name__ == "__main__":
	main()