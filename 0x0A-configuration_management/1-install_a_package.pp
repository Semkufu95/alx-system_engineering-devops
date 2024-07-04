# Installing a package by using puppet

class flask {
# 
package { 'flask':
ensure   => '2.1.0'
provider => 'pip3'
}
}