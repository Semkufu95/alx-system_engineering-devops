# Installing a package by using puppet

class flask {
# 
package { 'pySMART':
ensure   => 'installed'
provider => 'pip3'
}
}