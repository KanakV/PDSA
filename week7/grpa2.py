def minimum_platform(schedule : list):
    platforms = []

    schedule = sortByDeparture(schedule)
    platforms.append([schedule.pop(0)])

    for train in schedule:
        scheduled = False
        for platform in platforms:
            if not isTimeClash(platform[-1], train):
                platform.append(train)
                scheduled = True
                break
        if not scheduled:
            platforms.append([train])

            
    return len(platforms)


def sortByDeparture(schedule):
    time = lambda train:train[2]
    ordered = sorted(schedule, key = time)

    return ordered

def isTimeClash(departing, arriving):
    if departing[2] <= arriving[1]:
        return False
    else:
        return True

# print(isTimeClash("9:00", "8:00"))
# print(isTimeClash("9:00", "10:00"))
# print(isTimeClash("9:00", "9:00"))

schedule = [(1,'09:00','09:10'),(2,'09:40','12:00'),(3,'09:50','11:20'),(4,'11:00','11:30'),(5,'11:40','12:10'),(6,'12:05','19:00'),(7,'12:06','13:00'),(8,'13:05','14:00'),(9,'14:05','15:00'),(10,'18:00','20:00')]
# schedule = [(1,'09:00','09:10'),(2,'09:10','10:00'),(3,'10:50','11:20'),(4,'11:25','11:30'),(5,'11:40','12:10'),(6,'12:15','13:00'),(7,'13:06','13:10'),(8,'13:15','14:00'),(9,'14:05','15:00'),(10,'18:00','20:00')]
# print(sortByDeparture(schedule))

# schedule = eval(input())           
print(minimum_platform(schedule))