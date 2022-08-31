def asteroidsDestroyed(mass: int, asteroids) -> bool:
    asteroids.sort()
        
    current = mass
        
    for asteroid in asteroids:
        if current < asteroid:
            return False
        current += asteroid
            
    return True

print(asteroidsDestroyed(10, [3, 9, 19, 5, 21]))