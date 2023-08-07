def max_altitude(data: list) -> int:
    max = 0
    for record in data:
        if record.altitude > max:
            max = record.altitude
    return max

def min_altidude(data: list) -> int:
    min = 9999999999
    for record in data:
        if record.altitude < min:
            min = record.altitude
    return min

def avg_altitude(data: list) -> int:
    total = 0
    count = 0
    for record in data:
        total += record.altitude
        count += 1
    return total / count

def determine_status(data: list) -> str:
    warning_last_min = False
    for record in data:
        if record.altitude < 160:
            warning_last_min = True
    if data[len(data)-1].altitude < 160:
        return 'WARNING: RAPID ORBITAL DECAY IMMINENT'
    if data[len(data)-1].altitude >= 160 and warning_last_min:
        return 'Sustained Low Earth Orbit Resumed'
    return 'Altitude is A-OK'


