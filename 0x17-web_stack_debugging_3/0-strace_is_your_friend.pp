# fix the webstack 3

exec { 'create_file':
    command => 'usr/bin/touch /var/www/html/index.html'
}

exec { 'create_file_2':
    command => 'usr/bin/touch /var/www/html/index.cgi'
}

exec { 'create_file_3':
    command => 'usr/bin/touch /var/www/html/index.pl'
}

exec { 'create_file_4':
    command => 'usr/bin/touch /var/www/html/.maintenance'
}

exec { 'create_file_5':
    command => 'usr/bin/touch /var/www/html/wp-content/languages'
}

exec { 'create_file_6':
    command => 'usr/bin/touch /var/www/html/wp-content/db.php'
}

exec { 'create_file_7':
    command => 'usr/bin/touch /var/www/html/wp-content/object-cache.php'
}

exec { 'create_file_8':
    command => 'usr/bin/touch /var/www/html/wp-includes/class-wp-locale.phpp'
}
