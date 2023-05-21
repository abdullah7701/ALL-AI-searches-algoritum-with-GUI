# import tkinter as tk
# from tkinter import messagebox
# # from queue import Queue
# from queue import Queue, PriorityQueue
# from collections import deque
#
#
# class Graph:
#     def __init__(self, vertices):
#         self.vertices = vertices
#         self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]
#
#     def add_edge(self, src, dest, weight=1):
#         self.adjacency_matrix[src][dest] = weight
#         self.adjacency_matrix[dest][src] = weight
#
#     def get_neighbors(self, vertex):
#         neighbors = []
#         for i in range(self.vertices):
#             if self.adjacency_matrix[vertex][i] != 0:
#                 neighbors.append(i)
#         return neighbors
#
#
# class SearchGUI:
#     def __init__(self, root):
#         self.root = root
#         self.graph = None
#         self.start_node = None
#         self.goal_node = None
#
#         self.canvas = tk.Canvas(root, width=400, height=400)
#         self.canvas.pack()
#
#         self.frame = tk.Frame(root)
#         self.frame.pack()
#
#         self.algorithm_label = tk.Label(self.frame, text="Select Algorithm:")
#         self.algorithm_label.grid(row=0, column=0)
#
#         self.algorithm_var = tk.StringVar()
#         self.algorithm_var.set("BFS")  # Default algorithm
#         self.algorithm_dropdown = tk.OptionMenu(self.frame, self.algorithm_var, "BFS", "DFS", "DLS", "IDS", "UCS", "Bidirectional", "BestFS", "A*")
#         self.algorithm_dropdown.grid(row=0, column=1)
#
#         self.start_label = tk.Label(self.frame, text="Start Node:")
#         self.start_label.grid(row=1, column=0)
#
#         self.start_entry = tk.Entry(self.frame)
#         self.start_entry.grid(row=1, column=1)
#
#         self.goal_label = tk.Label(self.frame, text="Goal Node:")
#         self.goal_label.grid(row=2, column=0)
#
#         self.goal_entry = tk.Entry(self.frame)
#         self.goal_entry.grid(row=2, column=1)
#
#         self.create_graph_button = tk.Button(self.frame, text="Create Graph", command=self.create_graph)
#         self.create_graph_button.grid(row=3, columnspan=2)
#
#         self.search_button = tk.Button(self.frame, text="Search", command=self.search)
#         self.search_button.grid(row=4, columnspan=2)
#
#     def create_graph(self):
#         vertices = 6  # Number of vertices in the graph
#         self.graph = Graph(vertices)
#         self.graph.add_edge(0, 1)
#         self.graph.add_edge(0, 2)
#         self.graph.add_edge(1, 3)
#         self.graph.add_edge(1, 4)
#         self.graph.add_edge(2, 5)
#
#         messagebox.showinfo("Graph Created", "Graph has been created.")
#
#     def search(self):
#         start_node = int(self.start_entry.get())
#         goal_node = int(self.goal_entry.get())
#         algorithm = self.algorithm_var.get()
#
#         if algorithm == "BFS":
#             path = self.bfs(start_node, goal_node)
#         elif algorithm == "DFS":
#             path = self.dfs(start_node, goal_node)
#         elif algorithm == "DLS":
#             depth_limit = 3  # Set the desired depth limit
#             path = self.dls(start_node, goal_node, depth_limit)
#         elif algorithm == "IDS":
#             path = self.ids(start_node, goal_node)
#         elif algorithm == "UCS":
#             path = self.ucs(start_node, goal_node)
#         elif algorithm == "Bidirectional":
#             path = self.bidirectional_search(start_node, goal_node)
#         elif algorithm == "BestFS":
#             path = self.best_first_search(start_node, goal_node)
#         elif algorithm == "A*":
#             path = self.a_star_search(start_node, goal_node)
#         else:
#             messagebox.showerror("Error", "Invalid algorithm selected.")
#             return
#
#         if path:
#             messagebox.showinfo("Path Found", "Path: {}".format(path))
#         else:
#             messagebox.showinfo("No Path Found", "No path found.")
#
#     def bfs(self, start, goal):
#         visited = [False] * self.graph.vertices
#         queue = Queue()
#         queue.put(start)
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while not queue.empty():
#             vertex = queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 if not visited[neighbor]:
#                     queue.put(neighbor)
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#
#         return []
#
#     def dfs(self, start, goal):
#         visited = [False] * self.graph.vertices
#         stack = [start]
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while stack:
#             vertex = stack.pop()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 if not visited[neighbor]:
#                     stack.append(neighbor)
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#
#         return []
#
#     def dls(self, start, goal, depth_limit):
#         visited = [False] * self.graph.vertices
#         stack = [(start, 0)]
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while stack:
#             vertex, depth = stack.pop()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             if depth < depth_limit:
#                 neighbors = self.graph.get_neighbors(vertex)
#                 for neighbor in neighbors:
#                     if not visited[neighbor]:
#                         stack.append((neighbor, depth + 1))
#                         visited[neighbor] = True
#                         parent[neighbor] = vertex
#
#         return []
#
#     def ids(self, start, goal):
#         depth_limit = 0
#         while True:
#             path = self.dls(start, goal, depth_limit)
#             if path:
#                 return path
#             depth_limit += 1
#
#     def ucs(self, start, goal):
#         visited = [False] * self.graph.vertices
#         priority_queue = PriorityQueue()
#         priority_queue.put((0, start))
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#         cost = [float('inf')] * self.graph.vertices
#         cost[start] = 0
#
#         while not priority_queue.empty():
#             _, vertex = priority_queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 edge_cost = self.graph.adjacency_matrix[vertex][neighbor]
#                 new_cost = cost[vertex] + edge_cost
#                 if not visited[neighbor] or new_cost < cost[neighbor]:
#                     priority_queue.put((new_cost, neighbor))
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#                     cost[neighbor] = new_cost
#
#         return []
#
#     def bidirectional_search(self, start, goal):
#         forward_visited = [False] * self.graph.vertices
#         backward_visited = [False] * self.graph.vertices
#         forward_queue = Queue()
#         backward_queue = Queue()
#         forward_queue.put(start)
#         backward_queue.put(goal)
#         forward_visited[start] = True
#         backward_visited[goal] = True
#         forward_parent = [-1] * self.graph.vertices
#         backward_parent = [-1] * self.graph.vertices
#
#         intersect_node = -1
#         while not forward_queue.empty() and not backward_queue.empty():
#             forward_vertex = forward_queue.get()
#             backward_vertex = backward_queue.get()
#
#             if forward_visited[backward_vertex]:
#                 intersect_node = backward_vertex
#                 break
#             elif backward_visited[forward_vertex]:
#                 intersect_node = forward_vertex
#                 break
#
#             forward_neighbors = self.graph.get_neighbors(forward_vertex)
#             for neighbor in forward_neighbors:
#                 if not forward_visited[neighbor]:
#                     forward_queue.put(neighbor)
#                     forward_visited[neighbor] = True
#                     forward_parent[neighbor] = forward_vertex
#
#             backward_neighbors = self.graph.get_neighbors(backward_vertex)
#             for neighbor in backward_neighbors:
#                 if not backward_visited[neighbor]:
#                     backward_queue.put(neighbor)
#                     backward_visited[neighbor] = True
#                     backward_parent[neighbor] = backward_vertex
#
#         if intersect_node == -1:
#             return []
#
#         path = []
#         node = intersect_node
#         while node != -1:
#             path.append(node)
#             node = forward_parent[node]
#
#         path = path[::-1]  # Reverse the path
#
#         node = backward_parent[intersect_node]
#         while node != -1:
#             path.append(node)
#             node = backward_parent[node]
#
#         return path
#
#     def best_first_search(self, start, goal):
#         visited = [False] * self.graph.vertices
#         priority_queue = PriorityQueue()
#         priority_queue.put((0, start))
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while not priority_queue.empty():
#             _, vertex = priority_queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 if not visited[neighbor]:
#                     priority_queue.put((self.heuristic(neighbor, goal), neighbor))
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#
#         return []
#
#     def a_star_search(self, start, goal):
#         visited = [False] * self.graph.vertices
#         priority_queue = PriorityQueue()
#         priority_queue.put((0, start))
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#         cost = [float('inf')] * self.graph.vertices
#         cost[start] = 0
#
#         while not priority_queue.empty():
#             _, vertex = priority_queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 edge_cost = self.graph.adjacency_matrix[vertex][neighbor]
#                 new_cost = cost[vertex] + edge_cost
#                 if not visited[neighbor] or new_cost < cost[neighbor]:
#                     priority_queue.put((new_cost + self.heuristic(neighbor, goal), neighbor))
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#                     cost[neighbor] = new_cost
#
#         return []
#
#     def heuristic(self, current, goal):
#         # Calculate and return the heuristic value
#         return abs(current - goal)
#
#     def construct_path(self, parent, goal):
#         path = []
#         node = goal
#         while node != -1:
#             path.append(node)
#             node = parent[node]
#         path.reverse()
#         return path
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = SearchGUI(root)
#     root.mainloop()






# import tkinter as tk
# from tkinter import messagebox
# from queue import Queue
# from queue import Queue, PriorityQueue
# import matplotlib.pyplot as plt
# import networkx as nx
# from collections import deque
#
# class Graph:
#     def __init__(self, vertices):
#         self.vertices = vertices
#         self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]
#
#     def add_edge(self, src, dest, weight=1):
#         self.adjacency_matrix[src][dest] = weight
#         self.adjacency_matrix[dest][src] = weight
#
#     def get_neighbors(self, vertex):
#         neighbors = []
#         for i in range(self.vertices):
#             if self.adjacency_matrix[vertex][i] != 0:
#                 neighbors.append(i)
#         return neighbors
#
# class SearchGUI:
#     def __init__(self, root):
#         self.root = root
#         self.graph = None
#         self.start_node = None
#         self.goal_node = None
#
#         self.root.title("Graph Search")
#         self.root.geometry("1130x780")
#
#         self.canvas = tk.Canvas(root, width=400, height=400)
#         self.canvas.pack()
#
#         self.frame = tk.Frame(root)
#         self.frame.pack(pady=10)
#
#         self.algorithm_label = tk.Label(self.frame, text="Select Algorithm:")
#         self.algorithm_label.grid(row=0, column=0)
#
#         self.algorithm_var = tk.StringVar()
#         self.algorithm_var.set("BFS")  # Default algorithm
#         self.algorithm_dropdown = tk.OptionMenu(self.frame, self.algorithm_var, "BFS", "DFS", "DLS", "IDS", "UCS", "Bidirectional", "BestFS", "A*")
#         self.algorithm_dropdown.grid(row=0, column=1)
#
#         self.start_label = tk.Label(self.frame, text="Start Node:")
#         self.start_label.grid(row=1, column=0)
#
#         self.start_entry = tk.Entry(self.frame)
#         self.start_entry.grid(row=1, column=1)
#
#         self.goal_label = tk.Label(self.frame, text="Goal Node:")
#         self.goal_label.grid(row=2, column=0)
#
#         self.goal_entry = tk.Entry(self.frame)
#         self.goal_entry.grid(row=2, column=1)
#
#         self.create_graph_button = tk.Button(self.frame, text="Create Graph", command=self.create_graph, bg="#4CAF50", fg="white")
#         self.create_graph_button.grid(row=3, columnspan=2, pady=10)
#
#         self.search_button = tk.Button(self.frame, text="Search", command=self.search, bg="#008CBA", fg="white")
#         self.search_button.grid(row=4, columnspan=2)
#
#     def create_graph(self):
#         vertices = 6  # Number of vertices in the graph
#         self.graph = Graph(vertices)
#         self.graph.add_edge(0, 1)
#         self.graph.add_edge(0, 2)
#         self.graph.add_edge(1, 3)
#         self.graph.add_edge(1, 4)
#         self.graph.add_edge(2, 5)
#
#         # Create a NetworkX graph object
#         G = nx.Graph()
#         for src in range(vertices):
#             for dest in self.graph.get_neighbors(src):
#                 G.add_edge(src, dest)
#
#         # Plot the graph as a tree
#         pos = nx.spring_layout(G)
#         nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
#
#         plt.title("Graph")
#         plt.show()
#
#         messagebox.showinfo("Graph Created", "Graph has been created.")
#
#     def search(self):
#         start_node = int(self.start_entry.get())
#         goal_node = int(self.goal_entry.get())
#         algorithm = self.algorithm_var.get()
#
#         if algorithm == "BFS":
#             path = self.bfs(start_node, goal_node)
#         elif algorithm == "DFS":
#             path = self.dfs(start_node, goal_node)
#         elif algorithm == "DLS":
#             depth_limit = 3  # Set the desired depth limit
#             path= self.dls(start_node, goal_node, depth_limit)
#         elif algorithm == "IDS":
#             path = self.ids(start_node, goal_node)
#         elif algorithm == "UCS":
#             path = self.ucs(start_node, goal_node)
#         elif algorithm == "Bidirectional":
#             path = self.bidirectional_search(start_node, goal_node)
#         elif algorithm == "BestFS":
#             path = self.best_first_search(start_node, goal_node)
#         elif algorithm == "A*":
#             path = self.a_star_search(start_node, goal_node)
#         else:
#             messagebox.showerror("Error", "Invalid algorithm selected.")
#             return
#
#         if path:
#             messagebox.showinfo("Path Found", "Path: {}".format(path))
#         else:
#             messagebox.showinfo("No Path Found", "No path found.")
#
#     def bfs(self, start, goal):
#         visited = [False] * self.graph.vertices
#         queue = Queue()
#         queue.put(start)
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while not queue.empty():
#             vertex = queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 if not visited[neighbor]:
#                     queue.put(neighbor)
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#
#         return []
#
#     def dfs(self, start, goal):
#         visited = [False] * self.graph.vertices
#         stack = [start]
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while stack:
#             vertex = stack.pop()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 if not visited[neighbor]:
#                     stack.append(neighbor)
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#
#         return []
#
#     def dls(self, start, goal, depth_limit):
#         visited = [False] * self.graph.vertices
#         stack = [(start, 0)]
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while stack:
#             vertex, depth = stack.pop()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             if depth < depth_limit:
#                 neighbors = self.graph.get_neighbors(vertex)
#                 for neighbor in neighbors:
#                     if not visited[neighbor]:
#                         stack.append((neighbor, depth + 1))
#                         visited[neighbor] = True
#                         parent[neighbor] = vertex
#
#         return []
#
#     def ids(self, start, goal):
#         depth_limit = 0
#         while True:
#             path = self.dls(start, goal, depth_limit)
#             if path:
#                 return path
#             depth_limit += 1
#
#     def ucs(self, start, goal):
#         visited = [False] * self.graph.vertices
#         priority_queue = PriorityQueue()
#         priority_queue.put((0, start))
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#         cost = [float('inf')] * self.graph.vertices
#         cost[start] = 0
#
#         while not priority_queue.empty():
#             _, vertex = priority_queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 edge_cost = self.graph.adjacency_matrix[vertex][neighbor]
#                 new_cost = cost[vertex] + edge_cost
#                 if not visited[neighbor] or new_cost < cost[neighbor]:
#                     priority_queue.put((new_cost, neighbor))
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#                     cost[neighbor] = new_cost
#
#         return []
#
#     def bidirectional_search(self, start, goal):
#         forward_visited = [False] * self.graph.vertices
#         backward_visited = [False] * self.graph.vertices
#         forward_queue = Queue()
#         backward_queue = Queue()
#         forward_queue.put(start)
#         backward_queue.put(goal)
#         forward_visited[start] = True
#         backward_visited[goal] = True
#         forward_parent = [-1] * self.graph.vertices
#         backward_parent = [-1] * self.graph.vertices
#
#         intersect_node = -1
#         while not forward_queue.empty() and not backward_queue.empty():
#             forward_vertex = forward_queue.get()
#             backward_vertex = backward_queue.get()
#
#             if forward_visited[backward_vertex]:
#                 intersect_node = backward_vertex
#                 break
#             elif backward_visited[forward_vertex]:
#                 intersect_node = forward_vertex
#                 break
#
#             forward_neighbors = self.graph.get_neighbors(forward_vertex)
#             for neighbor in forward_neighbors:
#                 if not forward_visited[neighbor]:
#                     forward_queue.put(neighbor)
#                     forward_visited[neighbor] = True
#                     forward_parent[neighbor] = forward_vertex
#
#             backward_neighbors = self.graph.get_neighbors(backward_vertex)
#             for neighbor in backward_neighbors:
#                 if not backward_visited[neighbor]:
#                     backward_queue.put(neighbor)
#                     backward_visited[neighbor] = True
#                     backward_parent[neighbor] = backward_vertex
#
#         if intersect_node == -1:
#             return []
#
#         path = []
#         node = intersect_node
#         while node != -1:
#             path.append(node)
#             node = forward_parent[node]
#
#         path = path[::-1]  # Reverse the path
#
#         node = backward_parent[intersect_node]
#         while node != -1:
#             path.append(node)
#             node = backward_parent[node]
#
#         return path
#
#     def best_first_search(self, start, goal):
#         visited = [False] * self.graph.vertices
#         priority_queue = PriorityQueue()
#         priority_queue.put((0, start))
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while not priority_queue.empty():
#             _, vertex = priority_queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 if not visited[neighbor]:
#                     priority_queue.put((self.heuristic(neighbor, goal), neighbor))
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#
#         return []
#
#     def a_star_search(self, start, goal):
#         visited = [False] * self.graph.vertices
#         priority_queue = PriorityQueue()
#         priority_queue.put((0, start))
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#         cost = [float('inf')] * self.graph.vertices
#         cost[start] = 0
#
#         while not priority_queue.empty():
#             _, vertex = priority_queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 edge_cost = self.graph.adjacency_matrix[vertex][neighbor]
#                 new_cost = cost[vertex] + edge_cost
#                 if not visited[neighbor] or new_cost < cost[neighbor]:
#                     priority_queue.put((new_cost + self.heuristic(neighbor, goal), neighbor))
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#                     cost[neighbor] = new_cost
#
#         return []
#
#     def heuristic(self, current, goal):
#         # Calculate and return the heuristic value
#         return abs(current - goal)
#
#     def construct_path(self, parent, goal):
#         path= []
#         node = goal
#         while node != -1:
#             path.append(node)
#             node = parent[node]
#         path.reverse()
#         return path
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.configure(bg="#F0F0F0")
#     gui = SearchGUI(root)
#     root.mainloop()
#
#
#     def bfs(self, start, goal):
#         visited = [False] * self.graph.vertices
#         queue = Queue()
#         queue.put(start)
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while not queue.empty():
#             vertex = queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 if not visited[neighbor]:
#                     queue.put(neighbor)
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#
#         return []
#
#     def dfs(self, start, goal):
#         visited = [False] * self.graph.vertices
#         stack = [start]
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while stack:
#             vertex = stack.pop()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 if not visited[neighbor]:
#                     stack.append(neighbor)
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#
#         return []
#
#     def dls(self, start, goal, depth_limit):
#         visited = [False] * self.graph.vertices
#         stack = [(start, 0)]
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while stack:
#             vertex, depth = stack.pop()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             if depth < depth_limit:
#                 neighbors = self.graph.get_neighbors(vertex)
#                 for neighbor in neighbors:
#                     if not visited[neighbor]:
#                         stack.append((neighbor, depth + 1))
#                         visited[neighbor] = True
#                         parent[neighbor] = vertex
#
#         return []
#
#     def ids(self, start, goal):
#         depth_limit = 0
#         while True:
#             path = self.dls(start, goal, depth_limit)
#             if path:
#                 return path
#             depth_limit += 1
#
#     def ucs(self, start, goal):
#         visited = [False] * self.graph.vertices
#         priority_queue = PriorityQueue()
#         priority_queue.put((0, start))
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#         cost = [float('inf')] * self.graph.vertices
#         cost[start] = 0
#
#         while not priority_queue.empty():
#             _, vertex = priority_queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 edge_cost = self.graph.adjacency_matrix[vertex][neighbor]
#                 new_cost = cost[vertex] + edge_cost
#                 if not visited[neighbor] or new_cost < cost[neighbor]:
#                     priority_queue.put((new_cost, neighbor))
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#                     cost[neighbor] = new_cost
#
#         return []
#
#     def bidirectional_search(self, start, goal):
#         forward_visited = [False] * self.graph.vertices
#         backward_visited = [False] * self.graph.vertices
#         forward_queue = Queue()
#         backward_queue = Queue()
#         forward_queue.put(start)
#         backward_queue.put(goal)
#         forward_visited[start] = True
#         backward_visited[goal] = True
#         forward_parent = [-1] * self.graph.vertices
#         backward_parent = [-1] * self.graph.vertices
#
#         intersect_node = -1
#         while not forward_queue.empty() and not backward_queue.empty():
#             forward_vertex = forward_queue.get()
#             backward_vertex = backward_queue.get()
#
#             if forward_visited[backward_vertex]:
#                 intersect_node = backward_vertex
#                 break
#             elif backward_visited[forward_vertex]:
#                 intersect_node = forward_vertex
#                 break
#
#             forward_neighbors = self.graph.get_neighbors(forward_vertex)
#             for neighbor in forward_neighbors:
#                 if not forward_visited[neighbor]:
#                     forward_queue.put(neighbor)
#                     forward_visited[neighbor] = True
#                     forward_parent[neighbor] = forward_vertex
#
#             backward_neighbors = self.graph.get_neighbors(backward_vertex)
#             for neighbor in backward_neighbors:
#                 if not backward_visited[neighbor]:
#                     backward_queue.put(neighbor)
#                     backward_visited[neighbor] = True
#                     backward_parent[neighbor] = backward_vertex
#
#         if intersect_node == -1:
#             return []
#
#         path = []
#         node = intersect_node
#         while node != -1:
#             path.append(node)
#             node = forward_parent[node]
#
#         path = path[::-1]  # Reverse the path
#
#         node = backward_parent[intersect_node]
#         while node != -1:
#             path.append(node)
#             node = backward_parent[node]
#
#         return path
#
#     def best_first_search(self, start, goal):
#         visited = [False] * self.graph.vertices
#         priority_queue = PriorityQueue()
#         priority_queue.put((0, start))
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#
#         while not priority_queue.empty():
#             _, vertex = priority_queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 if not visited[neighbor]:
#                     priority_queue.put((self.heuristic(neighbor, goal), neighbor))
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#
#         return []
#
#     def a_star_search(self, start, goal):
#         visited = [False] * self.graph.vertices
#         priority_queue = PriorityQueue()
#         priority_queue.put((0, start))
#         visited[start] = True
#         parent = [-1] * self.graph.vertices
#         cost = [float('inf')] * self.graph.vertices
#         cost[start] = 0
#
#         while not priority_queue.empty():
#             _, vertex = priority_queue.get()
#             if vertex == goal:
#                 return self.construct_path(parent, goal)
#             neighbors = self.graph.get_neighbors(vertex)
#             for neighbor in neighbors:
#                 edge_cost = self.graph.adjacency_matrix[vertex][neighbor]
#                 new_cost = cost[vertex] + edge_cost
#                 if not visited[neighbor] or new_cost < cost[neighbor]:
#                     priority_queue.put((new_cost + self.heuristic(neighbor, goal), neighbor))
#                     visited[neighbor] = True
#                     parent[neighbor] = vertex
#                     cost[neighbor] = new_cost
#
#         return []
#
#     def heuristic(self, current, goal):
#         # Calculate and return the heuristic value
#         return abs(current - goal)
#
#     def construct_path(self, parent, goal):
#         path = []
#         node = goal
#         while node != -1:
#             path.append(node)
#             node = parent[node]
#         path.reverse()
#         return path
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = SearchGUI(root)
#     root.mainloop()


import tkinter as tk
from tkinter import messagebox
from queue import Queue
from queue import Queue, PriorityQueue
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, src, dest, weight=1):
        self.adjacency_matrix[src][dest] = weight
        self.adjacency_matrix[dest][src] = weight

    def get_neighbors(self, vertex):
        neighbors = []
        for i in range(self.vertices):
            if self.adjacency_matrix[vertex][i] != 0:
                neighbors.append(i)
        return neighbors

class SearchGUI:
    def __init__(self, root):
        self.root = root
        self.graph = None
        self.start_node = None
        self.goal_node = None

        self.root.title("Graph Search")
        self.root.geometry("1130x780")

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.algorithm_label = tk.Label(self.frame, text="Select Algorithm:")
        self.algorithm_label.grid(row=0, column=0)

        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("BFS")  # Default algorithm
        self.algorithm_dropdown = tk.OptionMenu(self.frame, self.algorithm_var, "BFS", "DFS", "DLS", "IDS", "UCS", "Bidirectional", "BestFS", "A*")
        self.algorithm_dropdown.grid(row=0, column=1)

        self.start_label = tk.Label(self.frame, text="Start Node:")
        self.start_label.grid(row=1, column=0)

        self.start_entry = tk.Entry(self.frame)
        self.start_entry.grid(row=1, column=1)

        self.goal_label = tk.Label(self.frame, text="Goal Node:")
        self.goal_label.grid(row=2, column=0)

        self.goal_entry = tk.Entry(self.frame)
        self.goal_entry.grid(row=2, column=1)

        self.create_graph_button = tk.Button(self.frame, text="Create Graph", command=self.create_graph, bg="#4CAF50", fg="white")
        self.create_graph_button.grid(row=3, columnspan=2, pady=10)

        self.search_button = tk.Button(self.frame, text="Search", command=self.search, bg="#008CBA", fg="white")
        self.search_button.grid(row=4, columnspan=2)

    def create_graph(self):
        vertices = 6  # Number of vertices in the graph
        self.graph = Graph(vertices)
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(1, 4)
        self.graph.add_edge(2, 5)

        # Create a NetworkX graph object
        G = nx.Graph()
        for src in range(vertices):
            for dest in self.graph.get_neighbors(src):
                G.add_edge(src, dest)

        # Plot the graph using Matplotlib
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')

        plt.title("Graph")
        plt.show()

        messagebox.showinfo("Graph Created", "Graph has been created.")

    def search(self):
        start_node = int(self.start_entry.get())
        goal_node = int(self.goal_entry.get())
        algorithm = self.algorithm_var.get()

        if algorithm == "BFS":
            path = self.bfs(start_node, goal_node)
        elif algorithm == "DFS":
            path = self.dfs(start_node, goal_node)
        elif algorithm == "DLS":
            depth_limit = 3  # Set the desired depth limit
            path = self.dls(start_node, goal_node, depth_limit)
        elif algorithm == "IDS":
            path = self.ids(start_node, goal_node)
        elif algorithm == "UCS":
            path = self.ucs(start_node, goal_node)
        elif algorithm == "Bidirectional":
            path = self.bidirectional_search(start_node, goal_node)
        elif algorithm == "BestFS":
            path = self.best_first_search(start_node, goal_node)
        elif algorithm == "A*":
            path = self.a_star_search(start_node, goal_node)
        else:
            messagebox.showerror("Error", "Invalid algorithm selected.")
            return

        # Create a new figure
        plt.figure()

        # Create a NetworkX graph object
        G = nx.Graph()
        for src in range(self.graph.vertices):
            for dest in self.graph.get_neighbors(src):
                if (src, dest) in path or (dest, src) in path:
                    G.add_edge(src, dest, color='red')  # Highlight the path
                else:
                    G.add_edge(src, dest, color='gray')

        # Plot the graph using Matplotlib
        pos = nx.spring_layout(G)
        edge_colors = [G[u][v]['color'] for u, v in G.edges()]
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color=edge_colors, font_weight='bold')

        plt.title("Graph")
        plt.show()

        if path:
            messagebox.showinfo("Path Found", "Path: {}".format(path))
        else:
            messagebox.showinfo("No Path Found", "No path found.")

    def bfs(self, start, goal):
        visited = [False] * self.graph.vertices
        queue = Queue()
        queue.put(start)
        visited[start] = True
        parent = [-1] * self.graph.vertices

        while not queue.empty():
            vertex = queue.get()
            if vertex == goal:
                return self.construct_path(parent, goal)
            neighbors = self.graph.get_neighbors(vertex)
            for neighbor in neighbors:
                if not visited[neighbor]:
                    queue.put(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = vertex

        return []

    def dfs(self, start, goal):
        visited = [False] * self.graph.vertices
        stack = [start]
        visited[start] = True
        parent = [-1] * self.graph.vertices

        while stack:
            vertex = stack.pop()
            if vertex == goal:
                return self.construct_path(parent, goal)
            neighbors = self.graph.get_neighbors(vertex)
            for neighbor in neighbors:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = vertex

        return []

    def dls(self, start, goal, depth_limit):
        visited = [False] * self.graph.vertices
        stack = [(start, 0)]
        visited[start] = True
        parent = [-1] * self.graph.vertices

        while stack:
            vertex, depth = stack.pop()
            if vertex == goal:
                return self.construct_path(parent, goal)
            if depth < depth_limit:
                neighbors = self.graph.get_neighbors(vertex)
                for neighbor in neighbors:
                    if not visited[neighbor]:
                        stack.append((neighbor, depth + 1))
                        visited[neighbor] = True
                        parent[neighbor] = vertex

        return []

    def ids(self, start, goal):
        depth_limit = 0
        while True:
            path = self.dls(start, goal, depth_limit)
            if path:
                return path
            depth_limit += 1

    def ucs(self, start, goal):
        visited = [False] * self.graph.vertices
        priority_queue = PriorityQueue()
        priority_queue.put((0, start))
        visited[start] = True
        parent = [-1] * self.graph.vertices
        cost = [float('inf')] * self.graph.vertices
        cost[start] = 0

        while not priority_queue.empty():
            _, vertex = priority_queue.get()
            if vertex == goal:
                return self.construct_path(parent, goal)
            neighbors = self.graph.get_neighbors(vertex)
            for neighbor in neighbors:
                edge_cost = self.graph.adjacency_matrix[vertex][neighbor]
                new_cost = cost[vertex] + edge_cost
                if not visited[neighbor] or new_cost < cost[neighbor]:
                    priority_queue.put((new_cost, neighbor))
                    visited[neighbor] = True
                    parent[neighbor] = vertex
                    cost[neighbor] = new_cost

        return []

    def bidirectional_search(self, start, goal):
        forward_visited = [False] * self.graph.vertices
        backward_visited = [False] * self.graph.vertices
        forward_queue = Queue()
        backward_queue = Queue()
        forward_queue.put(start)
        backward_queue.put(goal)
        forward_visited[start] = True
        backward_visited[goal] = True
        forward_parent = [-1] * self.graph.vertices
        backward_parent = [-1] * self.graph.vertices

        intersect_node = -1
        while not forward_queue.empty() and not backward_queue.empty():
            forward_vertex = forward_queue.get()
            backward_vertex = backward_queue.get()

            if forward_visited[backward_vertex]:
                intersect_node = backward_vertex
                break
            elif backward_visited[forward_vertex]:
                intersect_node = forward_vertex
                break

            forward_neighbors = self.graph.get_neighbors(forward_vertex)
            for neighbor in forward_neighbors:
                if not forward_visited[neighbor]:
                    forward_queue.put(neighbor)
                    forward_visited[neighbor] = True
                    forward_parent[neighbor] = forward_vertex

            backward_neighbors = self.graph.get_neighbors(backward_vertex)
            for neighbor in backward_neighbors:
                if not backward_visited[neighbor]:
                    backward_queue.put(neighbor)
                    backward_visited[neighbor] = True
                    backward_parent[neighbor] = backward_vertex

        if intersect_node == -1:
            return []

        path = []
        node = intersect_node
        while node != -1:
            path.append(node)
            node = forward_parent[node]

        path = path[::-1]  # Reverse the path

        node = backward_parent[intersect_node]
        while node != -1:
            path.append(node)
            node = backward_parent[node]

        return path

    def best_first_search(self, start, goal):
        visited = [False] * self.graph.vertices
        priority_queue = PriorityQueue()
        priority_queue.put((0, start))
        visited[start] = True
        parent = [-1] * self.graph.vertices

        while not priority_queue.empty():
            _, vertex = priority_queue.get()
            if vertex == goal:
                return self.construct_path(parent, goal)
            neighbors = self.graph.get_neighbors(vertex)
            for neighbor in neighbors:
                if not visited[neighbor]:
                    priority_queue.put((self.heuristic(neighbor, goal), neighbor))
                    visited[neighbor] = True
                    parent[neighbor] = vertex

        return []

    def a_star_search(self, start, goal):
        visited = [False] * self.graph.vertices
        priority_queue = PriorityQueue()
        priority_queue.put((0, start))
        visited[start] = True
        parent = [-1] * self.graph.vertices
        cost = [float('inf')] * self.graph.vertices
        cost[start] = 0

        while not priority_queue.empty():
            _, vertex = priority_queue.get()
            if vertex == goal:
                return self.construct_path(parent, goal)
            neighbors = self.graph.get_neighbors(vertex)
            for neighbor in neighbors:
                edge_cost = self.graph.adjacency_matrix[vertex][neighbor]
                new_cost = cost[vertex] + edge_cost
                if not visited[neighbor] or new_cost < cost[neighbor]:
                    priority_queue.put((new_cost + self.heuristic(neighbor, goal), neighbor))
                    visited[neighbor] = True
                    parent[neighbor] = vertex
                    cost[neighbor] = new_cost

        return []

    def heuristic(self, current, goal):
        # Calculate and return the heuristic value
        return abs(current - goal)

    def construct_path(self, parent, goal):
        path= []
        node = goal
        while node != -1:
            path.append(node)
            node = parent[node]
        path.reverse()
        return path


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#F0F0F0")
    gui = SearchGUI(root)
    root.mainloop()
