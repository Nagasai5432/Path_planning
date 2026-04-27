# Path_planning
An interactive Python-based simulation that demonstrates grid-based path planning algorithms used in robotics, including A* and Dijkstra, with real-time visualization, heuristic tuning, and dynamic obstacle handling.
🎯 Project Overview

This project simulates how autonomous robots plan paths in a 2D environment. It visualizes:

Node exploration
Shortest path generation
Algorithm efficiency
Real-time replanning under changing environments

Built to bridge the gap between theoretical algorithms and real-world robotic navigation systems (like ROS2 Nav2).

✨ Features

✅ A* Path Planning
✅ Dijkstra Algorithm (toggle mode)
✅ Heuristic Switching (Euclidean vs Manhattan)
✅ Dynamic Obstacle Injection (real-time replanning)
✅ Path Smoothing (continuous motion simulation)
✅ Performance Metrics:

Nodes explored
Path cost
Execution time

✅ Interactive Controls
✅ Clean Visualization using Matplotlib

🧠 Algorithms Used
🔹 A* Algorithm
Combines cost-so-far (g) and heuristic (h)
Ensures optimal and efficient pathfinding
🔹 Dijkstra Algorithm
Uniform cost search (no heuristic)
Guarantees shortest path but explores more nodes
🔹 Heuristics
Euclidean Distance
Manhattan Distance
