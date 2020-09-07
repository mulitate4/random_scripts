from notify_run import Notify
import sys

notify = Notify()

if sys.argv > 1:
	msg = sys.argv[1:]

else:
	print ("Enter msg")
	msg = input()

notify.send(msg)