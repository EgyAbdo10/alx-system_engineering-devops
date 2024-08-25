# fix the broken webstack by replacing the max number of file descriptors
exec {'change max file descriptors':
    command => "sed -i 's/15/4096/' /etc/default/nginx && service nginx restart"
}