import os
import sys
from requests import *
def makesure(link):
	if get(link).status_code == 200:
		pass
	else:
		print("link incorrect")
		sys.exit()

try:
	station = sys.argv[1]
except:
	station = "https://duckduckgo.com/"
	
makesure(station)
first = '''const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const Tray = electron.Tray;

let mainWindow;

function createWindow () {

  mainWindow = new BrowserWindow({width: 1800, height: 1200});

  mainWindow.loadURL(`'''

second = '''`);

  mainWindow.on('closed', () => {

    mainWindow = null;

  })
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {

  if (process.platform !== 'darwin') {

    app.quit();

  }

});

app.on('activate', () => {

  if (mainWindow === null) {

    createWindow();

  }
  
});  
'''

file = open("index.js", "w")
total = f"{first}{station}{second}"
file.write(''.join(total))
file.close()
os.system("electron index.js")
