import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random

def create_graph_from_csv(file_path):
    """Create a directed graph from a CSV file."""
    G = nx.DiGraph()  # Create an empty directed graph
    df = pd.read_csv(file_path)  # Read CSV file into a pandas dataframe
    names = df['Email Address'].tolist()  # Extract values from 'Email Address' column
    G.add_nodes_from(names)  # Add nodes to the graph

    for i in range(len(df)):
        impressions = list(df.iloc[i])
        for j in range(1, len(impressions)):
            if impressions[j] is not None:
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
            current_node = random_successor if random_successor in graph.nodes else random.choice(list(graph.nodes))
        else:
            current_node = random.choice(list(graph.nodes))

    sorted_nodes = dict(sorted(nodes.items(), key=lambda item: item[1], reverse=True))
    return sorted_nodes

#Calling the functions
def main():
    file_path = "C:\\Users\\NACHIKET\\Downloads\\Project 2_Impression Network.csv"
    graph = create_graph_from_csv(file_path)
    node_rankings = simulate_random_walk(graph)
    l=[]  #saving the nodes according to their rankings and coins distributed in the list
    for node in node_rankings.items():
        l.append(node)
    l.pop(0) #Removing 'nan' which was considered
    print('TOP LEADER :',l[0][0])
    print('Other top 10 are :')
    for i in range(1,10):
        print(i+1,':',l[i][0])

main()