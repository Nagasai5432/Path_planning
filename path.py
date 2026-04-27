import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import heapq
import random

# -----------------------------
# SETTINGS
# -----------------------------
grid_size = 10
start = (0, 0)
goal = (9, 9)

speed = 0.2
use_smoothing = True
random_obstacles = False

# -----------------------------
# GRID
# -----------------------------
def create_grid():
    grid = np.zeros((grid_size, grid_size))

    if random_obstacles:
        for _ in range(20):
            x = random.randint(0, grid_size-1)
            y = random.randint(0, grid_size-1)
            if (x, y) not in [start, goal]:
                grid[x, y] = -1
    else:
        grid[3, 5] = -1
        grid[6, 2:8] = -1
        grid[1:5, 9] = -1
        grid[1:8, 3] = -1

    return grid

# -----------------------------
# HEURISTIC
# -----------------------------
def heuristic(a, b):
    return np.hypot(a[0]-b[0], a[1]-b[1])

# -----------------------------
# NEIGHBORS
# -----------------------------
def get_neighbors(grid, pos):
    x, y = pos
    moves = [
        (1,0), (-1,0), (0,1), (0,-1),
        (1,1), (1,-1), (-1,1), (-1,-1)
    ]

    result = []
    for dx, dy in moves:
        nx, ny = x+dx, y+dy

        if 0 <= nx < grid_size and 0 <= ny < grid_size:
            if grid[nx, ny] == -1:
                continue

            if dx != 0 and dy != 0:
                if grid[x+dx, y] == -1 or grid[x, y+dy] == -1:
                    continue

            result.append((nx, ny))
    return result

# -----------------------------
# A*
# -----------------------------
def astar(grid):
    open_heap = []
    heapq.heappush(open_heap, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    open_set = {start}
    closed_set = set()

    visited_order = []

    while open_heap:
        _, current = heapq.heappop(open_heap)

        open_set.discard(current)
        closed_set.add(current)
        visited_order.append(current)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1], visited_order, g_score

        for neighbor in get_neighbors(grid, current):
            if neighbor in closed_set:
                continue

            dx = abs(neighbor[0]-current[0])
            dy = abs(neighbor[1]-current[1])
            cost = 1.414 if dx and dy else 1

            temp_g = g_score[current] + cost

            if neighbor not in g_score or temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g

                f = temp_g + heuristic(neighbor, goal)
                f_score[neighbor] = f

                heapq.heappush(open_heap, (f, neighbor))
                open_set.add(neighbor)

    return None, visited_order, g_score

# -----------------------------
# SMOOTH PATH
# -----------------------------
def interpolate_path(path):
    smooth = []
    for i in range(len(path)-1):
        x1, y1 = path[i]
        x2, y2 = path[i+1]

        dist = np.hypot(x2-x1, y2-y1)
        steps = max(2, int(dist / speed))

        for t in np.linspace(0, 1, steps):
            x = x1 + (x2-x1)*t
            y = y1 + (y2-y1)*t
            smooth.append((x, y))

    return smooth

# -----------------------------
# DRAW
# -----------------------------
def draw(grid, visited, path=None, robot=None, steps=0, explored=0, cost=0):
    display = np.ones_like(grid)
    display[grid == -1] = 0

    for v in visited:
        display[v] = 6

    if path:
        for p in path:
            display[p] = 4

    display[start] = 2
    display[goal] = 3

    plt.clf()
    plt.imshow(display, cmap=cmap)

    if robot:
        plt.scatter(robot[1], robot[0], s=80)

    plt.title(
        f"Steps: {steps} | Explored: {explored} | Cost: {round(cost,2)}\n"
        f"[r]=restart  [o]=random  [s]=smooth  [+/-]=speed"
    )

    plt.xticks(np.arange(-0.5, grid_size, 1))
    plt.yticks(np.arange(-0.5, grid_size, 1))
    plt.grid(True)
    plt.tick_params(left=False, bottom=False,
                    labelleft=False, labelbottom=False)

    plt.pause(0.05)

# -----------------------------
# CONTROLS
# -----------------------------
def on_key(event):
    global restart, random_obstacles, use_smoothing, speed

    if event.key == 'r':
        restart = True
    elif event.key == 'o':
        random_obstacles = not random_obstacles
        restart = True
    elif event.key == 's':
        use_smoothing = not use_smoothing
        restart = True
    elif event.key == '+':
        speed = max(0.05, speed - 0.05)
    elif event.key == '-':
        speed += 0.05

# -----------------------------
# MAIN LOOP
# -----------------------------
cmap = ListedColormap([
    'black','white','green','red',
    'purple','blue','yellow'
])

plt.figure(figsize=(6,6))
plt.gcf().canvas.mpl_connect('key_press_event', on_key)

while True:
    restart = False

    grid = create_grid()
    path, visited, g_score = astar(grid)

    if path is None:
        print("❌ No path found")
        continue

    # show exploration
    for i in range(len(visited)):
        if restart: break
        draw(grid, visited[:i], steps=i, explored=i)

    if restart: continue

    # path cost
    cost = g_score.get(goal, 0)

    # smoothing
    final_path = interpolate_path(path) if use_smoothing else path

    steps = 0

    for pos in final_path:
        if restart: break
        steps += 1
        draw(grid, visited, path, pos, steps, len(visited), cost)

    if not restart:
        print(f"✅ Done | Steps: {steps} | Cost: {cost}")