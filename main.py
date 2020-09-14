from DL import Map_Obj, astar

def main():
    mapobj=Map_Obj(task=4)
    start=tuple(mapobj.start_pos)
    end=tuple(mapobj.goal_pos)
    path = astar(mapobj.int_map, start, end)
    for p in path:
        mapobj.replace_map_values(p,0,end)
    mapobj.show_map()
    print(path)

main()