#Creating a manifest named killme now

exec { 'pkill -f killmenow':
  path  => '/usr/bin/:/usr/local/bin/:/bin/:/usr/sbin/:/sbin/',
}
