#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 19:44:34 2025

@author: razia
"""

graph = {
    'Razia': ['Rosie', 'Inaya'],
    'Rosie': ['Mona'],
    'Inaya': ['Manaly'],
    'Mona': [],
    'Manaly': []
}

# ----------- Recursive DFS -----------
def dfs_recursive(graph, start, visited=None):
    """
    Recursive DFS to explore all friends from a given student.
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")
    
    for friend in graph.get(start, []):
        if friend not in visited:
            dfs_recursive(graph, friend, visited)

# ----------- Iterative DFS using Stack -----------
def dfs_stack(graph, start):
    """
    Iterative DFS using an explicit stack.
    """
    visited = set()
    stack = [start]
    
    while stack:
        student = stack.pop()
        if student not in visited:
            print(student, end=" ")
            visited.add(student)
            
            # Push neighbors to stack in reverse order for consistent order with recursion
            neighbors = graph.get(student, [])
            stack.extend(reversed(neighbors))

# -------------------- MAIN PROGRAM --------------------
if __name__ == "__main__":
    print("Friendship Exploration using DFS")
    print("--------------------------------\n")
    
    print("Recursive DFS starting from Razia:")
    dfs_recursive(graph, 'Razia')
    print("\n")
    
    print("Iterative DFS (using stack) starting from Razia:")
    dfs_stack(graph, 'Razia')
    print("\n")
    
    # Bonus: Allow user input
    user_start = input("Enter a student's name to explore their friends: ").strip()
    
    if user_start in graph:
        print("Recursive DFS :")
        dfs_recursive(graph, user_start)
        print(" ")
        print("Iterative DFS:")
        dfs_stack(graph, user_start)
    else:
        print("Student not found in the graph.")
