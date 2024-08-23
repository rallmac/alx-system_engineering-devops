# Ensure the directory exists with correct permissions
file { '/var/www/html':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Ensure the index.php file exists with the correct content and permissions
file { '/var/www/html/index.php':
  ensure  => file,
  content => "<?php\nphpinfo();\n?>",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Restart Apache to apply changes
service { 'apache2':
  ensure => running,
  enable => true,
  subscribe => File['/var/www/html/index.php'],
}
