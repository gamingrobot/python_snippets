import httplib2
from urllib2 import urlopen
import urllib2
import string
from BeautifulSoup import BeautifulSoup, SoupStrainer
import time
import random


def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
    Uses a whitelist approach: any characters not present in valid_chars are
    removed. Also spaces are replaced with underscores.

    Note: this method may produce invalid filenames such as ``, `.` or `..`
    When I use this method I prepend a date string like '2009_01_15_19_46_32_'
    and append a file extension like '.txt', so I avoid the potential of using
    an invalid filename.

    """
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
    if filename == "":
        filename = "_"
    return filename

http = httplib2.Http()
url = raw_input("URL:")
status, response = http.request(url)

filelist = []

for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
    if link.has_key("href"):
        filelist.append(link['href'])

for filename in filelist:
    try:
        print "Opening %s" % filename
        remotefile = urlopen(url + filename)
        localfile = open(format_filename(filename), 'wb')
        localfile.write(remotefile.read())
        localfile.close()
        remotefile.close()
        print "Saved %s" % filename
    except urllib2.HTTPError, e:
        print 'failed' + filename
