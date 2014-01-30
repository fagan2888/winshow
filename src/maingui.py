# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from sortlistctrl import SortListCtrl
import wx
import wx.xrc

###########################################################################
## Class WinShow
###########################################################################

class WinShow ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"WinShow", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlWins = SortListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,300 ), wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
		bSizer4.Add( self.m_listCtrlWins, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxSelfForeground = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Bring self to Foreground after any action", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_checkBoxSelfForeground, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline21 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer11.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxForeground = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Bring target window to Foreground after action", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_checkBoxForeground, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button4 = wx.Button( self.m_panel1, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self.m_panel1, wx.ID_ANY, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button5, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel1, wx.ID_ANY, u"Maximize", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button6, 0, wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self.m_panel1, wx.ID_ANY, u"Minimize", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_button8 = wx.Button( self.m_panel1, wx.ID_ANY, u"Hide", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button8, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Statistics" ), wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Retrieved", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 92, False, wx.EmptyString ) )
		
		bSizer6.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText2.Wrap( -1 )
		bSizer6.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		sbSizer2.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText12 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"With Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 92, False, wx.EmptyString ) )
		
		bSizer61.Add( self.m_staticText12, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText22.Wrap( -1 )
		bSizer61.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		sbSizer2.Add( bSizer61, 0, wx.EXPAND, 5 )
		
		bSizer611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText121 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Visible", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )
		self.m_staticText121.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 92, False, wx.EmptyString ) )
		
		bSizer611.Add( self.m_staticText121, 1, wx.ALL, 5 )
		
		self.m_staticText221 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText221.Wrap( -1 )
		bSizer611.Add( self.m_staticText221, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		sbSizer2.Add( bSizer611, 0, wx.EXPAND, 5 )
		
		bSizer6111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1211 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Iconized", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1211.Wrap( -1 )
		self.m_staticText1211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 92, False, wx.EmptyString ) )
		
		bSizer6111.Add( self.m_staticText1211, 1, wx.ALL, 5 )
		
		self.m_staticText2211 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText2211.Wrap( -1 )
		bSizer6111.Add( self.m_staticText2211, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		sbSizer2.Add( bSizer6111, 0, wx.EXPAND, 5 )
		
		bSizer61111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText12111 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Enabled", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12111.Wrap( -1 )
		self.m_staticText12111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 92, False, wx.EmptyString ) )
		
		bSizer61111.Add( self.m_staticText12111, 1, wx.ALL, 5 )
		
		self.m_staticText22111 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText22111.Wrap( -1 )
		bSizer61111.Add( self.m_staticText22111, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		sbSizer2.Add( bSizer61111, 0, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		
		bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Get Windows", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		self.m_checkBoxTitled = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Titled", wx.DefaultPosition, wx.DefaultSize, wx.CHK_3STATE|wx.CHK_ALLOW_3RD_STATE_FOR_USER )
		sbSizer1.Add( self.m_checkBoxTitled, 0, wx.ALL, 5 )
		
		self.m_checkBoxVisible = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Visible", wx.DefaultPosition, wx.DefaultSize, wx.CHK_3STATE|wx.CHK_ALLOW_3RD_STATE_FOR_USER )
		sbSizer1.Add( self.m_checkBoxVisible, 0, wx.ALL, 5 )
		
		self.m_checkBoxIconized = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Iconized", wx.DefaultPosition, wx.DefaultSize, wx.CHK_3STATE|wx.CHK_ALLOW_3RD_STATE_FOR_USER )
		sbSizer1.Add( self.m_checkBoxIconized, 0, wx.ALL, 5 )
		
		self.m_checkBoxEnabled = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Enabled", wx.DefaultPosition, wx.DefaultSize, wx.CHK_3STATE|wx.CHK_ALLOW_3RD_STATE_FOR_USER )
		sbSizer1.Add( self.m_checkBoxEnabled, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( sbSizer1, 0, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer3, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_checkBoxSelfForeground.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxSelfForeground )
		self.m_checkBoxForeground.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxForeground )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnButtonClickShow )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnButtonClickRestore )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnButtonClickMaximize )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnButtonClickMinimize )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnButtonClickHide )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnButtonClickGetWindows )
		self.m_checkBoxTitled.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxTitled )
		self.m_checkBoxVisible.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxVisible )
		self.m_checkBoxIconized.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxIconized )
		self.m_checkBoxEnabled.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxEnabled )
	
	def __del__( self ):
		# Disconnect Events
		self.m_checkBoxSelfForeground.Unbind( wx.EVT_CHECKBOX, None )
		self.m_checkBoxForeground.Unbind( wx.EVT_CHECKBOX, None )
		self.m_button4.Unbind( wx.EVT_BUTTON, None )
		self.m_button5.Unbind( wx.EVT_BUTTON, None )
		self.m_button6.Unbind( wx.EVT_BUTTON, None )
		self.m_button7.Unbind( wx.EVT_BUTTON, None )
		self.m_button8.Unbind( wx.EVT_BUTTON, None )
		self.m_button1.Unbind( wx.EVT_BUTTON, None )
		self.m_checkBoxTitled.Unbind( wx.EVT_CHECKBOX, None )
		self.m_checkBoxVisible.Unbind( wx.EVT_CHECKBOX, None )
		self.m_checkBoxIconized.Unbind( wx.EVT_CHECKBOX, None )
		self.m_checkBoxEnabled.Unbind( wx.EVT_CHECKBOX, None )
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCheckBoxSelfForeground( self, event ):
		event.Skip()
	
	def OnCheckBoxForeground( self, event ):
		event.Skip()
	
	def OnButtonClickShow( self, event ):
		event.Skip()
	
	def OnButtonClickRestore( self, event ):
		event.Skip()
	
	def OnButtonClickMaximize( self, event ):
		event.Skip()
	
	def OnButtonClickMinimize( self, event ):
		event.Skip()
	
	def OnButtonClickHide( self, event ):
		event.Skip()
	
	def OnButtonClickGetWindows( self, event ):
		event.Skip()
	
	def OnCheckBoxTitled( self, event ):
		event.Skip()
	
	def OnCheckBoxVisible( self, event ):
		event.Skip()
	
	def OnCheckBoxIconized( self, event ):
		event.Skip()
	
	def OnCheckBoxEnabled( self, event ):
		event.Skip()
	

