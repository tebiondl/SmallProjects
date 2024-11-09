from AStar import Node, Connections, AStar

def start_a_star():
    # Create Astart object
    a_star = AStar()
    
    # Create nodes
    node_s = Node("S")
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_z = Node("Z")
    
    # Create connections between nodes
    node_s.connect_to(node_a, 1)
    node_s.connect_to(node_z, 15)
    node_a.connect_to(node_b, 2)
    node_a.connect_to(node_c, 1)
    node_b.connect_to(node_d, 5)
    node_c.connect_to(node_d, 3)
    node_c.connect_to(node_z, 3)
    node_d.connect_to(node_z, 2)
    
    result_path = a_star.run_algorithm(node_s, node_z)
    
    print("FINAL RESULT")
    result_path.print_path()
    
start_a_star()