""" 
Code is taken from: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
Changes has been done to accomadate the spesific task we have been given here.




"""

from Map import Map_Obj


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def manhatten(p1,p2): #use the manhatten distance as the h function. 
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def astar(mapobj, start, end, task):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    maze = mapobj.int_map
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add start node to the list of open nodes. 
    open_list.append(start_node)

    # While loop until one find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1], end_node.position # Return path from the goal. 

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # adjacent squares for left, right, over and under. 

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == -1:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            #for closed_child in closed_list: This was done by the downloaded code, however this made it code slow. 
                
            if closed_list.count(child)>0:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + maze[child.position[0]][child.position[1]]
            child.h = manhatten(child.position,end_node.position) 
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

        # Moving goal for task 5
        if task == 5:
            mapobj.tick()
            end = tuple(mapobj.goal_pos)
            end_node = Node(None, end)
            end_node.g = end_node.h = end_node.f = 0