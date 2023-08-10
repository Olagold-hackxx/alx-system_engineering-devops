# Debug Server
exec { 'Fix error found in wp-settings.php file':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
