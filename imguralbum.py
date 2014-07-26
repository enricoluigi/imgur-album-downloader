# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
import os
import math
import sys



def gettitle(url):
    print (url)

    tmpfile = open("tmp.txt",'w+')
    page = urllib.urlopen(url).read()
    tmpfile.write(page)
    tmpfile.close()

    with open('tmp.txt') as f:
        for line in f:
            if re.match('(.*) - Imgur</title>(.*)',line):
                line = line.split(" - ")
                line = line[0].split("    ")
                line = line[1].decode('utf-8')
                return line
                
b = 1

def getalbums():
    with open('myfile.txt') as f:
        for line in f:
            if re.match('(.*)image-list-link"(.*)',line):
                line = line.split('/')
                line = line[3].split('"')

                album = ['http://imgur.com/a/',''.join(line[0])]
                album = ''.join(album)
                print (album)
                titulo = gettitle(album)
                try:
                    downloader = ImgurAlbumDownloader(album)
                    print ("This album has %d images" % downloader.num_images())
                    downloader.save_images(titulo)
                    #downloader.save_images()
                except:
                    print ("Ops")


getalbums()

