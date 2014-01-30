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
import flushfile

import wx

from mvcbase import MvcContainer
from controller import Controller
from mainframe import MainFrame
from model import Model

@MvcContainer
class MainApp(wx.App):
    def OnInit(self):
        wx.Log_SetActiveTarget(wx.LogStderr())
        # wx.Log_SetActiveTarget(wx.LogBuffer())

        self._model = Model()
        self._controller = Controller()
        self._view = MainFrame(None)

        self.SetTopWindow(self._view)
        self._view.Show(True)
        return True

    def GetAppname(self):
        return 'winshow'

    def GetVendorName(self):
        return 'winshow'

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()

