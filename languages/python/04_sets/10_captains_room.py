size = int(input())
room_number_list = list(map(int, input().split(' ')))
room_tourist_map = {}

for item in room_number_list:
    room_tourist_map[item] = room_tourist_map.get(item, 0) + 1
    
for room, tourist in room_tourist_map.items():
    if tourist == 1:
        print(room)
