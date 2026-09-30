ssh -i c370570.pem ubuntu@15.222.190.85
sudo apt update
sudo apt install apache2 -y
sudo sed -i 's/^Listen 80$/Listen 8008/' /etc/apache2/ports.conf
sudo sed -i 's/<VirtualHost \*:80>/<VirtualHost *:8008>/' /etc/apache2/sites-available/000-default.conf
sudo systemctl restart apache2
echo "Hello from my COMP 370 EC2! Fun fact: octopuses have three hearts." | sudo tee /var/www/html/comp370_hw3.txt
curl http://localhost:8008/comp370_hw3.txt
# Open in a browser: http://15.222.190.85:8008/comp370_hw3.txt