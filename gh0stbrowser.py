#Simple Browser written in python Install the Libs below
#irc.twistednet.org #dev #twisted
#by gh0st 

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction('←', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('→', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Home button
        home_btn = QAction('🏠', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Dark Mode Toggle Button
        self.dark_mode_btn = QAction('Dark Mode', self)
        self.dark_mode_btn.triggered.connect(self.toggle_dark_mode)
        navbar.addAction(self.dark_mode_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Updating the URL bar
        self.browser.urlChanged.connect(self.update_url)

        self.dark_mode = False

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def toggle_dark_mode(self):
        if not self.dark_mode:
            self.browser.page().runJavaScript("""
                var style = document.createElement('style');
                style.type = 'text/css';
                style.id = 'dark-mode-style';
                style.innerHTML = 'body { background-color: #121212; color: white; }';
                document.head.appendChild(style);
            """)
            self.dark_mode = True
            self.dark_mode_btn.setText('Light Mode')
        else:
            self.browser.page().runJavaScript("document.getElementById('dark-mode-style').remove();")
            self.dark_mode = False
            self.dark_mode_btn.setText('Dark Mode')

app = QApplication(sys.argv)
QApplication.setApplicationName('gh0st Browser')
window = Browser()
app.exec_()
