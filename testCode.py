
# coding=utf-8
import re
import datetime
import itertools
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool

def test():
	print "Œ¥’“µΩcooick!"


test();

'''from selenium import webdriver 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
#driver = webdriver.Chrome('C:\Program Files\Internet Explorer\iexplore.exe') 
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
                "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
            ) 
browser = webdriver.PhantomJS(desired_capabilities=dcap)
browser.get('http://qzone.qq.com/')
'''