#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import sys
from socket import gethostname
from collections import deque

# configure GPIO pin here
gpio_port = 12

GPIO.setmode(GPIO.BOARD) # use RaspPi board layout pin numbering
GPIO.setup(gpio_port, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0

# needed for collectd
hostname = gethostname()

# output interval
interval = 10

count_history = deque([0,0],60/interval)

def tube_impulse_callback(channel):
    global counter
    counter+=1

GPIO.add_event_detect(gpio_port, GPIO.FALLING, callback=tube_impulse_callback)

try:
    while True:
        count_history.appendleft(counter)
	cpm = count_history[0] - count_history[-1]
        time.sleep(interval)
        print "PUTVAL \"%s/exec-geigercounter/geiger_CPS-cps\" interval=%d N:%d" % (hostname,interval,counter)
        print "PUTVAL \"%s/exec-geigercounter/geiger_CPM-cpm\" interval=%d N:%d" % (hostname,interval,cpm)
	sys.stdout.flush()
except:
    GPIO.cleanup()

