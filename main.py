from DL import Map_Obj, astar

def main():
    task = 5
    mapobj=Map_Obj(task)
    start=tuple(mapobj.start_pos)
    end=tuple(mapobj.goal_pos)
    path, end = astar(mapobj, start, end, task)
    for p in path:
        mapobj.replace_map_values(p,0,end)
    mapobj.show_map()
    print(path)

main()