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
        xbmc.log("[script.geetvguide] Deleting Guide listing Choices...", xbmc.LOGDEBUG)
        dbPath = xbmc.translatePath(xbmcaddon.Addon(id = 'script.geetvguide').getAddonInfo('profile'))
        dbPath = os.path.join(dbPath, 'guides.ini')

        delete_file(dbPath)

        passed = not os.path.exists(dbPath)

        if passed:
            xbmc.log("[script.geetvguide] Deleting Guide listing Choices...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.geetvguide] Deleting Guide listing Choices...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.geetvguide] Deleting Guide listing Choices...EXCEPTION', xbmc.LOGDEBUG)
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
        d.ok('geetvguide', 'Deleting Guide listing Choices has been successfully deleted.', 'It will be re-created next time you start the guide')
    else:
        d = xbmcgui.Dialog()
        d.ok('geetvguide', 'Failed to delete Guide listing Choices.', 'File may be locked,', 'please restart Kodi and try again')