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
import wx


class ConfigBase(object):
    Config = wx.FileConfig

    def __init__(self, name, defvalue, **kwargs):
        self.name = name
        self.icache = dict()
        self.bcache = dict()
        self.defvalue = defvalue

    def __get__(self, instance, owner=None):
        try:
            return self.icache[instance]
        except KeyError:
            retval = self.rd(instance.config, self.name, self.defvalue)
            instance.config.Flush() # in case defvalue has been used
            self.icache[instance] = retval
            return retval
            
        return self.icache[instance]
        
    def __set__(self, instance, value):
        self.wr(instance.config, self.name, value)
        instance.config.Flush()
        self.icache[instance] = value


class ConfigString(ConfigBase):
    wr = ConfigBase.Config.Write # unbound method
    rd = ConfigBase.Config.Read # unbound method

class ConfigBool(ConfigBase):
    wr = ConfigBase.Config.WriteBool # unbound method
    rd = ConfigBase.Config.ReadBool # unbound method

class ConfigInt(ConfigBase):
    wr = ConfigBase.Config.WriteInt # unbound method
    rd = ConfigBase.Config.ReadInt # unbound method

class ConfigFloat(ConfigBase):
    wr = ConfigBase.Config.WriteFloat # unbound method
    rd = ConfigBase.Config.ReadFloat # unbound method


class Config(object):
    vcdir = ConfigString('vcdir', '')
    scdir = ConfigString('scdir', '')
    indir = ConfigString('indir', '')

    def __init__(self, appname, vendorname):
        self.config = ConfigBase.Config(appname, vendorname)
        self.config.SetRecordDefaults(True)


config = Config('vcsc', 'Sensible Odds')
