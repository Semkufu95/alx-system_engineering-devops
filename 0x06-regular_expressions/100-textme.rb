#!/usr/bin/env ruby
#A regex to print text logs

puts ARGV[0].scan(/\[from:(\+?\w*)\]\s\[to:(\+?\w*)\s\[flags:(\S*)\]/).join(',')
