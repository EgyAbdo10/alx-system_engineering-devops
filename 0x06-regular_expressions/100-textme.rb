#!/usr/bin/env ruby
text = ARGV[0]
# (?<sender>(?<=\[from:).*?(?=\]))(?<receiver>(?<=\[to:).*(?=\]))
sender = text.match(/(?<sender>(?<=\[from:).*?(?=\]))/)
receiver = text.match(/(?<receiver>(?<=\[to:).*?(?=\]))/)
flags = text.match(/(?<flags>(?<=\[flags:).*?(?=\]))/)
puts "#{sender},#{receiver},#{flags}"