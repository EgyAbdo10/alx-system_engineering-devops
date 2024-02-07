# installing flask using pip3

package {'pip':
ensure => 'installed',
name   => 'python3-pip'
}

package { 'flask':
ensure   => 'installed',
name     => 'flask==2.1.0',
provider => 'pip3',
}

package { 'werkzeug':
ensure   => 'installed',
name     => 'werkzeug',
provider => 'pip3',
}