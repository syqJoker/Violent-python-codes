# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import wx
from ChatFrame import *


class LogInDialog(wx.Dialog):

    """docstring for LogInDialog"""

    def __init__(self, parent, ID, title):
        super(LogInDialog, self).__init__(
            parent, -1, title, wx.DefaultPosition, wx.Size(480, 270))
        self.Center()
        panel = wx.Panel(self, -1)
        # 添加两个label
        wx.StaticText(panel, -1, 'ServerIP:', pos=(140, 80))
        wx.StaticText(panel, -1, 'Name:', pos=(140, 120))
        # 输入IP地址的文本框
        self.serverIPText = wx.TextCtrl(
            panel, -1, '192.168.1.101:3000', pos=(210, 76), size = (120, 30))
        # 输入name的文本框
        self.nameEdit = wx.TextCtrl(
            panel, -1, 'cyril', pos=(210, 116), size = (120, 30))
        # 确认按钮
        self.logInBtn = wx.Button(panel, wx.ID_OK, 'Log In', pos=(280, 220))
        # 取消按钮
        self.cancleBtn = wx.Button(
            panel, wx.ID_CANCEL, 'Cancle', pos=(370, 220))


class ClientApp(wx.App):

    """docstring for ClientApp"""
    # wxpython　程序启动会首先运行OnInit

    def OnInit(self):
        logInDlg = LogInDialog(None, -1, 'Log in')
        while True:
            # 登录窗口显示
            result = logInDlg.ShowModal()
            # 按下登录按钮
            if result == wx.ID_OK:
                # 聊天主界面
                self.frame = MainFrame(None, -1, logInDlg.nameEdit.Value)
                # 判断是否与服务器连接成功，如果成功就显示主界面
                if self.frame.connect(logInDlg.serverIPText.Value):
                    self.SetTopWindow(self.frame)
                    self.frame.Show()
                    break
            # 退出程序
            if result == wx.ID_CANCEL:
                break
        # 销毁对话框
        logInDlg.Destroy()
        return True

if __name__ == '__main__':
    # wxPython的框架
    app = ClientApp(0)
    app.MainLoop()