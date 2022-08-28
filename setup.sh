echo "downloading files"
sleep 1
sudo apt-get install python3 npm nodejs python3-pip 
clear
sudo dnf install python3 nodejs npm python3-pip 
clear
sudo pacman -S install python3 nodejs npm python3-pip
clear
pip install requests
clear
sudo npm install -g electron --unsafe-perm=true
clear
echo "done!"
echo "now you can launch it by writing 'python3 main.py <link>"
echo "enjoy!"
