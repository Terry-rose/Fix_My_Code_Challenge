#!/usr/bin/ruby

def sort_args(args)
  """
  Function to sort arguments
  """
  args.map(&:to_i).sort.each { |arg| puts arg }
end

sort_args(ARGV)

