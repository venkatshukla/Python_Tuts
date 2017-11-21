#!/usr/bin/env python

from selenium import webdriver
from xvfbwrapper import Xvfb

import unittest


class TestHomepages(unittest.TestCase):

    def setUp(self):
        self.vdisplay = Xvfb(width=1280, height=720)
        self.vdisplay.start()
        myProxy = "147.204.6.136:8080"
        proxy = Proxy({'proxyType': ProxyType.MANUAL,'httpProxy': myProxy,'ftpProxy': myProxy,'sslProxy': myProxy,'noProxy': '147.204.6.136:8080' # set this value as desired})
        self.browser = webdriver.Firefox()

    def testUbuntuHomepage(self):
        self.browser.get('http://www.ubuntu.com')
        self.assertIn('Ubuntu', self.browser.title)

    def tearDown(self):
        self.browser.quit()
        self.vdisplay.stop()


if __name__ == '__main__':
    unittest.main(verbosity=2)

