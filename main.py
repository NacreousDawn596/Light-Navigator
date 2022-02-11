import os
import sys
from requests import *
from bs4 import *
def makesure(link):
	if get(link).status_code == 200:
		security(link)
	else:
		print("link incorrect")
		sys.exit()
def security(ty):
	result = BeautifulSoup(os.popen(f"curl -s http://trueurl.net/service?q={ty.replace(':', '%3A').replace('/', '%2F')}&lucky=on&Uncloak=Find+True+URL").read(), 'html.parser').find_all('td')[3].find_all('a')
	try:
		if len(result) == 1:
			result = result[0].get('href')
		else:
			result = result[1].get('href')
		if ty == result:
			pass
		else:
			umm = input(f"do you want to be redirected to this link: '{result}'? y/n\n->")
			if "y" in umm.lower():
				pass
			else:
				print("okay")
				sys.exit()
	except IndexError:
		humm = input(f'is this domain trusted? "{ty.replace("https://", "").replace("http://", "").split("/")[0]}" y/n\n->')
		if "y" in humm.lower():
			pass
		else:
			print("okay")
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
