# Development outline:
# installer > config run > request data > get data > run in the background > notify user of dates or changes > repeat
# add install and usage instructions somewhere. maybe an install/setup wizard with a directory and optionals?
# run a configuration utility to set up the initial postcode, along with a selectable list of all addresses 
# under this postcode that the user can make a selection from. these are the two user variables that will be input into website
# run automatically every morning and afternoon if machine is on, notifying the 
# display graphics of a bin being hauled with the appropriate bin color for the nearest date.
# optional synth voice to read the bin dates, like bonzibuddy, although it should work without the voice if external packages are required
# go to website, go through html looking for correct entry elements, then input the postcode and do the search.
# get required info and return it back to the program
# allow user to click the bin and go to the website immediately as well! Park the bin around.

import sys
import time 
import json # read last checked...



# make this file wait? for example config file needs to be run only when exe is clicked.
# gui displayed only when user clicks again, auto request should be done only once every 12hrs or 
# immediately if time has exceeded 12hrs. notification should be able to listen in the background somehow...

from bin.config_gui import *


def main():
    prefs = set_user_configuration()
    print(prefs)

if __name__ == "__main__":
    main()