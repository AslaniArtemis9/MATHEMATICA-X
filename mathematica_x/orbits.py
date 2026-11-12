"""Educational Newtonian two-body orbit integrator (velocity-Verlet)."""
import numpy as np
G = 6.67430e-11

def simulate_two_body(central_mass, radius, duration, steps=4000):
    if central_mass <= 0 or radius <= 0 or duration <= 0:
        raise ValueError("Mass, radius and duration must be positive.")
    dt = duration / steps
    position = np.array([radius, 0.0, 0.0])
    speed = np.sqrt(G * central_mass / radius)
    velocity = np.array([0.0, speed, 0.0])
    positions = np.empty((steps + 1, 3))
    times = np.linspace(0.0, duration, steps + 1)
    def acceleration(r):
        norm = np.linalg.norm(r)
        return -G * central_mass * r / norm**3
    acc = acceleration(position)
    for i in range(steps + 1):
        positions[i] = position
        if i == steps: break
        next_position = position + velocity*dt + 0.5*acc*dt**2
        next_acc = acceleration(next_position)
        velocity = velocity + 0.5*(acc + next_acc)*dt
        position, acc = next_position, next_acc
    return times, positions
