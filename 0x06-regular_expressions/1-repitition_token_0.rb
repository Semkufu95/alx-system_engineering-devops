#!/usr/bin/env ruby
#A Ruby script that accepts one argument and pass it to regular expression matching methhod\

puts ARGV[0].scan(/hbt{2,5}n/).join
