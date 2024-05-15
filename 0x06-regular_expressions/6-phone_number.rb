#!/usr/bin/env ruby
#A regular expression that searches for phone numbers of 10 digits

puts ARGV[0].scan(/^\d{10}/$).join
