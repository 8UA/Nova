try:
   from time import sleep
   from sys import argv 
   import urllib.request
   import qtmodern.styles
   import qtmodern.windows
   from PyQt5.QtCore import QUrl, QSize
   from PyQt5.QtWebEngineWidgets import QWebEngineView #    Web Browser (HTML Frame)    #
   from PyQt5.QtWidgets import *
   from PyQt5.QtGui import *
except ImportError:
   print()
   sleep(5)
   print("Some modules are missing, use the install batch file.")


# Check if connected to internet.
def connect():
   host = 'http://google.com'
   try:
      urllib.request.urlopen(host) # Python 3.x
      return True
   except:
      return False

class Window(QMainWindow):
   def __init__(self, *args, **kwargs):
      super(Window, self).__init__(*args, **kwargs)
   
      self.browser = QWebEngineView()

      self.status_bar = QStatusBar()
      self.setStatusBar(self.status_bar)
      
      self.navigation_bar = QToolBar('Navigation Toolbar')
      self.addToolBar(self.navigation_bar)

      if connect() == False:
         self.browser.setUrl(QUrl("file:///resources/error.html"))
      else:
         self.browser.setUrl(QUrl('https://start.duckduckgo.com/'))
      self.browser.urlChanged.connect(self.update_AddressBar)
      self.setCentralWidget(self.browser)
      self.browser.loadFinished.connect(self.update_title)

      # BUTTONS DEFAULT SIZE
      size = QSize(16, 16)
      self.setIconSize(size)
      # DEFAULT FONT
      font = QFont("Arial", 8)
      self.setFont(font)

      back_button = QAction("Back",self)
      back_button.setIcon(QIcon('resources/left.png'))
      back_button.setStatusTip('Go to previous page you visited')
      back_button.triggered.connect(self.browser.back)
      self.navigation_bar.addAction(back_button)

      next_button = QAction("Next",self)
      next_button.setIcon(QIcon('resources/right.png'))
      next_button.setStatusTip('Go to next page')
      next_button.triggered.connect(self.browser.forward)
      self.navigation_bar.addAction(next_button)

      refresh_button = QAction("Refresh", self)
      refresh_button.setIcon(QIcon('resources/rotate.png'))
      refresh_button.setStatusTip('Refresh this page')
      refresh_button.triggered.connect(self.browser.reload)
      self.navigation_bar.addAction(refresh_button)

      self.navigation_bar.addSeparator()

      home_button = QAction("Home", self)
      home_button.setIcon(QIcon('resources/home.png'))
      home_button.setStatusTip('Go to home page')
      home_button.triggered.connect(self.go_to_home)
      self.navigation_bar.addAction(home_button)

      self.navigation_bar.addSeparator()

      self.URLBar = QLineEdit()
      self.URLBar.returnPressed.connect(lambda: self.go_to_URL(QUrl(self.URLBar.text())))  # This specifies what to do when enter is pressed in the Entry field
      self.navigation_bar.addWidget(self.URLBar)

      self.navigation_bar.addSeparator()

      options_button = QAction("Options", self)
      options_button.setIcon(QIcon('resources/menu.png'))
      options_button.setStatusTip('See browser options')
                                                               # LOCAL ERROR PAGE (FEATURE NOT IMPLEMENTED) #
      options_button.triggered.connect(lambda: self.go_to_URL(QUrl("file:///resources/error.html")))
      self.navigation_bar.addAction(options_button)
      
      self.navigation_bar.addSeparator()

      # THEMES BUTTONS
      dark_button = QAction("Dark Theme", self)
      dark_button.setIcon(QIcon('resources/moon.png'))
      dark_button.setStatusTip('Sets browser theme to Dark')
      dark_button.triggered.connect(Themes.darkTheme)
      self.navigation_bar.addAction(dark_button)

      # Light theme is broke i know i still need to work on theme changes.
      light_button = QAction("Light Theme [BROKE]", self)
      light_button.setIcon(QIcon('resources/sun.png'))
      light_button.setStatusTip('Sets browser theme to Light')
      light_button.triggered.connect(Themes.lightTheme)
      self.navigation_bar.addAction(light_button)

      self.addToolBarBreak()

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

   def go_to_home(self):
      self.browser.setUrl(QUrl('https://start.duckduckgo.com/'))
      if connect() == False:
         self.browser.setUrl(QUrl("file:///resources/error.html"))

   def go_to_URL(self, url: QUrl):
      if url.scheme() == '':
         url.setScheme('https')
      self.browser.setUrl(url)
      self.update_AddressBar(url)

   def update_AddressBar(self, url):
      if connect() == False:
         self.browser.setUrl(QUrl("file:///resources/error.html"))
      self.URLBar.setText(url.toString())
      self.URLBar.setCursorPosition(0)

   def update_title(self):
      title = self.browser.page().title()
      mw.setWindowTitle("                  % s - Nova Browser" % title)

class Themes:
   def darkTheme():
         qtmodern.styles.dark(app)
      
   def lightTheme():
         qtmodern.styles.light(app)


app = QApplication(argv)
window = Window()

# Default Style
################################################# [WIP]
Themes.darkTheme()
mw = qtmodern.windows.ModernWindow(window)
mw.setWindowTitle("                  Nova")
mw.show()

app.exec_()
