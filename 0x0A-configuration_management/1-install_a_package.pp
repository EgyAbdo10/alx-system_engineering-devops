# install flask package

package {'python3.8':
    ensure => 'present',
}

package {'python3-pip':
    ensure => 'present',
}

package {'flask':
    ensure   => '2.1.0',
    require  => Package['python3-pip'],
    provider => 'pip',
}

package {'werkzeug':
    ensure   => '2.1.1',
    name     => 'werkzeug',
    require  => Package[python3-pip],
    provider => 'pip',
}

