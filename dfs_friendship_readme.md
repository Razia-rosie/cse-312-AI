# friendship-dfs-exploration

## Problem Statement
Write a Python program that explores friendships in a class using Depth-First Search (DFS). The program should allow the user to explore all friends reachable from a given student. The program supports:  
- Recursive DFS  
- Iterative DFS using a stack  
- User input to start the exploration from any student  

## Technology Used
- Python 3

## How to Run the Code
1. Make sure you have Python 3 installed on your system.  
2. Open a terminal and navigate to the project directory.  
3. Run the following command:
   ```
   python3 friendship_dfs.py
   ```
4. The program will display the DFS traversal starting from the default student (`Razia`).  
5. You can also enter the name of any student to explore their friends.

## Sample Input and Output
**Sample Input:**
```
Enter a student's name to explore their friends: Inaya
```

**Sample Output:**
```
Friendship Exploration using DFS
--------------------------------

Recursive DFS starting from Razia:
Razia Rosie Mona Inaya Manaly

Iterative DFS (using stack) starting from Razia:
Razia Inaya Manaly Rosie Mona

Recursive DFS :
Inaya Manaly
Iterative DFS:
Inaya Manaly
```

