def score(x, y):
    distance = (x**2 + y**2)**0.5
    points = 0
    
    if distance <= 1:
        points = 10
    elif distance <= 5:
        points = 5
    elif distance <= 10:
        points = 1
    return points
