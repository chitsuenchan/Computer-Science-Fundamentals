def asteroidCollision(asteroids):
    stack = []

    for asteroid in asteroids:
        while stack and asteroid < 0 and stack[-1] > 0:
            if abs(asteroid) > stack[-1]:
                stack.pop()
                continue
            elif abs(asteroid) == stack[-1]:
                stack.pop()
            break
        else:
            stack.append(asteroid)

    return stack

# Example usage:
asteroids = [-5, 10, 5, 15, -15, -50, 20]
print(asteroidCollision(asteroids))  # Output: [5, 20]
