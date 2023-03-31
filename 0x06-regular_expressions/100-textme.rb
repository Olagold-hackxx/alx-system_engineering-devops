#!/usr/bin/env ruby

sender, receiver, flags = ARGV[0].match(/from:(\+?\w+)?\].*to:(\+?\w+)?\].*flags?:([-:\d]+)?/).captures

p "#{sender}, #{receiver}, #{flags}"