from sys import argv 
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
#                                 Web Browser (HTML Frame)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QMainWindow):
   def __init__(self, *args, **kwargs):
      super(Window, self).__init__(*args, **kwargs)


      self.browser = QWebEngineView()
      self.browser.setUrl(QUrl('https://start.duckduckgo.com/'))
      self.browser.urlChanged.connect(self.update_AddressBar)
      self.setCentralWidget(self.browser)
      self.browser.loadFinished.connect(self.update_title)

      self.status_bar = QStatusBar()
      self.setStatusBar(self.status_bar)

      self.navigation_bar = QToolBar('Navigation Toolbar')
      self.addToolBar(self.navigation_bar)

      back_button = QAction("[ < ]", self)
      back_button.setStatusTip('Go to previous page you visited')
      back_button.triggered.connect(self.browser.back)
      self.navigation_bar.addAction(back_button)

      next_button = QAction("[ > ]", self)
      next_button.setStatusTip('Go to next page')
      next_button.triggered.connect(self.browser.forward)
      self.navigation_bar.addAction(next_button)

      refresh_button = QAction("Refresh", self)
      refresh_button.setStatusTip('Refresh this page')
      refresh_button.triggered.connect(self.browser.reload)
      self.navigation_bar.addAction(refresh_button)

      home_button = QAction("Home", self)
      home_button.setStatusTip('Go to home page (Google page)')
      home_button.triggered.connect(self.go_to_home)
      self.navigation_bar.addAction(home_button)

      self.navigation_bar.addSeparator()

      self.URLBar = QLineEdit()
      self.URLBar.returnPressed.connect(lambda: self.go_to_URL(QUrl(self.URLBar.text())))  # This specifies what to do when enter is pressed in the Entry field
      self.navigation_bar.addWidget(self.URLBar)

      self.addToolBarBreak()

      # Adding another toolbar which contains the bookmarks
      bookmarks_toolbar = QToolBar('Bookmarks', self)
      self.addToolBar(bookmarks_toolbar)

      pythonsite = QAction("Python", self)
      pythonsite.setStatusTip("Go to Python website")
      pythonsite.triggered.connect(lambda: self.go_to_URL(QUrl("https://python.org")))
      bookmarks_toolbar.addAction(pythonsite)

      discordsite = QAction("Discord", self)
      discordsite.setStatusTip("Go to Discord")
      discordsite.triggered.connect(lambda: self.go_to_URL(QUrl("https://discord.com")))
      bookmarks_toolbar.addAction(discordsite)

      facebook = QAction("Facebook", self)
      facebook.setStatusTip("Go to Facebook")
      facebook.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.facebook.com")))
      bookmarks_toolbar.addAction(facebook)

      linkedin = QAction("LinkedIn", self)
      linkedin.setStatusTip("Go to LinkedIn")
      linkedin.triggered.connect(lambda: self.go_to_URL(QUrl("https://in.linkedin.com")))
      bookmarks_toolbar.addAction(linkedin)

      instagram = QAction("Instagram", self)
      instagram.setStatusTip("Go to Instagram")
      instagram.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.instagram.com")))
      bookmarks_toolbar.addAction(instagram)

      twitter = QAction("Twitter", self)
      twitter.setStatusTip('Go to Twitter')
      twitter.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.twitter.com")))
      bookmarks_toolbar.addAction(twitter)
      
      # Style
      self.setWindowIcon(QIcon('resources/logo_1.ico'))
      app.setStyle('Fusion')
      self.setStyleSheet("background-color: gray;")
      self.navigation_bar.setStyleSheet("color: white;")
      bookmarks_toolbar.setStyleSheet("color: white;")

      self.show()

   # method for updating the title of the window
   def update_title(self):
      title = self.browser.page().title()
      self.setWindowTitle("% s - Nova Browser" % title)

   def go_to_home(self):
      self.browser.setUrl(QUrl('https://start.duckduckgo.com/'))

   def go_to_URL(self, url: QUrl):
      if url.scheme() == '':
         url.setScheme('https://')
      self.browser.setUrl(url)
      self.update_AddressBar(url)

   def update_AddressBar(self, url):
      self.URLBar.setText(url.toString())
      self.URLBar.setCursorPosition(0)


app = QApplication(argv)
app.setApplicationName('Nova')

window = Window()
app.exec_()