"""
Changes background of Mac.

Predecessor here: https://gist.github.com/swehrwein/d6aa922505c4e5f21f2f
"""
import appscript

def change_background(path):
	"""
	Changes background of Mac.
	Input: path to image to which the background should change
	"""
	se = appscript.app('System Events')
	desktops = se.desktops.display_name.get()
	for d in desktops:
	    desk = se.desktops[appscript.its.display_name == d]
	    desk.picture.set(appscript.mactypes.File(path))