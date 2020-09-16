from DL import Map_Obj, astar

def main():
    task = 1
    while task != 6:

        #Creates a map object
        mapobj=Map_Obj(task)

        #Gets start and goal from map object
        start=tuple(mapobj.start_pos)
        end=tuple(mapobj.goal_pos)

        #Calles astar-algorithm
        path, end, goal_path= astar(mapobj, start, end, task)
        print(goal_path)
        #Draws path on map
        for p in path:
            mapobj.replace_map_values(p,0,end)
        for gp in goal_path:
            mapobj.replace_map_values(gp,-2,end)
        mapobj.show_map()
        print(path)

        task = task + 1

        input("Press Enter to continue...")

main()
