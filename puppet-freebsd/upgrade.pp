#updrading freebsd daily, nightly
schedule { 'nightly':
  period => 'daily',
  range  => '21 - 22',
}

exec { '/usr/sbin/pkg upgrade -y':
  schedule => 'nightly',
}
