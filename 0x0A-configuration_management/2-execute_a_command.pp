exec { 'kill_killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
  path    => '/usr/bin/:/usr/local/bin/:/bin/:/usr/sbin/:/sbin/',
}
