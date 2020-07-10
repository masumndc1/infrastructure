# manage user

package {'zsh':
  ensure => 'latest',
  before => User['masum'],
}

user { 'masum':
  shell   => '/usr/local/bin/zsh',
  require => Package['zsh'],
}

