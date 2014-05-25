import argparse
from bs4 import BeautifulSoup
import Queue
import urllib
import urllib2
import string
import sys
import threading
import time




hosts = ["http://www.amazon.com/CONVERSE-LEATHER-WHITE-135311C-WOMEN/dp/B007US08VG/ref=sr_1_1?ie=UTF8&qid=1401030488&sr=8-1&keywords=converse+red+leather+men",
         "http://www.amazon.com/Converse-Unisex-Taylor%C2%AE-Leather-Pepper/dp/B004TFO3YQ/ref=sr_1_2?ie=UTF8&qid=1401030488&sr=8-2&keywords=converse+red+leather+men",
         "http://www.amazon.com/Converse-Chuck-Taylor-Leather-Black/dp/B000BCN5OA/ref=sr_1_3?ie=UTF8&qid=1401030488&sr=8-3&keywords=converse+red+leather+men",
         "http://www.amazon.com/Converse-Mens-Basketball-Black-White/dp/B0036BQ8YM/ref=sr_1_4?ie=UTF8&qid=1401030498&sr=8-4&keywords=converse+red+leather+men"]
         

queue = Queue.Queue()
out_queue = Queue.Queue()

class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, queue, out_queue, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue
        self.name = name

    def run(self):
        self.time = time.time()
        print '%s started %s \n' % (self.name, self.time)
        while True:
            #grabs host from queue
            host = self.queue.get()

            #grabs urls of hosts and then grabs chunk of webpage
            user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:13.0) Gecko/20100101 Firefox/13.0'
            headers = { 'User-Agent' : user_agent }
            url = urllib2.urlopen(host)
            chunk = url.read()

            #place chunk into out queue
            self.out_queue.put(chunk)

            #signals to queue job is done
            self.queue.task_done()

class DatamineThread(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, out_queue, name):
        threading.Thread.__init__(self)
        self.out_queue = out_queue
        self.name = name

    def run(self):
        self.time = time.time()
        print '%s started %s \n' % (self.name, self.time)
        while True:
            #grabs host from queue
            chunk = self.out_queue.get()

            #parse the chunk and look for whatever tag/element you want
            #Item price for instance
            soup = BeautifulSoup(chunk)
            
            print soup.findAll(['title'])
            #TODO title = soup.find("span",{"id":"btAsinTitle"})
            #TODO price = unicode(soup.find("b",{"class":"priceLarge"}).string).strip()
           

            #signals to queue job is done
            self.out_queue.task_done()

start = time.time()
def main():

    #spawn a pool of threads, and pass them queue instance
    for i in range(5):
        name = 'ProcessThread%s' % i
        t = ThreadUrl(queue, out_queue, name)
        t.setDaemon(True)
        t.start()

    #populate queue with data
    for host in hosts:
        queue.put(host)

    for i in range(5):
        dname = 'DataThread%s' % i
        dt = DatamineThread(out_queue, dname)
        dt.setDaemon(True)
        dt.start()


    #wait on the queue until everything has been processed
    queue.join()
    out_queue.join()

main()
print "Elapsed Time: %s" % (time.time() - start)
