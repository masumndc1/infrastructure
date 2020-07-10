# checking partition and their size
each ( $facts['partitions'] ) |$name, $capacity | {
  notice("partition ${name} has size of ${capacity['size']}")
}
