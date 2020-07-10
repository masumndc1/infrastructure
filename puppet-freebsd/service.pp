#keeping service up

package { 'puppet':
  ensure => 'latest',
  before => Service['puppet'],
}

service { 'puppet':
  enable  => 'true',
  ensure  => 'running',
  require => Package['puppet'],
  tag     => 'puppet',
}
