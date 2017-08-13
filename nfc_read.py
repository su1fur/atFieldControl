#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nfc
import time
import requests


def connected(tag):
  print tag.type
  print tag.identifier.encode("hex").upper()
  payload = {'key1': tag.identifier.encode("hex").upper()}
  requests.post("http://sulfur.work/", params=payload)
  time.sleep(3)
  clf.connect(rdwr={'on-connect': connected})

clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
