#imports
from imp import reload
import sys
from turtle import forward
from pyQT5.QtCore import *
from PyQT5.QtWidgets import *
from PyQT5.QtwebEngineWidgets import *

#class

class mainwindow(Qmainwindow):
    #encapsulation
    def __init__(self):
        super(mainwindow, self).__init__()
        #don't touch this
        self.browser = QwebEngineView
        self.browser.setURL(QUrl('https://dalton-s-mabuza.netlify.app/')) #change URL to your engine
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        #nav bar
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        
        
        back_btn = QAction('Back', self)
        back_btn.triggered.connection(self.browser.back)
        navbar.addAction(back_btn)
        
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connection(self.browser.forward)
        navbar.addAction(forward_btn)
        
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connection(self.browser.reload)
        navbar.addAction(reload_btn)
        
        home_btn = QAction('home', self)
        reload_btn.triggered.connection(self.navigate_home)
        navbar.addAction(home_btn)
        
        selt.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        

        
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://dalton-s-mabuza.netlify.app/')) #change to your engine URL
        
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.seturl(QUrl(url))
      
#Browser Execution
app = QApplication(sys.argv)
QApplication.setApplicationName('Delta Browser')

window = mainwindow

app.exec_()