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
import itertools
import utils.mvc as mvc
import wx

if True:
    def __init__(self, *args, **kwargs):
        # Get a fixed point size font and set it for the control
        # self.font = wx.Font(8, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.font = wx.Font(8, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Lucida Sans')
        self.m_listCtrlWins.SetFont(self.font)

        # Operating System Details for column sizes
        winDC = wx.ClientDC(self)
        colwins = [('Hwnd', 12), ('Visible', 0), ('Iconized', 0), ('Enabled', 0), ('Title', 64),]
        for icol, colitem in enumerate(colwins):
            colname, colwidth = colitem
            self.m_listCtrlWins.InsertColumn(icol, colname)
            if not colwidth:
                colwidth = len(colname) + 3
            colwidth, colheight = winDC.GetTextExtent( 'a' * colwidth)
            self.m_listCtrlWins.SetColumnWidth(icol, colwidth)

if True:
    @mvc.PubRecv('mainmodel.hwndshown')
    def OnHwndShown(self, hwnds):
        if self.foreground:
            self.model.SetForeground(hwnds)

        if self.selfforeground:
            # self.model.SetForeground([self.model.hwnd,])
            self.Raise()

if True:
    @mvc.PubRecv('mainmodel.hwndinfos')
    def OnHwndInfos(self, msg):
        hwndinfos = msg
        self.m_listCtrlWins.DeleteAllItems()

        checks = ['titled', 'enabled', 'iconized', 'visible']

        stats_total = 0
        stats_titled = 0
        stats_visible = 0
        stats_iconized = 0
        stats_enabled = 0
        stats_shown = 0

        for index, hwndinfo in enumerate(hwndinfos):
            stats_total += 1
            stats_titled += 1 if hwndinfo.titled else 0
            stats_visible += 1 if hwndinfo.visible else 0
            stats_iconized += 1 if hwndinfo.iconized else 0
            stats_enabled += 1 if hwndinfo.enabled else 0

            show = True
            for check in checks:
                # If any check fails, it will be skipped
                configholder = getattr(self, check)
                configcheck = getattr(configholder, 'value')
                configwin = getattr(hwndinfo, check)

                if configcheck == wx.CHK_UNDETERMINED:
                    break

                if configcheck == wx.CHK_CHECKED and not configwin:
                    show = False
                    break

                if configcheck == wx.CHK_UNCHECKED and configwin:
                    show = False
                    break

            if not show:
                continue

            stats_shown += 1

            col = itertools.count(1)
            newindex = self.m_listCtrlWins.InsertStringItem(index, hex(hwndinfo.hwnd))
            if newindex != -1:
                self.m_listCtrlWins.SetStringItem(newindex, col.next(), str(hwndinfo.visible))
                self.m_listCtrlWins.SetStringItem(newindex, col.next(), str(hwndinfo.iconized))
                self.m_listCtrlWins.SetStringItem(newindex, col.next(), str(hwndinfo.enabled))
                self.m_listCtrlWins.SetStringItem(newindex, col.next(), str(hwndinfo.titled))
                self.m_listCtrlWins.SetItemData(newindex, hwndinfo.hwnd)

            self.m_staticTextRetrieved.SetLabel('%4d' % stats_total)
            self.m_staticTextTitled.SetLabel('%4d' % stats_titled)
            self.m_staticTextVisible.SetLabel('%4d' % stats_visible)
            self.m_staticTextIconized.SetLabel('%4d' % stats_iconized)
            self.m_staticTextEnabled.SetLabel('%4d' % stats_enabled)
            self.m_staticTextShown.SetLabel('%4d' % stats_shown)
                
    def GetSelectedHwnds(self):
        selected = list()
        index = self.m_listCtrlWins.GetFirstSelected()
        while index != -1:
            hwnd = self.m_listCtrlWins.GetItemData(index)
            selected.append(hwnd)
            index = self.m_listCtrlWins.GetNextSelected(index)
        return selected
