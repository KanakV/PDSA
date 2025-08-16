def no_overlap(L):
    schedule = []

    ordered_slots = sortByEnd(L)

    schedule.append(ordered_slots.pop(0))

    for slot in ordered_slots:
        if slot[1] > schedule[-1][2]:
            schedule.append(slot)
    
    ids = []
    for slot in schedule:
        ids.append(slot[0])

    return ids
    

def sortByEnd(slots):
    end = lambda slot:int(slot[2])
    ordered = sorted(slots, key = end)

    return ordered


L = [
    (0, 1, 2),
    (1, 1, 3),
    (2, 1, 5),
    (3, 3, 4),
    (4, 4, 5),
    (5, 5, 8),
    (6, 7, 9),
    (7, 10, 13),
    (8, 11, 12)
]

print(no_overlap(L))