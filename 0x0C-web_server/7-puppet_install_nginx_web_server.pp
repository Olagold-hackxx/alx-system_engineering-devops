# Install and configure nginx
exec { 'install_nginx':
    provider => 'shell',
    command => 'sudo apt-get update -y; sudo apt-get install nginx -y; sudo ufw allow "Nginx Https"; sudo echo "Hello World!" > /var/www/html/index.html;
    sudo sed -i "/server_name _/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-enabled/default; sed -i "/rewrite/a  error_page 404 /error404.html;" /etc/nginx/sites-enabled/default; service nginx restart'
}
