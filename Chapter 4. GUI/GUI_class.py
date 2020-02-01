import maya.cmds as cmds

#most of the companies use classes to utilize as namespace
class SJ_OptionWindow(object): #object: fundamental object in python

    def __init__(self): #initalize    #self를 지정하지 않게 되면, 지역변수화가 된다.
        self.window="optionWindow"
        self.title="First Window"
        self.size=(540,320)
        self.supportsToolAction=False
        self.actionName = 'Apply and Close'
        
    def create(self):
        if cmds.window(self.window,exists=True):
            cmds.deleteUI(win,window=True)
        self.window=cmds.window(self.window,title=self.title,widthHeight=self.size,menuBar=True)
        
        self.commonMenu() #commonMenu 생성
        self.commonButtons() #button 생성
        cmds.showWindow()
        
    def commonMenu(self):
        self.editMenu = cmds.menu(label='Edit')
        self.editMenuSave = cmds.menuItem(label='Save Settings')
        self.editMenuReset = cmds.menuItem(label='Reset Settings')
        
        self.editMenuDiv = cmds.menuItem(d=True) #enable: 기능의 on off의 여부
        self.editMenuTool = cmds.menuItem(label = 'As Tool', radioButton=True,enable = self.supportsToolAction)
        self.editMenuAction = cmds.menuItem(label = 'As Action', radioButton=True, enable = self.supportsToolAction)
        
        self.helpMenu = cmds.menu(label = 'Help')
        self.helpMenuItem = cmds.menuItem(label = 'Help on %s' %self.title, command = self.helpMenuCmd)

    def commonButtons(self):
        #datatpe = tuple(width,height)
        self.commonBtnSize = ((self.size[0] - 18)/3,26)
        #rowLayout, columnlayout도 있다.
        #rowLayout cw=column width, ct=column attachment, co=column offset, cl = column test alignment      
        self.commonBtnLayout = cmds.rowLayout(numberOfColumns = 3,cw3 = (self.commonBtnSize[0]+3, self.commonBtnSize[0]+3, self.commonBtnSize[0]+3),ct3=('both','both','both'), co3=(2,0,2), cl3=('center','center','center'))
        self.actionBtn = cmds.button(label=self.actionName,height=self.commonBtnSize[1], command = self.applyBtnCmd)
        self.applyBtn = cmds.button(label='Apply',height=self.commonBtnSize[1],command = self.applyBtnCmd)
        self.closeBtn = cmds.button(label='Close',height= self.commonBtnSize[1],command = self.closeBtnCmd)
        
    #이 다음에 어떤 액션이 오는지 따로 지정해야 주어야 한다.
    def helpMenuCmd(self, *args):
        cmds.launch(web = "http://download.autodesk.com/global/docs/maya2014/en_us/CommandsPython/index.html")
    def actionBtnCmd(self,*args):
        pass

    def applyBtnCmd(self, *args):
        pass
        
    def closeBtnCmd(self, *args):
        cmds.deleteUI(self.window, window=True)
    
testWindow=SJ_OptionWindow()    #utilize class
testWindow.create()    #classname.function()
