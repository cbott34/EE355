# See if if you come come up with an example of a dictionary
# that has tuples and lists as well. Do some queries to show how it works.

t = (1,2,3,5,7,11,13,17) # initialize tuple
l = [1,2,3,4,5,6,7,8] # initialize list
d = dict(zip(l,t)) # combine list and tuple in dictionary using zip
print(d)
print(d[7]) 
print(d[2])