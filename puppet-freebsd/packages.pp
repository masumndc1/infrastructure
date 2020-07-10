$packages = [
  'vim',
  'git',
  'puppet5',
  'iftop',
  'htop',
  'zsh',
]

if ( $facts['os']['family'] == 'FreeBSD' ) 
  and ( $facts['os']['name'] == 'FreeBSD' ) {
    package { $packages:
      ensure => 'latest',
      tag    => 'pkg',
    }
}

