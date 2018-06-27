'''
Thomas Vermeersch
June 27, 2018
A Program that takes a json object as input and outputs the path to every terminal value in the object
'''
import sys
import json

'''
Method that recursively traverses the dictionary, taking note of its current path.
Once it finds a terminal value, it adds the current path and value to a new dictionary
'''
def path(json, prev, our_dict):
	for k, v in json.items():
		#If we find another subdictionary, go deeper while updating the path thus far
	    if isinstance(v, dict):
	    	prev += k + "."
	    	path(v, prev, our_dict)
	    #If the value is a terminal value, then we simply update the path and add it to our final dictionary
	    else:
	    	key = prev+k
	    	our_dict[key] = v

def main():
	#parse json into python dictionary
	data = json.load(sys.stdin)
	#set prev as empty string, to symbolize the start of the path for our method
	prev = ""
	our_dict = {}
	#call method to get paths within our dictionary and update our_dict
	path(data, "", our_dict)
	#output our new dictionary with formatting
	print(json.dumps(our_dict, indent=4))

main()