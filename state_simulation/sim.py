"""
Clock - State Simulation
===================
Author: Chase August Lotito
Created: 12/11/2024
Version: 0.0.1
Description:
    For building the clock out of hardware,
    I want to run a simple test simulation for
    the general state machine logic.

Usage:
   

Dependencies:
    - time


License:
    Personal Use Only

Notes:
    - This script is a work-in-progress.
    - Feedback or suggestions are welcome!
"""

import time 



# create binary digit for hours, minutes, seconds
am_pm_toggle = 0
hh = [0b0000,0b0000]
mm = [0b0000,0b0000]
ss = [0b0000,0b0000]

def update_time(hh, mm, ss, am_pm_toggle):
    s0 = 1
    s1 = 0
    
    # increment seconds
    ss[s0] += 0b0001
    
    # if 1 seconds place overflows to 10, reset SS[0] to 0,
    # then increment 10 seconds place
    if (ss[s0] == 0b1010):
        ss[s0] = 0b0000
        ss[s1] += 0b0001
    # if 10 seconds place overflows to 6, reset SS[0,1] to 0,
    # then increment 1 minutes place
    elif (ss[s1] == 0b0110):
        ss[s0] = 0
        ss[s1] = 0
        mm[s0] += 0b0001
    # if 1 minutes place overflows to 10, reset MM[0] to 0,
    # then increment 10 minutes place
    elif (mm[s0] == 0b1010):
        mm[s0] == 0b0000
        mm[s1] += 0b0001
    # if 10 minutes place overflows to 6, reset MM[0,1] to 0,
    # then increment 1 hours place 
    elif (mm[s1] == 0b0110):
        mm[s0] = 0
        mm[s1] = 0
        hh[s0] += 0b0001
    # if 1 hours place overflows to 10, reset HH[0] to 0,
    # then increment 10 hours place,
    # but this only happens if HH[1]=0b0000, if HH[0b0001]
    # then the reset happens if HH[0]=0b0011
    elif (hh[s0] == 0b1010):
        hh[s0] == 0
        hh[s1] += 0b0001
    elif (hh[s0] == 0b0011 and hh[s1] == 0b0001):
        hh[s0] = 0
        hh[s1] = 0
        # if this happens, AM -> PM or PM -> AM
        ampm_toggle = ~am_pm_toggle
    

    return hh, mm, ss, am_pm_toggle

def print_time(hh, mm, ss, am_pm_toggle):
    s0 = 1
    s1 = 0

    suffix = "AM" if ~am_pm_toggle else "PM"

    print(f'{hh}:{mm}:{ss} ', suffix)
    time.sleep(0.05)
    hh, mm, ss, am_pm_toggle = update_time(hh, mm, ss, am_pm_toggle)
    print_time(hh, mm, ss, am_pm_toggle)


# start clock
print_time(hh, mm, ss, am_pm_toggle)