#!/usr/bin/env rubiy
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
