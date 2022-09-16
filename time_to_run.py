from datetime import datetime as dt

RUN = True

while RUN:
	if dt(dt.now().year,dt.now().month,dt.now().day,18,30) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18,34):
		print("Working")
	else:
		RUN = False
		print("Done!!!")

# updateing something
# new changes happned..!