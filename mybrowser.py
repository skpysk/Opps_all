import sys
from turtle import forward
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.showMaximized()
        self.browser = QWebEngineView() # from PyQt5.QtWebEngineWidgets import *
        self.browser.setUrl(QUrl("http://google.com/")) #  from PyQt5.QtCore import *  # any url as central url
        self.setCentralWidget(self.browser)

        # nav bar
        navbar = QToolBar()
        self.addToolBar(navbar)
        # back button
        back_button = QAction("Back",self)
        back_button.triggered.connect( self.browser.back )
        # add it on nav bar
        navbar.addAction(back_button)
        # forward button
        forwr_button = QAction("Forward", self)
        forwr_button.triggered.connect(self.browser.forward)
        navbar.addAction(forwr_button)
        # reload button
        reload_button = QAction("Reload", self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)
        # home button
        home_button = QAction("Home", self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)
        # search bar
        self.url_bar  = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url) # navigate_to url is ur choive baseed 
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
    # home ka url set
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com/"))
    def navigate_to_url(self):
        url = self.url_bar.text() # url bar me jo search krega usko get krengi
        self.browser.setUrl(QUrl(url)) # variable jo upper bnaya thaa
    # url update method
    def update_url(self,q): # hmko kya 
        self.url_bar.setText(q.toString())



app = QApplication(sys.argv)
QApplication.setApplicationName('My Browser')
window = MainWindow()
app.exec_()