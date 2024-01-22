# Automated fixing is employed to identify the reason why Apache is returning a 500 error

exec { 'Fix wordpress site':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
