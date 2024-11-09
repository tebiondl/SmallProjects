import random
import copy

class Node():
    
    def __init__(self, node_name):
        self.conections = []
        self.node_name = node_name
        self.seen = False
        
    def connect_to(self, node_out, cost):
        new_con = Connections(node_in=self, node_out=node_out, cost=cost)
        self.conections.append(new_con)
        
    def calculate_h(self, final_node):
        # Calculates the sum of the cost to the destination, then selects a random num between that number and the third part of it (modify)
        # Use dynamic programming to get the greediest way to destination (only cost)
        memo = {}
        memo[0] = 0
        
        i = 1
        current_node = self
        found = False
        while not found:
            if len(current_node.conections) > 0:
                for con in current_node.conections:
                    if memo.get(i, float('inf')) > con.cost:
                        memo[i] = con.cost + memo[i-1]
                        current_node = con.node_out
                        if current_node.node_name == final_node.node_name:
                            # Found final node
                            found = True
                i += 1
            else:
                print("No more nodes available in node " + current_node.node_name)
                return -1
            
        i -= 1
        # Generate random num between memo[i] and memo[i]/3
        
        return random.uniform(memo[i], memo[i]/3)
        
class Connections():
    def __init__(self, node_in, node_out, cost):
        self.node_in = node_in
        self.node_out = node_out
        self.cost = cost
        
class Path():
    def __init__(self, path=None):
        if path is None:
            self.nodes = []
            self.current_value = 0
        else:
            self.nodes = copy.deepcopy(path.nodes)
            self.current_value = path.current_value
        
    def duplicate(self):
        return Path(self)
    
    def add_node(self, node, val):
        self.nodes.append(node)
        self.current_value += val
        
    def get_last_node(self):
        return self.nodes[-1]
    
    def print_path(self):
        print("")
        print("Path Printed: ")
        for node in self.nodes:
            print("Node :" + node.node_name)
        print("")
        
class AStar():
    
    def __init__(self):
        pass
    
    def run_algorithm(self, start_node, end_node):
        # Start node is S and end node is Z
        temporal_paths = []
        final_paths = []
        found = False
        current_node = start_node
        current_path = Path()
        current_path.add_node(current_node, 0)
        temporal_paths.append(current_path)
        final_node = end_node
        
        counter = 0
        
        while not found:
            if current_node.seen:
                node_obtained = False
                for path in temporal_paths:
                    if not path.get_last_node().seen:
                        current_node = path.get_last_node()
                        node_obtained = True
                
                if not node_obtained:
                    print("Final path cant be obtained with this graph")
                    found = True

            if not found:
                # Add to temporal paths all new paths for the current node   
                for con in current_node.conections:
                    new_path = current_path.duplicate()
                    h = current_node.calculate_h(final_node)
                    if h < 0:
                        current_node.seen = True
                        break
                    else:
                        res = con.cost + h
                        new_path.add_node(con.node_out, res)
                        temporal_paths.append(new_path)
                        current_node.seen = True
                    
                # Select best path to continue there
                    
                best_value = float("inf")
                deleted_paths = []
                for path in temporal_paths:
                    if path.get_last_node().node_name == final_node.node_name:
                        # Found the last node with X path
                        final_paths.append(path)
                        deleted_paths.append(path)
                        continue
                    if path.get_last_node().seen:
                        deleted_paths.append(path)
                        continue
                    if path.current_value < best_value:
                        best_value = path.current_value
                        current_node = path.get_last_node()
                        current_path = path
                            
                # Delete paths with last nodes already seen
                for path in deleted_paths:
                    if path in temporal_paths:
                        temporal_paths.remove(path)
        
                if len(temporal_paths) == 0:
                    if len(final_paths) > 0:
                        print("Finished algorithm")
                        found = True
                    else:
                        print("Can't find a path to the end with this graph")
            counter += 1
            
            if counter >=500:
                break
        
        print("POSSBILE FINAL PATHS") 
        # Final paths
        for path in final_paths:
            path.print_path()
            
        best_path = final_paths[0]
        # Select the shortest path
        for path in final_paths:
            if path.current_value < best_path.current_value:
                best_path = path
        
        return best_path