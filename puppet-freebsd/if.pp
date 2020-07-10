# example of if/elsif/else block


if ( $facts['os']['family'] == 'FreeBSD' )
  and ( $facts['os']['name'] == 'FreeBSD' )
    and ( $facts['os']['release']['major'] == '12' ) {
      notify { 'whatOS':
         message => "You Are Running Latest FreeBSD"
      }
}


elsif ( $facts['os']['family'] == 'FreeBSD' )
  and ( $facts['os']['name'] == 'FreeBSD' )
    and ( $facts['os']['release']['major'] <= '12' ) {
      notify { 'whatOS':
        message => "You Need to Update FreeBSD"
      }
}
