from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# # map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
# print('here',room_graph)
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

## traversal code:

# this will contain back route when player hits dead end
back_path = []

opposite_path = {"n": "s", "s": "n", "e": "w", "w": "e"}

visited = set()

while len(visited) < len(room_graph):
    next_room = None

    # loop over an array of neighbor rooms
    for nextRoom in player.current_room.get_exits():
        # for each nextRoom, if its not been visited, set as the next move
        if player.current_room.get_room_in_direction(nextRoom) not in visited:
            next_room = nextRoom
            # exit from array right away, so it goes into 'depth':
            break

    # continue to explore:
    if next_room is not None:
        traversal_path.append(next_room)
        back_path.append(opposite_path[next_room])

        player.travel(next_room)
        visited.add(player.current_room)
        # print("visited", visited)
    # go back if hit the wall or already visited:
    else:
        next_room = back_path.pop()
        traversal_path.append(next_room)

        player.travel(next_room)

# print("path", traversal_path)
## end

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
