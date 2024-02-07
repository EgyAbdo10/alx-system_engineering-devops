# installing flask using pip3

package { 'flask':
ensure   => 'installed',
name     => 'Flask==2.1.0',
provider => 'pip3',
}