# installing flask using pip3

package { 'flask':
ensure          => 'installed',
name            => 'flask',
install_options => ['--version', '2.1.0'],
provider        => 'pip3',
}