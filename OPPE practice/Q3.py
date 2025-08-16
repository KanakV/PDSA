'''
write function build_roads(cost_List) that accept a weighted adjacency list cost_list 
in the following format, 
cost_list = {source_city:[(destination_city,cost),........]} 
the function returns the minimum construction cost to connect all n cities. 

input : 5 
[(0,1,3),(0,3,7),(0,4,8),(1,3,4),(1,2,1),(2,3,2),(3,4,3)] 

output : 9
'''

# Implement Prim's Algo
def build_roads(n, cost_List):
    
    # Find smallest weight road
    cost_sorted = sorted(cost_List, key=lambda x:x[2])

    # Add origin as starting node
    # Peform Prim's algo from starting node


n = 5 
L = [(0,1,3),(0,3,7),(0,4,8),(1,3,4),(1,2,1),(2,3,2),(3,4,3)] 
build_roads(n, L)