# change security limits
exec { 'Change soft limit':
  command  => 'sudo sed -i "s/holberton\ssoft.*/holberton\tsoft\tnofile\t200000/" /etc/security/limits.conf',
  provider => shell,
}

exec { 'Change hard limit':
  command  => 'sudo sed -i "s/holberton\shard.*/holberton\thard\tnofile\t200000/" /etc/security/limits.conf',
  provider => shell,
}