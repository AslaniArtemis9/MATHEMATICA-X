"""Educational Newtonian test-particle orbit integrator (velocity-Verlet)."""
import math
import numpy as np
G = 6.67430e-11

def simulate_two_body(central_mass, radius, duration, steps=4000):
    central_mass, radius, duration = map(float, (central_mass, radius, duration))
    if not all(map(math.isfinite, (central_mass, radius, duration))):
        raise ValueError("Mass, radius and duration must be finite.")
    if central_mass <= 0 or radius <= 0 or duration <= 0:
        raise ValueError("Mass, radius and duration must be positive.")
    if isinstance(steps, bool) or int(steps) != steps or steps < 1 or steps > 2_000_000:
        raise ValueError("steps must be an integer between 1 and 2,000,000.")
    steps = int(steps)
    dt = duration / steps
    position = np.array([radius, 0.0, 0.0], dtype=float)
    speed = math.sqrt(G * central_mass / radius)
    velocity = np.array([0.0, speed, 0.0], dtype=float)
    positions = np.empty((steps + 1, 3), dtype=float)
    times = np.linspace(0.0, duration, steps + 1)
    def acceleration(r):
        norm = np.linalg.norm(r)
        if not math.isfinite(norm) or norm <= np.finfo(float).tiny:
            raise ArithmeticError("Numerical trajectory reached the central singularity.")
        return -G * central_mass * r / norm**3
    acc = acceleration(position)
    for i in range(steps + 1):
        positions[i] = position
        if i == steps: break
        next_position = position + velocity*dt + 0.5*acc*dt**2
        next_acc = acceleration(next_position)
        velocity = velocity + 0.5*(acc + next_acc)*dt
        position, acc = next_position, next_acc
        if not np.isfinite(position).all() or not np.isfinite(velocity).all():
            raise ArithmeticError("Numerical integration became unstable; increase the number of steps.")
    return times, positions
