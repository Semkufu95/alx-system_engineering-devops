# A puppet script that kills and executes a command

exec { 'killmenow':
command   => 'pkill killmenow',
path      => '/usr/bin',
logoutput => 'true',
}