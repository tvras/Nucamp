states = ["Washington", "Oregon", "California"]

'''
for s in states:
    s = s.lower()
    print(s)
'''
'''
    print("Washington" in states)
    print("tenessee" in states)
    print("Washington" not in states)
'''
states2 = ["Arizona", "Ohio", "Louisiana"]

best_states = states + states2
print(best_states)

print(best_states[1:3])
print(best_states[:2])
print(best_states[4:])