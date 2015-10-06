
# File Operations %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import pickle

# def To_File(list):  # deprecated
#     try:
#         with open(outputfile, "w") as file:
#             pickle.dump(list, file)
#     except IOError, err:
#         print err
#         yes = input("want to create the file 'output_list' to dump data y/n: ")
#         if yes == 'y':
#             with open("output_list", "w") as file:
#                 pickle.dump(list, file)
#             return
#         else:
#             import sys
#             sys.exit()

def to_file(data, outputfile):
    if outputfile:
        file = open(outputfile, "w")
        pickle.dump(data, file)
        file.close()
    else: print "no outputfile indicated; use option -o [filename]"
    return

#def from_file(data, outputfile):
#   if inputfile:
#       file = open(inputfile, "r")
#       list_of_exceptionals = pickle.load(file)
#       file.close()
#    else: print"no inputfile indicated; use option -i [filename]"
#    return
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import timeit

#decorator
def timer(fun):
	"""
	usage:
	@timer
	def whatever():
	    pass
	"""
	def wrapper(*args, **kwargs):
		start = timeit.default_timer()
		fun(*args, **kwargs)
		stop = timeit.default_timer()
		print "time: ", stop-start
		return

	return wrapper



import sys
INF = sys.maxint # even bigger: float('inf')
