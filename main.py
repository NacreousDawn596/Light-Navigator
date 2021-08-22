import os

first = '''const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const Tray = electron.Tray;

let mainWindow;

function createWindow () {

  mainWindow = new BrowserWindow({width: 1800, height: 1200});

  mainWindow.loadURL(`'''

station = open(".conf", "r")
station = station.read()
station = station.split()[0]

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