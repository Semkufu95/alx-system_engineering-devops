# A puppet script that automates the fixing of web server
exec { 'fix-wordpress':
  command => 'bash -c "sed -i s/class-wp-locale.phpp/class-wp-locale.php/ \
/var/www/html/wp-settings.php; service apache2 restart"',
  path    => '/usr/bin:/usr/sbin:/bin'
}