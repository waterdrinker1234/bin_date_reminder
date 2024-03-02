# python application to automatically get bin dates from the Cambridge bin dates website. 
# run a configuration utility to set up the initial postcode, along with a selectable list of all addresses 
# under this postcode that the user can make a selection from. these are the two user variables that will be input into website
# run automatically every morning and afternoon if machine is on, notifying the 
# display graphics of a bin being hauled with the appropriate bin color for the nearest date.
# optional synth voice to read the bin dates, like bonzibuddy, although it should work without the voice if external packages are required
# go to website, go through html looking for correct entry elements, then input the postcode and do the search.
# get required info and return it back to the program