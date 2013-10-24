"""
dumpimages.py
    Downloads all the images on the supplied URL, and saves them to the
    specified output file ("/test/" by default)

Usage:
    python dumpimages.py http://example.com/ [output]
"""

from BeautifulSoup import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys
import urllib
import uuid
def main(url, out_folder="/home/piyush/test/"):
    """Downloads all the images at 'url' to /test/"""
    soup = bs(url)
    sensor = 0
    for image in soup.findAll("img"):
        print "Image: %s" % image['src']
        filename = out_folder +  str(uuid.uuid4()) + '.png'
        outpath = os.path.join(out_folder, filename)
        print "outpath",outpath, 'image', image['src']
        url_location = 'http://www.example.in' + image['src'] if image['src'].startswith('/') else image['src']
	print "url_location",url_location
	url_location = url_location.replace(',','')
        url_location = urllib.unquote_plus(url_location)
	if url_location:
	    sensor = url_location.rfind('sensor')
	    if sensor == -1:
	        url_location = url_location + '&sensor=false'

        u = urllib.urlopen(url_location)
        f = open(outpath ,'w')
	f.write(u.read())
	f.close()       

def _usage():
    print "usage: python dumpimages.py http://example.com [outpath]"

if __name__ == "__main__":
    url = sys.argv[-1]
    out_folder = "/home/piyush/test/"
    print url
    f = open(url,'r')
    main(f.read(), out_folder)
    f.close()
