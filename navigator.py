import os

os.system("clear")

os.system("figlet Light Navigator")

print("                  -{By NacreousDawn596}-")

station = input("enter the link \n; at the beggining for the https links\n, at the beggining for the http links \n(leave empty for https://google.com) \n->")

file = open("index.js", "w")

try:

	first_part = '''const electron = require('electron');

const app = electron.app;

const BrowserWindow = electron.BrowserWindow;

const Tray = electron.Tray;

let mainWindow;

function createWindow () {

  mainWindow = new BrowserWindow({width: 1800, height: 1200});

  mainWindow.loadURL(`'''

	if station[0] == ";":

		station = station[1 : -1]

		station = f"https://{station}"

	elif station[0] == ",":

		extention = station.split(".")[-1]

		station = station[1 : -1]

		station = station.split(".")[0 : -1]

		stat = []

		n = 0

		for items in station:

			stat.append(station[n])

			stat.append(".")

			n = n + 1

		stat = ''.join([str(item) for item in stat])

		station = f"http://{stat}{extention}"

	file.write("".join(first_part))

	file.write("".join(station))

	second_part = '''`);

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
	  
});  '''

	file.write("".join(second_part))

except IndexError:

	content = '''const electron = require('electron');

const app = electron.app;

const BrowserWindow = electron.BrowserWindow;

const Tray = electron.Tray;

let mainWindow;

function createWindow () {

	 mainWindow = new BrowserWindow({width: 1800, height: 1200});

	 mainWindow.loadURL(`https://google.com`);

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
	  
});  '''

	file.write("".join(content))

file.close()

os.system("electron index.js")

print("hi")








#cd && cd 'Light Navigator' && sudo apt-get install nodejs python3 figlet && sudo npm install electron -g && npm install electron --save-dev && python3 navigator.py