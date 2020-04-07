import wx


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='mail tools')
        panel = wx.Panel(frame,-1)
        button1 = wx.Button(panel, 1, u'Choose File',pos = (300,10))
        self.button1  = button1
        self.Bind(wx.EVT_BUTTON,
                  self.OnButton1,
                  self.button1)

        button2 = wx.Button(panel, 2, u'Extract',pos = (300,50))
        self.button2  = button2
        self.Bind(wx.EVT_BUTTON,
                  self.OnButton2,
                  self.button2)

        self.text1 = wx.TextCtrl(panel,1,pos=(10,10),size = (280,30),
                                 style = wx.TE_MULTILINE)

        self.text2 = wx.TextCtrl(panel,2,pos=(10,50),size = (280,330),
                                 style = wx.TE_MULTILINE)

        self.list = []
        self.listbox = wx.ListBox(panel , -1, pos = (300,90),size = (90,120),
                                 choices = self.list, style = wx.LB_SINGLE)




        frame.Show()
        return True

    def OnButton1(self,event):
        self.button1.SetLabel('your sister')

    def OnButton2(self,event):
        self.button2.SetLabel('your sister')

app = MyApp()
app.MainLoop()
