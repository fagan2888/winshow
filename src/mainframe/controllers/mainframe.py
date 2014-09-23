#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
################################################################################
# 
#  Copyright (C) 2014 Daniel Rodriguez
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from .. import aboutdialog
from utils.mvc import DynBind

if True:

    @DynBind.EVT_CHECKBOX.CheckBox.Enabled
    @DynBind.EVT_CHECKBOX.CheckBox.Iconized
    @DynBind.EVT_CHECKBOX.CheckBox.Foreground
    @DynBind.EVT_CHECKBOX.CheckBox.SelfForeground
    @DynBind.EVT_CHECKBOX.CheckBox.Visible
    @DynBind.EVT_CHECKBOX.CheckBox.Titled
    @DynBind.EVT_BUTTON.BUTTON.GetWindows
    def OnButtonClickGetWindows(self, event):
        event.Skip()
        self.model.reload()

    @DynBind.EVT_BUTTON.Button.Show
    def OnButtonClickShow(self, event):
        event.Skip()
        hwnds = self.view.GetSelectedHwnds()
        self.model.ShowNormal(hwnds)

    @DynBind.EVT_BUTTON.Button.Restore
    def OnButtonClickRestore(self, event):
        event.Skip()
        hwnds = self.view.GetSelectedHwnds()
        self.model.ShowRestore(hwnds)

    @DynBind.EVT_BUTTON.Button.Maximize
    def OnButtonClickMaximize(self, event):
        event.Skip()
        hwnds = self.view.GetSelectedHwnds()
        self.model.ShowMaximize(hwnds)

    @DynBind.EVT_BUTTON.Button.Minimize
    def OnButtonClickMinimize(self, event):
        event.Skip()
        hwnds = self.view.GetSelectedHwnds()
        self.model.ShowMinimize(hwnds)

    @DynBind.EVT_BUTTON.Button.Hide
    def OnButtonClickHide(self, event):
        event.Skip()
        hwnds = self.view.GetSelectedHwnds()
        self.model.ShowHide(hwnds)

if True:
    @DynBind.EVT_BUTTON.Button.About
    def OnEventAboutDialog(self, event):
        event.Skip()
        dialog = aboutdialog.AboutDialog(self)
        dialog.ShowModal()
