notify { 'MD5_hash':
  message => md5( $facts['fqdn'] )
}
# Include the MD5 hash in the result string
$result = "The MD5 hash for the node name is ${md5( $facts['fqdn'] )}"

notify { 'nodename_hash':
  message => "$result"
}

