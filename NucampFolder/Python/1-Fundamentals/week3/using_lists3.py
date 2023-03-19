states = ["Washington", "Oregon", "California"]
h = "Hello mama"
after = h.center(50)
print(after)
i = 0
for s in states:
    
    if "Ore" in s:
        print(s)
    elif "Ore" not in s:
        print(f"No 'Ore' found in {s}")
        i += 1
print(f"{i} are not 'Ore'")




'''
    print("Washington" in states)
    print("tenessee" in states)
    print("Washington" not in states)

states2 = ["Arizona", "Ohio", "Louisiana"]

best_states = states + states2
print(best_states)

print(best_states[1:3])
print(best_states[:2])
print(best_states[4:])
'''