#
# Copyright (C) 2014 Sean Poyser and Richard Dean (write2dixie@gmail.com)
#
#
#      Modified for tecbox Guide (02/2015 onwards)
#
# This Program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This Program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with XBMC; see the file COPYING. If not, write to
# the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# http://www.gnu.org/copyleft/gpl.html
#
import time
import os
import xbmc
import xbmcgui
import xbmcaddon

def deleteDB():
    try:
        xbmc.log("[script.geetvguide] Deleting guide data xml files...", xbmc.LOGDEBUG)
        dbPath1 = xbmc.translatePath(xbmcaddon.Addon(id = 'script.geetvguide').getAddonInfo('profile'))
        dbPath1 = os.path.join(dbPath1, 'guide.xml')

        delete_file(dbPath1)

        passed = not os.path.exists(dbPath1)

        if passed:
            xbmc.log("[script.geetvguide] Deleting data xml files...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.geetvguide] Deleting data xml files...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.geetvguide] Deleting data xml files...EXCEPTION', xbmc.LOGDEBUG)
        return False
		
def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1

if __name__ == '__main__':
    if deleteDB():
        d = xbmcgui.Dialog()
        d.ok('geetvguide', 'Deleted data files successfully completed.', 'Click OK to continue')
    else:
        d = xbmcgui.Dialog()
        d.ok('geetvguide', 'Deleting data files Failed.', 'files may be locked,', 'please restart Kodi and try again')

time.sleep(1)		
		
def deleteDB():
    try:
        xbmc.log("[script.geetvguide] Deleting guide data xml files...", xbmc.LOGDEBUG)
        dbPath2 = xbmc.translatePath(xbmcaddon.Addon(id = 'script.geetvguide').getAddonInfo('profile'))
        dbPath2 = os.path.join(dbPath2, 'guide.xml')

        delete_file(dbPath2)

        passed = not os.path.exists(dbPath2)

        if passed:
            xbmc.log("[script.geetvguide] Deleting guide data xml files...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.geetvguide] Deleting guide data xml files...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.geetvguide] Deleting guide data xml files...EXCEPTION', xbmc.LOGDEBUG)
        return False
		

def deleteDB():
    try:
        xbmc.log("[script.geetvguide] Deleting guide data xml files...", xbmc.LOGDEBUG)
        dbPath6 = xbmc.translatePath(xbmcaddon.Addon(id = 'script.geetvguide').getAddonInfo('profile'))
        dbPath6 = os.path.join(dbPath6, 'guide5.xml')

        delete_file(dbPath6)

        passed = not os.path.exists(dbPath6)

        if passed:
            xbmc.log("[script.geetvguide] Deleting guide data xml files...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.geetvguide] Deleting guide data xml files...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.geetvguide] Deleting guide data xml files...EXCEPTION', xbmc.LOGDEBUG)
        return False
		
def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1

if __name__ == '__main__':
    if deleteDB():
        d = xbmcgui.Dialog()
        d.ok('geetvguide', 'Deleted all guide data ', 'Please restart the guide to continue')
    else:
        d = xbmcgui.Dialog()
        d.ok('geetvguide', 'Deleting guide data xml files Failed.', 'files may be locked,', 'please restart XBMC and try again')
		
