"""
Problem 1: mostCommonNames(names) in O(N)

You have seen mostCommonName using list that runs in O(N^2). Now, let's do 
better than O(N^2) and write mostCommonNames in O(N)!
Here is the problem statement again:
Write the function mostCommonName, that takes a list of names (such as ["Jane", 
"Aaron", "Cindy", "Aaron"], and returns the most common name in this list (in 
this case, "Aaron"). If there is more than one such name, return a set of the 
most common names. So mostCommonName(["Jane", "Aaron", "Jane", "Cindy", 
"Aaron"]) returns the set {"Aaron", "Jane"}. If the set is empty, return None. 
Also, treat names case sensitively, so "Jane" and "JANE" are different names. 
Your solution should runs in O(N). 
"""
def mostCommonNames(names):
    return [] # implement your solution here!

def testMostCommonNames():
    print("Testing mostCommonNames...", end="")
    assert(mostCommonNames(["Jane", "Aaron", "Cindy", "Aaron"]) == "Aaron")
    assert(sorted(mostCommonNames(["Jane", "Aaron", "Jane", "Cindy", "Aaron"])) 
            == ["Aaron", "Jane"])
    assert(mostCommonNames(["Cindy"]) == "Cindy")
    assert(sorted(mostCommonNames(["Jane", "Aaron", "Cindy"])) == 
                                                    ["Aaron", "Cindy", "Jane"])
    assert(mostCommonNames([]) == None)
    print("Passed!")

# testMostCommonNames() # uncomment to test your solution! 

"""
Problem 2: mostCommonCities(cityMap)

Background: for this problem, we will say that a cityMap is a dictionary mapping 
a state (a lowercase string)to some cities in that state (a set of lowercase 
strings). For example: 

cityMap = {                                                               
    "maine" : { "madison" },                                                              
    "ohio"  : { "akron", "toledo", "dayton", "madison"},                                                                 
    "iowa"  : { "ames", "dayton", "akron" },                                                              
    "indiana": { "akron", "madison" }                                                       
} 

With this in mind, write the function mostCommonCities that takes a cityMap as 
just described and returns a sorted list of all the cities that occur the most 
in that map. If we use the cityMap in the example above, this would return 
["akron",   "madison"].
"""
def mostCommonCities(cityMap):
    return [] # implement your solution here!

def testMostCommonCities(): 
    cityMap = {                                                               
        "maine" : {"madison"},                                                              
        "ohio"  : {"akron", "toledo", "dayton", "madison"},                                                                 
        "iowa"  : {"ames", "dayton", "akron"},                                                              
        "indiana": {"akron", "madison"}                                                      
    }
    print("Testing mostCommonCities...", end="")
    assert(sorted(mostCommonCities(cityMap)) == ["akron", "madison"])
    print("Passed!")

# testMostCommonCities() # uncomment to test your solution!

"""
Bonus: Write mostCommonNames in O(NlogN)
"""
