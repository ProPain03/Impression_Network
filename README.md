# Graph-Based Social Network Analysis and Link Prediction

A comprehensive Python framework for analyzing social networks using graph theory, implementing PageRank-style algorithms, link prediction models, and search algorithm comparisons. This project demonstrates advanced graph analytics techniques on real-world social network data.

## 🌟 Project Overview

This project implements a complete graph analytics pipeline that:
- **Identifies Key Influencers** using random walk algorithms with teleportation
- **Predicts Missing Links** using least squares regression on adjacency matrices
- **Compares Search Algorithms** (Myopic vs Optimal) for pathfinding efficiency
- **Visualizes Results** through comprehensive data plots and rankings

## 🚀 Key Features

### 1. **PageRank with Random Walk & Teleportation**
- Implements custom PageRank algorithm with 85% transition probability and 15% teleportation
- Simulates user navigation patterns through 1M iterations
- Identifies top influencers in the social network

### 2. **Link Prediction System** 
- Uses least squares regression to predict missing connections
- Analyzes adjacency matrix patterns to identify potential relationships
- Enhances network connectivity through intelligent link suggestions

### 3. **Search Algorithm Comparison**
- **Myopic Search**: Local greedy approach for pathfinding
- **Optimal Search**: Dijkstra's algorithm for shortest paths
- Performance analysis across 100 random node pairs with visualization

### 4. **Real-World Data Processing**
- Processes CSV-based social network datasets
- Handles email-based node identification
- Manages incomplete data and NaN values gracefully

## 📁 Project Structure

```
Impression_Network/
├── Project-2, Q1 (2023CSB1106).py    # Basic PageRank implementation
├── Project-2, Q2 (2023CSB1106).py    # PageRank with teleportation + Link prediction
├── Project-2, Q3 (2023CSB1106).py    # Search algorithm comparison
├── Project 2_Impression Network.csv   # Social network dataset
├── CS101-Project 2 Q*.pdf            # Problem statements and requirements
└── README.md
```

## 🛠 Technologies Used

- **Python 3.x**: Core programming language
- **NetworkX**: Graph creation, manipulation, and algorithms
- **Pandas**: Data processing and CSV handling
- **NumPy**: Matrix operations and linear algebra
- **Matplotlib**: Data visualization and plotting
- **Random**: Stochastic simulation and sampling

## 📊 Algorithms Implemented

### Random Walk with Teleportation
```python
# 85% probability: follow edge to neighbor
# 15% probability: jump to random node
if random.random() >= 0.15:
    current_node = random.choice(successors)
else:
    current_node = random.choice(all_nodes)
```

### Link Prediction via Least Squares
```python
# For missing edge (i,j), solve: X·A = b
# Where A is reduced adjacency matrix, b is test row
X = np.linalg.lstsq(A.T, b.T)[0].T
predicted_value = X @ test_column
if abs(predicted_value) >= 0.8:
    add_link(i, j)
```

## 🔧 Installation & Setup

### Prerequisites
```bash
pip install pandas networkx matplotlib numpy
```

### Running the Analysis

**1. Basic PageRank Analysis:**
```bash
python "Project-2, Q1 (2023CSB1106).py"
```
- Outputs top 10 most influential nodes
- Uses simple random walk without teleportation

**2. Advanced PageRank + Link Prediction:**
```bash
python "Project-2, Q2 (2023CSB1106).py"
```
- Implements teleportation-based PageRank
- Predicts and adds missing links
- Compares original vs modified network rankings

**3. Search Algorithm Comparison:**
```bash
python "Project-2, Q3 (2023CSB1106).py"
```
- Compares Myopic vs Dijkstra search
- Generates performance visualization plots
- Analyzes 100 random node pairs

## 📈 Results & Analysis

### PageRank Results
- **Top Leader Identification**: Ranks all nodes by influence score
- **Network Centrality**: Quantifies node importance in the graph
- **Teleportation Impact**: Shows how random jumps affect rankings

### Link Prediction Results
- **Missing Links Found**: Identifies potential connections using regression
- **Network Enhancement**: Increases connectivity through predicted edges
- **Threshold Analysis**: Uses 0.8 threshold for link acceptance

### Search Comparison Results
- **Path Length Analysis**: Compares efficiency of different search strategies
- **Algorithm Performance**: Visualizes Myopic vs Optimal search results
- **Statistical Insights**: Quantifies search algorithm effectiveness

## 🎯 Key Insights

1. **Influencer Identification**: PageRank with teleportation provides more robust centrality measures
2. **Network Completion**: Least squares regression effectively predicts missing social connections
3. **Search Efficiency**: Optimal (Dijkstra) consistently outperforms Myopic search in path length
4. **Real-World Applicability**: Framework scales to large social networks with email-based identifiers

## 📊 Sample Output

```
TOP LEADER : 2023CSB1140
Other top 10 are :
2 : 2023CSB1121
3 : 2023CSB1162
4 : 2023CSB1123
...

Number of links added : 42
Number of links unchanged : 20564
Added links are :
('2023CSB1095', '2023CSB1118')
('2023CSB1100', '2023CSB1143')
...
```

## 🔬 Research Applications

- **Social Media Analysis**: Identify key influencers and predict user connections
- **Recommendation Systems**: Suggest new connections based on network patterns
- **Network Optimization**: Enhance connectivity in sparse social graphs
- **Algorithm Benchmarking**: Compare search and ranking algorithm performance


## 📄 References

- **NetworkX Documentation**: Graph algorithms and implementations
- **PageRank Algorithm**: Google's original web ranking methodology  
- **Dijkstra's Algorithm**: Shortest path optimization
- **Social Network Analysis**: Graph theory applications in sociology

## 📋 Data Format

The CSV dataset follows this structure:
```csv
Email Address,Your Impression 1,Your Impression 2,...,Your Impression 30
2023CSB1162,2023CSB1137,2023MCB1291,2023CSB1123,...
```

Each row represents a node and their connections (impressions) in the social network.

---
