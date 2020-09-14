from DL import Map_Obj, astar

def main():
    #Specifies task number
    task = 5

    #Creates a map object
    mapobj=Map_Obj(task)

    #Gets start and goal from map object
    start=tuple(mapobj.start_pos)
    end=tuple(mapobj.goal_pos)

    #Calles astar-algorithm
    path, end = astar(mapobj, start, end, task)

    #Draws path on map
    for p in path:
        mapobj.replace_map_values(p,0,end)
    mapobj.show_map()
    print(path)

main()