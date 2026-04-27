Path Planning Visualizer (A* | Dijkstra | Dynamic Replanning)

An interactive Python-based simulation that demonstrates grid-based path planning algorithms used in robotics, including A and Dijkstra, with real-time visualization, heuristic tuning, and dynamic obstacle handling.

Project Overview

This project simulates how autonomous robots plan paths in a 2D environment. It visualizes:

 Node exploration
 Shortest path generation
 Algorithm efficiency
 Real-time replanning under changing environments

Built to bridge the gap between theoretical algorithms and real-world robotic navigation systems (like ROS2 Nav2).

---

## Features

--- A Path Planning
--- Dijkstra Algorithm (toggle mode)
--- Heuristic Switching (Euclidean vs Manhattan)
--- Dynamic Obstacle Injection (real-time replanning)
--- Path Smoothing (continuous motion simulation)
--- Performance Metrics:

 Nodes explored
 Path cost
 Execution time

--- Interactive Controls
--- Clean Visualization using Matplotlib

---

## Algorithms Used

### A* Algorithm

 Combines cost-so-far (g) and heuristic (h)
 Ensures optimal and efficient pathfinding

### Dijkstra Algorithm

 Uniform cost search (no heuristic)
 Guarantees shortest path but explores more nodes

### Heuristics

 Euclidean Distance
 Manhattan Distance

## 🎮 Controls

| Key     | Action                  |
| ------- | ----------------------- |
| `a`     | Switch to A            |
| `d`     | Switch to Dijkstra      |
| `h`     | Toggle heuristic        |
| `x`     | Inject dynamic obstacle |
| `r`     | Restart simulation      |
| `o`     | Toggle random obstacles |
| `s`     | Toggle path smoothing   |
| `+ / -` | Adjust speed            |

---

## Installation

#bash
git clone https://github.com/your-username/path-planning-visualizer.git
cd path-planning-visualizer
pip install numpy matplotlib

##Run the Project
#bash
python3 path.py

##Example Output Metrics

 Steps taken by robot
 Nodes explored during search
 Total path cost
 Execution time

##Project Structure

path-planning-visualizer/
│── path.py
│── README.md
│── assets/
│    └── demo.gif

## Real-World Relevance

This project directly relates to:

 Autonomous robot navigation
 ROS2 Nav2 stack
 Self-driving car path planning
 SLAM-based navigation systems

---

##Key Learnings

 Trade-offs between optimality vs speed
 Importance of heuristics in search algorithms
 Handling dynamic environments
 Difference between global planning vs local adaptation

---

##Future Improvements

 ROS2 (Nav2) integration
 Costmap simulation
 Dynamic Window Approach (DWA)
 RRT / RRT implementation
 Multi-agent path planning

---

##Author
Nagasai P
Robotics | Computer Vision | ROS2

---

##If you found this useful

Give it a ⭐ on GitHub and feel free to connect!

---
