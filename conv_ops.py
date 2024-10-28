# conv_ops.py
#
# Usage: python3 script_name.py arg1 arg2 ...
# Text explaining script usage
# Parameters:
# arg1: description of argument 1
# arg2: description of argument 2
# ...
# Output:
# A description of the script output
#
# Written by Erik Judy
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
# import Python modules
# e.g., import math # math module
import sys
import math
# "constants"
# helper functions
## function description
# def calc_something(param1, param2):
# pass
# initialize script arguments
c_in=float('nan')
h_in=float('nan')
w_in=float('nan')
n_filt=float('nan')
h_filt=float('nan')
w_filt=float('nan')
s=float('nan')
p=float('nan')
if len(sys.argv)==9:
    c_in = float(sys.argv[1])
    h_in = float(sys.argv[2])
    w_in  = float(sys.argv[3])
    n_filt = float(sys.argv[4])
    h_filt = float(sys.argv[5])
    w_filt = float(sys.argv[6])
    s=float(sys.argv[7])
    p=float(sys.argv[8])
else:
    print(\
     'Usage: '\
     'python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p'\
    )
    exit()
# write script below this line
h_out = math.floor((h_in + 2*p - h_filt)/s + 1)
w_out = math.floor((w_in + 2*p - w_filt)/s + 1)
c_out = n_filt
adds = n_filt*h_out*w_out*c_in*h_filt*w_filt
muls = n_filt*h_out*w_out*c_in*h_filt*w_filt
divs = 0

print(int(c_out)) 
print(int(h_out)) 
print(int(w_out)) 
print(int(adds)) 
print(int(muls))  
print(int(divs))  