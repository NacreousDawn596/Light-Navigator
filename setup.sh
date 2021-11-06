echo "downloading files"
sleep 1
sudo apt-get install python3 npm python3-pip python3-bs4
clear
sudo dnf install install python3 npm python3-pip python3-bs4
clear
sudo pacman -S install python3 npm python3-pip python3-bs4
clear
pip install requests bs4
clear
sudo npm install electron -g
clear
echo "configuring files"
mkdir ~/.local/share/NacreousDawn596
cd ..
mv ./lowser ~/.local/share/NacreousDawn596
rm ~/.local/share/NacreousDawn596/lowser/setup.sh
echo 'source ~/.local/share/NacreousDawn596/lowser/.lowser.sh' >> ~/.bashrc
clear
echo "done!"
echo "now you can launch it by writing 'nav https://google.com'(you can change the link)"
echo "enjoy!"
