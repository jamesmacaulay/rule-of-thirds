#!/usr/bin/env ruby

def avg_distance_between(a1,a2)
  distances = []
  a1.each_with_index do |v,i|
    distances << (a2.index(v) - i).abs
  end
  distances.inject {|sum,d| sum + d} / distances.length.to_f
end

h1 = [3, 7, 8, 12, 16, 19, 6, 2, 5, 11, 13, 18, 4, 9, 15, 20, 14, 17, 1, 10]
h2 = [8, 19, 16, 12, 13, 1, 5, 3, 7, 14, 2, 4, 6, 9, 10, 17, 20, 11, 15, 18]
avg = [8, 19, 16, 12, 3, 7, 5, 13, 2, 6, 11, 1, 4, 14, 18, 9, 20, 17, 15, 10]
comp  = [1, 19, 12, 7, 11, 14, 17, 5, 16, 2, 8, 3, 18, 6, 13, 4, 9, 10, 15, 20]

rand_avgs = []
10000.times do
  rand_avgs << avg_distance_between(h1, (1..20).to_a.sort_by{rand})
end
avg_avg = rand_avgs.inject {|sum,d| sum + d} / rand_avgs.length.to_f
puts "expected average distance for a random algorithm: #{avg_avg}"


puts "avg_distance_between(h1,h2): " + avg_distance_between(h1,h2).to_s
puts "avg_distance_between(comp,h1): " + avg_distance_between(comp,h1).to_s
puts "avg_distance_between(comp,h2): " + avg_distance_between(comp,h2).to_s
puts "avg_distance_between(avg,h1): " + avg_distance_between(avg,h1).to_s
puts "avg_distance_between(avg,h2): " + avg_distance_between(avg,h2).to_s
puts "avg_distance_between(avg,comp): " + avg_distance_between(avg,comp).to_s

# output:

# expected average distance for a random algorithm: 6.64578999999997
# avg_distance_between(h1,h2): 4.4
# avg_distance_between(comp,h1): 5.3
# avg_distance_between(comp,h2): 4.5
# avg_distance_between(avg,h1): 2.3
# avg_distance_between(avg,h2): 2.3
# avg_distance_between(avg,comp): 4.3