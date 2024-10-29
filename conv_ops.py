# conv_ops.py

# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
# Description: Outputs the shape and operation count of a convolution layer

# Parameters:
# c_in: input channel 
# h_in: input height 
# w_in: input width 
# n_filt: number of filters in the convolution layer
# h_filt: filter height 
# w_filt: filter width 
# s: stride of convolution filters
# p: amount of padding on each of the four input map sides

# Output:
#  Shape and operation count of a convolution layer

# Written by Maxwell Oross
# Other contributors: None

# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math
import sys


# initialize script arguments
c_in = float(sys.argv[1])
h_in = float(sys.argv[2])
w_in = float(sys.argv[3])
n_filt = float(sys.argv[4])
h_filt = float(sys.argv[5])
w_filt = float(sys.argv[6])
s = float(sys.argv[7])
p = float(sys.argv[8])

# parse script arguments
if len(sys.argv)==9:
  c_in = float(sys.argv[1])
  h_in = float(sys.argv[2])
  w_in = float(sys.argv[3])
  n_filt = float(sys.argv[4])
  h_filt = float(sys.argv[5])
  w_filt = float(sys.argv[6])
  s = float(sys.argv[7])
  p = float(sys.argv[8])
else:
  print(\
   'Usage: '\
   'python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p'\
  )
  exit()

#Size of output
h_out = ((h_in + 2*p - h_filt)/s) + 1
w_out = ((w_in + 2*p - w_filt)/s) + 1
c_out = n_filt
adds = h_out * w_out * c_in * h_filt * w_filt * (n_filt-1) 
muls = h_out * w_out * c_in * h_filt * w_filt * n_filt
divs = 0

# Display final answers
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed


