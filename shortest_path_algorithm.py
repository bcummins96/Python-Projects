#A graph is called a weighted graph when its edges are associated with weights, representing a distance, time or other quantitative value.
#here we use dictionaries to store connections (edges) between nodes.

#To represent a weighted graph you can modify your dictionary, using a list of tuples for each value.
# The first element in the tuple will be the connected node, and the second element will be an integer number indicating the distance.

#The algorithm will start at a specified node. Then it will explore the graph to find the shortest path between the starting node, or source, and all the other nodes.
# To keep track of the visited nodes, you need a list of all the nodes in the graph. Once a node is visited, it will be removed from that list.

#establish the graph
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# function is going to explore all the nodes connected to the starting node. It will calculate the shortest 
# paths for all of them. Then, it will remove the starting node from the unvisited nodes.
# Next, the closest neighbor node will be visited and the process will be repeated until all the nodes are visited.

#accepts 3 arguments: the graph, which node to start at, and which is the endpoint we are finding the shortest path to.
def shortest_path(graph, start, target = ''):

    #establish the nodes we haven't visited yet. forms a list of the dictionary entries, stores as tuples
    unvisited = list(graph)

    #distance to each node that is not the starting node is infinity at first
    distances = {node: 0 if node == start else float('inf') for node in graph}

    #this will create a dictionary based on an existing graph entry, assigning a blank list as the value to each node which are the keys (A,B,C, etc.)
    paths = {node: [] for node in graph}

    #if we try to append to paths, its a dicitonary so we cant. but if we specify that we want the list in the dicitonary, then we can
    paths[start].append(start)
    
    #as long as unvisited is True; that is, there are still entries in the unvisited list 
    while unvisited:

        #key=distances.get as the second argument to your min() call. In this way, the comparison will 
        # take place depending on the value each unvisited list item has inside the distances dictionary.
        current = min(unvisited, key=distances.get)

        for node, distance in graph[current]:

            #an if statement to check if the distance of the neighbor node (the second item in the processed tuple) 
            #plus the distance of current is less than the currently known distance of the neighbor node (the first item in the processed tuple).
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]

                if paths[node] and paths[node][-1] == node:
                    #When a shorter distance is found for a neighbor node, paths[current] 
                    # gets assigned to the neighbor node path, paths[node]. since they are 
                    # refering to the same list, we slice [:] paths[current] to avoid saving wrong
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            #skips to the next so we don't include our first node
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A','F')


































#old statements
#for node in graph:
#        unvisited.append(node)
#        if node == start:
#            distances[node] = 0
#        else:
#            distances[node] = float('inf')
#    print(f'Unvisited: {unvisited}\nDistances: {distances}')

#    paths = {node: [] for node in graph}







#At the beginning, all the other nodes in the graph are considered to be at infinite distance from the source node, because the distance has not been determined yet.
#Create an else clause and assign an infinite value to the node in the distances dictionary. For that, use the float() function with the string 'inf' as argument to 
# generate a floating point number representing the positive infinity.