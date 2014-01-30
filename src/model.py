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
from pubsub import pub
import win32api
import win32con
import win32gui
import wx

from mvcbase import ModelRole, PubSend

class HWndInfo(object):
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.titled = win32gui.GetWindowText(hwnd)
        self.enabled = win32gui.IsWindowEnabled(hwnd)
        self.iconized = win32gui.IsIconic(hwnd)
        self.visible = win32gui.IsWindowVisible(hwnd)

class ModelSetting(object):
    def __init__(self, defvalue):
        self.defvalue = defvalue
        self.icache = dict()

    def __get__(self, instance, owner=None):
        return self.icache.setdefault(instance, self.defvalue)

    def __set__(self, instance, value):
        self.icache[instance] = value
        instance.reload()

@ModelRole
class Model(object):

    checks = ['titled', 'enabled', 'iconized', 'visible']
    titled = ModelSetting(defvalue=wx.CHK_CHECKED)
    enabled = ModelSetting(defvalue=wx.CHK_CHECKED)
    visible = ModelSetting(defvalue=wx.CHK_CHECKED)
    iconized = ModelSetting(defvalue=wx.CHK_CHECKED)
    foreground = ModelSetting(defvalue=wx.CHK_UNCHECKED)
    selfforeground = ModelSetting(defvalue=wx.CHK_CHECKED)

    def __init__(self):
        pass

    @PubSend('hwndinfos')
    def reload(self):
        hwnds = list()
        def EnumWindowsCallBack(hwnd, extra):
            hwndinfo = HWndInfo(hwnd)

            hwnds.append(HWndInfo(hwnd)) # add for a set

            # If any check fails, it will be removed
            for check in self.checks:
                config = getattr(self, check)
                wininfo = getattr(hwnds[-1], check)

                if config == wx.CHK_UNDETERMINED:
                    continue

                if config == wx.CHK_CHECKED and not wininfo:
                    hwnds.pop(-1)
                    break

                if config == wx.CHK_UNCHECKED and wininfo:
                    hwnds.pop(-1)
                    break

            return True

        win32gui.EnumWindows(EnumWindowsCallBack, None)
        # pub.sendMessage('model.hwndinfos', msg=hwnds)
        return hwnds

    def Show(self, hwnds, action):
        for hwnd in hwnds:
            win32gui.ShowWindow(hwnd, action)
            if self.foreground:
                win32gui.SetForegroundWindow(hwnd)

        if self.selfforeground:
            win32gui.SetForegroundWindow(self.hwnd)
        self.reload()

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

    def SetForeground(self, hwnd):
        win32gui.SetForegroundWindow(hwnd)
