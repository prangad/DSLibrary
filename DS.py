#################################################
# Written by: Dylan Pranga                      #
# WINTER 2020 MTH 325 02                        #
# Grand Valley State University                 #
#################################################

# Degree sequence method.
# Parameters: The dictionary of vertices, and their adjacent vertices.
# Returns: The >sanitized< degree sequence of the dictionary.
# This method sanitizes bad input without throwing errors. (Negative integers)
def degree_sequence(dict):
  degSeq = [];                                    # Initialize a new list.

  for vert in dict:                               # For every vertex in the dictionary...
    if (len(dict.get(vert)) >= 0):                # Append to the degree sequence.
      degSeq.append(len(dict.get(vert)));         # (If the vertex has non-negative degree)
  
  degSeq.sort(reverse = True);                    # Sort the degree sequence.
  return degSeq;                                  # Return the sorted degree sequence.


# Erdos Gallai Method.
# (We can assume the provided degree sequence is non-negative and in a non-increasing order.)
def Erdos_Gallai(degSeq):
  if (sum(degSeq) % 2 != 0):                      # Checks the initial condition, whether or not the degree sum is even.
    return False;                                 # If the degree sum is not even, then return false.

  for k in range(1, len(degSeq)+1):               # For every k, 1 to the length of the degree sequence...
    degSum = sum(degSeq[0:k]);                    # Sum up the degree sequence for index 0 to k.
    partSum = k * (k-1);                          # Starts the partial sum from k * (k-1).
    
    for j in range(k+1, len(degSeq)+1):           # As k increases, modify and sum up the partial sum.
      partSum += min(k, degSeq[j-1]);             # Add the lesser value between k and the degree sequence index to the partial sum.
      
    if degSum > partSum:                          # If the degree sum (for indices 0 to k) is less than the partial sum...
      return False;                               # Return false.
    
  return True;                                    # If conditions were not met to return false, return true.

# is_proper Method
# Parameters: The graph represented by a dictionary, and the potential coloring of the vertices represented as a dictionary.
# Returns: A boolean value, whether or not the potential coloring is a valid coloring.
# Description: This method checks to see if a given coloring is a valid coloring of the given graph.
# The method will return true if the coloring is valid, and not necessarily the most efficient coloring.
def is_proper(graph, coloring):
  if (len(graph) != len(coloring)                         # If the graph's vertices and the vertices in the coloring are different...
      or len(graph) == 0 or len(coloring) == 0):          # or if they are empty...
    return False;                                         # Then return False. 
  for vert in graph:                                      # For every vertex in the graph...
    for adjacent in graph.get(vert):                      # Check all of the adjacent vertices...
      if (coloring.get(vert) == coloring.get(adjacent)):  # If the adjacent vertex and the given vertex share the same color...
        return False;                                     # return false.
  return True;                                            # After checking all vertices for adjacent vertices with the same color, return true.
  
# greedy Method
# Parameters: The graph represented by a dictionary, and the order in which to color the vertices represented as a list.
# Returns: A dictionary, the most efficient vertex coloring (when done in the given order.) in the order of coloring.
# Description: This method takes a graph and an order in which to color the vertices of the graph, and returns
# the most efficient coloring (when colored in the specified color).
def greedy(graph, vertices):
  coloring = {};                                          # Initialize a new dictionary for the coloring.
  if (len(graph) != len(vertices)                         # If the graph's vertices and the vertices in the coloring order are different...
      or len(graph) == 0 or len(vertices) == 0):          # or if they are empty...
    return coloring;                                         # Return the empty dictionary.
  for vert in vertices:                                   # For every vertex (in order) in the ordered set...
    color = 1;                                            # Start with color 1.
    valid = False;                                        # Assume the color is not valid.
    while (not valid):                                    # Prove that the color is valid by...
      valid = True;                                       # Assuming the color is valid until proven otherwise.
      for adjacent in graph.get(vert):                    # For every vertex adjacent to the vertex being colored...
        if (color == coloring.get(adjacent)):             # Check to see if the adjacent vertex has the color being attempted.
          valid = False;                                  # If it does, then the coloring is not valid. (We'll try another color.)
          color += 1;                                     # Go to the next color, and...
          break;                                          # Break out of the loop to try again.
    coloring[vert] = color;                               # If all adjacent vertices have been checked, then the coloring is valid.
  return coloring;                                        # Once all of tghe vertices have been colored, return the coloring.
     
#################################################
# BEGIN INDEPENDENT TESTING                     #
#################################################
# print(degree_sequence({"A" : ["B", "C"], "B" : ["A", "C"], "C" : ["A", "B"]}))
# print(degree_sequence({"A" : ["B", "C"], "B" : ["A", "C"], "C" : ["A", "B", "D"], "D" : ["C"]}))

# print(Erdos_Gallai([3,3,3,3,3]))
# print(Erdos_Gallai([3,3,2,2,2,2]))
# print(Erdos_Gallai([2,2,2,2,2,2,2]))

# print(is_proper({"A" : ["B", "C"], "B" : ["A", "C"], "C" : ["A", "B"]}, {"A" : 1, "B" : 2, "C" : 3}))
# print(is_proper({"A" : ["B", "C"], "B" : ["A", "C"], "C" : ["A", "B"]}, {"A" : 1, "B" : 1, "C" : 3}))
# 
# print(greedy({"A" : ["B","C"],"B" : ["A"],"C" : ["A"]},["A","B","C"]))
# print(greedy({"A" : ["B"],"B" : ["A","C"],"C" : ["B","D"],"D" : ["C"]}, ["A","D","B","C"]))
# print(greedy({"A" : ["B"],"B" : ["A","C"],"C" : ["B","D"],"D" : ["C"]}, ["A","B","C","D"]))
#################################################
# END OF INDEPENDENT TESTING                    #
#################################################