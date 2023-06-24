# Execute pkill cmd
exec { 'pkill killmenow':
    path => 'usr/bin:/bin',
}