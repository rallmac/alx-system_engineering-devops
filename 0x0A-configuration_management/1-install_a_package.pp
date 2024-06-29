exec { 'install_flask':
command => 'pip3 install flask==2.1.0',
unless  => 'pip3 show flask | grep Version | grep 2.1.0',
path    => '/usr/bin/:/usr/local/bin/:/bin/:/usr/sbin/:/sbin/',
}
