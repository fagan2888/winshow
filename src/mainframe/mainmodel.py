#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
#   Copyright (C) 2014 Daniel Rodriguez
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
import win32api
import win32con
import win32gui

import utils.mvc as mvc

class HWndInfo(object):
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.titled = win32gui.GetWindowText(hwnd)
        self.enabled = win32gui.IsWindowEnabled(hwnd)
        self.iconized = win32gui.IsIconic(hwnd)
        self.visible = win32gui.IsWindowVisible(hwnd)

@mvc.DynamicModel
class MainModel(object):

    def __init__(self, hwnd, reload=False):
        self.hwnd = hwnd
        if reload:
            self.reload()
    
    @mvc.PubSend('mainmodel.hwndinfos')
    def reload(self):
        hwnds = list()
        def EnumWindowsCallBack(hwnd, extra):
            hwndinfo = HWndInfo(hwnd)
            hwnds.append(HWndInfo(hwnd)) # add for a set
            return True

        win32gui.EnumWindows(EnumWindowsCallBack, None)
        return hwnds

    def SetForeground(self, hwnds):
        for hwnd in hwnds:
            # win32gui.SetForegroundWindow(hwnd)
            win32gui.SetActiveWindow(hwnd)
    
    @mvc.PubSend('mainmodel.hwndshown')
    def Show(self, hwnds, action):
        for hwnd in hwnds:
            win32gui.ShowWindow(hwnd, action)
        self.reload()
        return hwnds

    def ShowNormal(self, hwnds):
        self.Show(hwnds, win32con.SW_NORMAL)

    def ShowRestore(self, hwnds):
        self.Show(hwnds, win32con.SW_RESTORE)

    def ShowMaximize(self, hwnds):
        self.Show(hwnds, win32con.SW_MAXIMIZE)

    def ShowMinimize(self, hwnds):
        self.Show(hwnds, win32con.SW_MINIMIZE)

    def ShowHide(self, hwnds):
        self.Show(hwnds, win32con.SW_HIDE)
