# fix the web stack 3

exec { 'create_file':
    command => '/usr/bin/touch /var/www/html/index.html &&
    /usr/bin/touch /var/www/html/index.cgi &&
    /usr/bin/touch /var/www/html/index.pl &&
    /usr/bin/touch /var/www/html/.maintenance &&
    /usr/bin/touch /var/www/html/wp-content/languages &&
    /usr/bin/touch /var/www/html/wp-content/db.php &&
    /usr/bin/touch /var/www/html/wp-content/object-cache.php &&
    /usr/bin/touch /var/www/html/wp-includes/class-wp-locale.phpp',
}
