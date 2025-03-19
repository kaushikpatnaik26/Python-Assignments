def has_antipodal_points(points):
    point_set = set(points) 
    for x, y in points:
        if (-x, -y) in point_set:  
            return True
    return False
points = [(1, 0), (-1, 0), (0, 1), (0, -1)]
print(f'Are antipodal: {has_antipodal_points(points)}') 
