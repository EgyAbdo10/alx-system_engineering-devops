# fix the web stack 3

exec {
    command => 'sed -i 's/phpp/php/g' wp-settings.php',
}

# exec { 'create_file':
#    command => '/usr/bin/touch /var/www/html/index.html &&
#    /usr/bin/touch /var/www/html/index.cgi &&
#    /usr/bin/touch /var/www/html/index.pl &&
#    /usr/bin/touch /var/www/html/.maintenance &&
#    /usr/bin/touch /var/www/html/wp-content/languages &&
#    /usr/bin/touch /var/www/html/wp-content/db.php &&
#    /usr/bin/touch /var/www/html/wp-content/object-cache.php &&
#    /usr/bin/touch /var/www/html/wp-includes/class-wp-locale.phpp &&
#    /etc/init.d/apache2 restart',
# }
