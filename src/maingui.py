# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from utils.widgets.sortlistctrl import SortListCtrl
import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
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
		
		self.m_buttonShow = wx.Button( self.m_panel1, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_buttonShow, 0, wx.ALL, 5 )
		
		self.m_buttonRestore = wx.Button( self.m_panel1, wx.ID_ANY, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_buttonRestore, 0, wx.ALL, 5 )
		
		self.m_buttonMaximize = wx.Button( self.m_panel1, wx.ID_ANY, u"Maximize", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_buttonMaximize, 0, wx.ALL, 5 )
		
		self.m_buttonMinimize = wx.Button( self.m_panel1, wx.ID_ANY, u"Minimize", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_buttonMinimize, 0, wx.ALL, 5 )
		
		self.m_buttonHide = wx.Button( self.m_panel1, wx.ID_ANY, u"Hide", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_buttonHide, 0, wx.ALL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer5.Add( self.m_staticline3, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonAbout = wx.Button( self.m_panel1, wx.ID_ANY, u"About", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_buttonAbout, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Statistics" ), wx.VERTICAL )
		
		bSizer61111 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		sbSizer2.Add( bSizer61111, 0, wx.EXPAND, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 8, 75, 90, 92, False, "Lucida Sans Typewriter" ) )
		
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_staticTextRetrieved = wx.StaticText( self.m_panel1, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticTextRetrieved.Wrap( -1 )
		self.m_staticTextRetrieved.SetFont( wx.Font( 8, 75, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_staticTextRetrieved, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Titled", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 8, 75, 90, 92, False, "Lucida Sans" ) )
		
		fgSizer1.Add( self.m_staticText12, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticTextTitled = wx.StaticText( self.m_panel1, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticTextTitled.Wrap( -1 )
		self.m_staticTextTitled.SetFont( wx.Font( 8, 75, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_staticTextTitled, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText121 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Visible", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )
		self.m_staticText121.SetFont( wx.Font( 8, 75, 90, 92, False, "Lucida Sans Typewriter" ) )
		
		fgSizer1.Add( self.m_staticText121, 1, wx.ALL, 5 )
		
		self.m_staticTextVisible = wx.StaticText( self.m_panel1, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticTextVisible.Wrap( -1 )
		self.m_staticTextVisible.SetFont( wx.Font( 8, 75, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_staticTextVisible, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText1211 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Iconized", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1211.Wrap( -1 )
		self.m_staticText1211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 75, 90, 92, False, "Lucida Sans Typewriter" ) )
		
		fgSizer1.Add( self.m_staticText1211, 1, wx.ALL, 5 )
		
		self.m_staticTextIconized = wx.StaticText( self.m_panel1, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticTextIconized.Wrap( -1 )
		self.m_staticTextIconized.SetFont( wx.Font( 8, 75, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_staticTextIconized, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText12111 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Enabled", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12111.Wrap( -1 )
		self.m_staticText12111.SetFont( wx.Font( 8, 75, 90, 92, False, "Lucida Sans" ) )
		
		fgSizer1.Add( self.m_staticText12111, 1, wx.ALL, 5 )
		
		self.m_staticTextEnabled = wx.StaticText( self.m_panel1, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticTextEnabled.Wrap( -1 )
		self.m_staticTextEnabled.SetFont( wx.Font( 8, 75, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_staticTextEnabled, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText121111 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Shown", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121111.Wrap( -1 )
		self.m_staticText121111.SetFont( wx.Font( 8, 75, 90, 92, False, "Lucida Sans" ) )
		
		fgSizer1.Add( self.m_staticText121111, 0, wx.ALL, 5 )
		
		self.m_staticTextShown = wx.StaticText( self.m_panel1, wx.ID_ANY, u"----", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticTextShown.Wrap( -1 )
		self.m_staticTextShown.SetFont( wx.Font( 8, 75, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_staticTextShown, 0, wx.ALL, 5 )
		
		
		sbSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		
		bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_buttonGetWindows = wx.Button( self.m_panel1, wx.ID_ANY, u"Get Windows", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_buttonGetWindows, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
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
	
	def __del__( self ):
		pass
	

###########################################################################
## Class AboutDialog
###########################################################################

class AboutDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebookAbout = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panelAbout = wx.Panel( self.m_notebookAbout, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextAppNameVersion = wx.StaticText( self.m_panelAbout, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextAppNameVersion.Wrap( -1 )
		bSizer10.Add( self.m_staticTextAppNameVersion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextCopyright = wx.StaticText( self.m_panelAbout, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextCopyright.Wrap( -1 )
		bSizer10.Add( self.m_staticTextCopyright, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_hyperlinkURL = wx.HyperlinkCtrl( self.m_panelAbout, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
		bSizer10.Add( self.m_hyperlinkURL, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.m_panelAbout.SetSizer( bSizer10 )
		self.m_panelAbout.Layout()
		bSizer10.Fit( self.m_panelAbout )
		self.m_notebookAbout.AddPage( self.m_panelAbout, u"About", True )
		
		bSizer8.Add( self.m_notebookAbout, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_buttonClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_buttonClose, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PanelAboutDocument
###########################################################################

class PanelAboutDocument ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrlDocument = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_AUTO_URL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer111.Add( self.m_textCtrlDocument, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer111 )
		self.Layout()
		bSizer111.Fit( self )
	
	def __del__( self ):
		pass
	

