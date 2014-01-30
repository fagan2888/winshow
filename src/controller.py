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
from mvcbase import MvcRole, PubSubscribe, ViewManager

@MvcRole('controller')
class Controller(object):

    def __init__(self):
        pass

    @PubSubscribe('OnInit')
    def OnViewInit(self, msg):
        self._model.hwnd = self._view.GetHandle()

        defconfig = dict()
        deffields = ['titled', 'visible', 'iconized', 'enabled', 'foreground', 'selfforeground']
        for field in deffields:
            defconfig[field] = getattr(self._model, field)
        self._view.DefConfig(defconfig)
        self._model.reload()

    @ViewManager
    def OnButtonClickGetWindows(self, event):
        event.Skip()
        self._model.reload()

    @ViewManager
    def OnCheckBoxTitled(self, event):
        event.Skip()
        self._model.titled = event.GetInt()

    @ViewManager
    def OnCheckBoxVisible(self, event):
        event.Skip()
        self._model.visible = event.GetInt()

    @ViewManager
    def OnCheckBoxEnabled(self, event):
        event.Skip()
        self._model.enabled = event.GetInt()

    @ViewManager
    def OnCheckBoxIconized(self, event):
        event.Skip()
        self._model.iconized = event.GetInt()

    @ViewManager
    def OnCheckBoxForeground(self, event):
        event.Skip()
        self._model.foreground = event.GetInt()

    @ViewManager
    def OnCheckBoxSelfForeground(self, event):
        event.Skip()
        self._model.selfforeground = event.GetInt()

    @ViewManager
    def OnButtonClickShow(self, event):
        event.Skip()
        hwnds = self._view.GetSelectedHwnds()
        self._model.ShowNormal(hwnds)

    @ViewManager
    def OnButtonClickRestore(self, event):
        event.Skip()
        hwnds = self._view.GetSelectedHwnds()
        self._model.ShowRestore(hwnds)

    @ViewManager
    def OnButtonClickMaximize(self, event):
        event.Skip()
        hwnds = self._view.GetSelectedHwnds()
        self._model.ShowMaximize(hwnds)

    @ViewManager
    def OnButtonClickMinimize(self, event):
        event.Skip()
        hwnds = self._view.GetSelectedHwnds()
        self._model.ShowMinimize(hwnds)

    @ViewManager
    def OnButtonClickHide(self, event):
        event.Skip()
        hwnds = self._view.GetSelectedHwnds()
        self._model.ShowHide(hwnds)
