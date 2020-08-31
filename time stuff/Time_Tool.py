import pyttsx3, os, time
from datetime import datetime
import time
import threading

speak = pyttsx3.init()

time_start = round(time.time(), 2)


#to-do, replace datetime with time module completely!
def Speak_time():
	while True:
		now = datetime.now()
		if now.minute == 15 or now.minute == 45 or now.minute == 30:
			minutes = "The time is" + str(now.hour) + str(now.minute)
			speak.say(minutes)
			speak.runAndWait()
			time.sleep(19)

		elif now.minute == 0:
			minutes = "The time is" + str(now.hour)
			speak.say(minutes)
			speak.runAndWait()
			time.sleep(19)

		else:
			time.sleep(20)


def Time_elapsed():
	while True:
		time_elapsed = round(time.time(), 2) - time_start
		time_in_minutes = round(time_elapsed/60, 2)
		print (str(time_in_minutes) + "minutes")
		time.sleep(60)

#threading :D
t1 = threading.Thread(target = Speak_time,)
t2 = threading.Thread(target = Time_elapsed,)

t1.start()
t2.start()