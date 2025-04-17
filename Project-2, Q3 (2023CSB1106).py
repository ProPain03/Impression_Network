import pandas as pd  
import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np  
import random 
import math  

def create_graph(file_path):
    """Create a directed graph from a CSV file."""
    G = nx.DiGraph()  # Create an empty directed graph
    df = pd.read_csv(file_path)  # Read CSV file into a pandas dataframe
    names = df['Email Address'].tolist()  # Extract values from 'Email Address' column
    G.add_nodes_from(names)  # Add nodes to the graph

    for i in range(len(df)):
        impressions = list(df.iloc[i])
        for j in range(1, len(impressions)):
            if impressions[j] != float('nan'):
                G.add_edge(impressions[0], impressions[j])  # Add edges to the graph

    return G


def simulate_random_walk(graph, iterations=1000000):
    """Simulate a random walk on the graph and calculate node rankings."""
    nodes = {node: 0 for node in graph.nodes}  # Initialize node rankings

    current_node = random.choice(list(graph.nodes))  # Start from a random node
    for _ in range(iterations): 
        nodes[current_node] += 1  # Increment visit count for the current node
        successors = list(graph.successors(current_node))
        if successors:  # If there are successors
            random_successor = random.choice(successors)
            # Move to a random successor if it exists, otherwise choose a random node in the graph
            current_node = random_successor if random_successor in graph.nodes else random.choice(list(graph.nodes))
        else:
            current_node = random.choice(list(graph.nodes))

    # Sort nodes based on visit counts in descending order
    sorted_nodes = dict(sorted(nodes.items(), key=lambda item: item[1], reverse=True))
    return sorted_nodes


file_path = "C:\\Users\\NACHIKET\\Downloads\\Project 2_Impression Network.csv"
G = create_graph(file_path)  # Create the graph from the CSV file

def myopic_search(graph, start_node, target_node):
    """Perform myopic search from start_node to target_node in the graph."""
    current_node = start_node
    if nx.has_path(G, start_node, target_node):  # Check if a path exists between start_node and target_node
        path = [current_node]  # Initialize the path with the start_node
        while current_node != target_node:
            neighbors = list(graph.successors(current_node))  # Get neighbors of the current node
            if not neighbors:  # If there are no neighbors, return 0 (no path)
                return 0
            elif target_node in neighbors:  # If target_node is a neighbor, return path length + 1
                return len(path) + 1
            else:
                # Move to a random neighbor and update the path
                for i in range (len(neighbors)): 
                    next_node = random.choice(neighbors)
                    if nx.has_path(G, next_node, target_node):
                        path.append(next_node)
                        current_node = next_node
                        break
        return len(path) + 1
    else:
        return 0  # Return 0 if no path exists

# Implement optimal search
def optimal_search(graph, start_node, target_node):
    """Perform optimal search (Dijkstra's algorithm) from start_node to target_node."""
    if nx.has_path(G, start_node, target_node):  # Check if a path exists between start_node and target_node
        # Calculate the shortest path using Dijkstra's algorithm
        shortest_path_length, shortest_path = nx.single_source_dijkstra(graph, start_node, target_node)
        return len(shortest_path)  # Return the length of the shortest path
    else:
        return 0  # Return 0 if no path exists

nodes = list(G.nodes())  # Get a list of nodes in the graph
pairs = [(random.choice(nodes), random.choice(nodes)) for _ in range(100)]  # Generate 100 random pairs of nodes

# Perform searches for each pair and store the path lengths
myopic_lengths = []
optimal_lengths = []
for start_node, target_node in pairs:
    if start_node not in G or target_node not in G:
        continue  # Skip if nodes not in graph
    else:
        myopic_lengths.append(myopic_search(G,start_node,target_node))
        optimal_lengths.append(optimal_search(G,start_node,target_node))
print(myopic_lengths)
print(optimal_lengths)        

# Plot the comparison in a line graph
plt.figure(figsize=(10, 6))
x_values = range(1, len(pairs) + 1)
plt.plot(x_values, myopic_lengths, color='blue', label='Myopic Search')
plt.plot(x_values, optimal_lengths, color='red', label='Optimal Search (Dijkstra)')
plt.xlabel('Pairs of Nodes')
plt.ylabel('Path Length')
plt.title('Comparison of Myopic Search and Optimal Search for Various Node Pairs')
#plt.xticks(x_values, [f'{pair[0]}-{pair[1]}' for pair in pairs], rotation=45)
plt.legend()
plt.show()