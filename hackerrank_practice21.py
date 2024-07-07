# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
room_numbers = list(map(int, input().split()))

rooms = set()
repeated_rooms = set()

for number in room_numbers:
    if number in rooms:
        repeated_rooms.add(number)
    else:
        rooms.add(number)

captain_room = rooms - repeated_rooms
print(captain_room.pop())
    
