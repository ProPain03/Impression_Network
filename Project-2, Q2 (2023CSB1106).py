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
    '''For adding teleportation with probability 15%, create random variable x varying from 0 to 1
    If x<0.15, jump to any random node else choose from one of the neighbours'''

    for _ in range(iterations):
        x=random.random()  
        nodes[current_node] += 1  # Increment visit count for the current node
        if x>=0.15:
            successors = list(graph.successors(current_node))
            if successors:  # If there are successors
                random_successor = random.choice(successors)
                current_node = random_successor if random_successor in graph.nodes else random.choice(list(graph.nodes))
            else:
                current_node = random.choice(list(graph.nodes))
        else:
            current_node = random.choice(list(graph.nodes))


    sorted_nodes = dict(sorted(nodes.items(), key=lambda item: item[1], reverse=True))
    return sorted_nodes


def main():
    file_path = "C:\\Users\\NACHIKET\\Downloads\\Project 2_Impression Network.csv"
    G = create_graph(file_path)  # Create the graph from the CSV file
    node_rankings = simulate_random_walk(G)  # Perform random walk and calculate node rankings
    l = []
    for node in node_rankings.items():
        l.append(node)
    l.pop(0)  #'nan' in the graph gets highest coins however wee don't consider this
    print('Original Page Rank : ')
    for i in range(1, 101):
        print(i, ':', l[i - 1][0])  # Print node rankings
    nodes_to_remove = [node for node in G.nodes() if pd.isna(node)]
    G.remove_nodes_from(nodes_to_remove)
    #print(len(list(G.nodes())))    
    nodes = list(G.nodes())
    adj_matrix = nx.to_numpy_array(G)  # Convert the graph to an adjacency matrix
    yes = 0  # Counter for added links
    no = 0  # Counter for unchanged links   
    links=[] #list to store missing links


    '''We will check missing links if aij is 0'''
    for num1 in range (143):  #144 is the number of nodes
        for num2 in range (143):
            if num1==num2:
                no+=1
            elif adj_matrix[num1][num2]==0:  
                a=np.delete(adj_matrix, num2, axis=1)  #Delete the column of the test cell and store the remaining test row in b
                #print(a.shape)
                b=a[num1]
                A=np.delete(a, num1, axis=0)   #Delete the test row too and store remaining adj matrix of dimensions (n-1)*(n-1) in A
                '''We have to solve XA=b'''
                Xt, residuals, rank, s = np.linalg.lstsq(A.T, b.T, rcond=None)  #Xt is the transpose of our row of coefficients
                X=Xt.T #Find X from Xt 
                #print(X.shape)
                a1=adj_matrix[ : ,num2]   
                a1=np.delete(a1, num1, axis=0)
                #print(a1)
                #print(a1.shape)
                s=np.matmul(X,a1)  #Multiplying X with the test column
                #print(s)
                if abs(s)>=0.8:   #If the absolute of the value we get is greater than 0.8 then we change 0 to 1 
                    adj_matrix[num1][num2]+=1
                    yes+=1
                    links.append((nodes[num1],nodes[num2]))  #Store the missing link found
                else:
                    no+=1
                #flag+=1
    
    Gg=nx.from_numpy_array(adj_matrix, create_using=nx.DiGraph)
    
    node_rankings = simulate_random_walk(Gg)
    l=[]
    for node in node_rankings.items():
        l.append(node)
    l.pop(0)
    #for i in range(1,len(l)+1):
    print('Page Rank of Modified graph')
    for i in range (1,101):
        print(i,':',nodes[l[i-1][0]])


    print('Number of links added : ',yes)
    print('Number of links unchanged : ',no)
    print('Added links are :')
    for i in links:
        print(i)







    

    


main()
    
