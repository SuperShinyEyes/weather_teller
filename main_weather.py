
import sys

import alsaaudio, wave

import numpy as np

import psw
import gapi

import commands
import weather

speech = gapi.Speech('en-uk')

if len(sys.argv)==2:
	if sys.argv[1] in gapi.languages.keys():
		speech.lang = gapi.languages[sys.argv[1]]
	elif sys.argv[1] in gapi.languages.values():
		speech.lang = sys.argv[1]

def handler(fileName):
	global speech

	translator = gapi.Translator(speech.lang, 'en-uk')
	try:
		cfileName = psw.convert(fileName)
		city = speech.getText(cfileName)
		import os
		os.remove(fileName)
		os.remove(cfileName)
		if city!=None:
			city = city.lower()
			if len(city.strip())>0:
				print 'You said:',city
				w.update(city)
				print 'Status:', w.status
				print 'Temperature: %f celsius' % w.temp
				print 'Humidity: %d%%' % w.humidity
				print 'Wind: %fm/s, %ddegrees' % (w.wind[0], w.wind[1])


	except Exception, e:
		print "Unexpected error:", sys.exc_info()[0], e
	return True

w = weather.Weather()
mic = psw.Microphone()
print 'sampling...'
sample = np.array(mic.sample(200))
print 'done'

#import matplotlib.pyplot as plt
#plt.plot(sample)
#plt.show()
#from scipy import ndimage
#sample = ndimage.gaussian_filter(sample, sigma=3)
#plt.plot(sample)
#plt.show()

mic.listen(handler, sample.mean(), sample.std())
