# Initial guest list
guests = [ "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Kevin", "Liam", "Mallory", "Nia", "Oscar", "Peggy", "Quinn", "Riley", "Sybil", "Trent", "Uma", "Victor", "Walter", "Xander", "Yara", "Zane", "Amari", "Blake", "Casey", "Dakota" ]
#challenge 1.1
bobs_plus_one = input("Hi Bob, what is your friend's name? ")
guests.append(bobs_plus_one)
print(f"Added {bobs_plus_one} to the list.")
#challenge 1.2
vip_name = input("Please enter the VIP's name: ")
guests.insert(0, vip_name)
print(f"Added {vip_name} as the VIP at the beginning of the list.")
#challenge 1.3
new_friend_for_alice = input("Alice can't make it. Who is her replacement? ")
try:
    alice_index = guests.index("Alice")
    guests[alice_index] = new_friend_for_alice
    print(f"Replaced Alice with {new_friend_for_alice}.")
except ValueError:
    print("Alice was not found in the list, no replacement made.")
#challenge 1.4
print("Final Guest List")
for i, guest in enumerate(guests, 1):
    print(f"{i}. {guest}")

print(f"Total number of guests attending: {len(guests)}")
