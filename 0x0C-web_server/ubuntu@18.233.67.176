# Install and configure nginx
exec { 'install_nginx':
    provider => 'shell',
    command => 'apt-get update -y; apt-get install nginx -y; ufw allow 'Nginx Https'; echo "Hello World!" > /var/www/html/index.html;
    echo "Ceci n'est pas une page" > /var/www/html/error404.html; sed -i '/server_name _/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-enabled/default; sed -i '/rewrite/a  error_page 404 /error404.html;' /etc/nginx/sites-enabled/default; service nginx restart'
}
