# Add a custom header to response
exec { 'Add_header':
    provider => 'shell',
    command  => 'sudo sed -i "/^\slocation /a \\\\\t\tadd_header X-Served-By \$hostname;" /etc/nginx/sites-enabled/default;
    sudo service nginx restart'
}