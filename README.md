Orbital Velocity Calculator
===========================

These calculators calculate the orbital velocity of an object in a circular 
orbit around Earth at a given altitude above sea level.

The calculator estimates the velocity based on Newton's cannonball analogy,
with a little help from Pythygoras's theorem and the constant linear
acceleration formula.

The calculator also calculates the precise orbital velocity using orbital
mechanics, and calculates the variance between the precise orbital velocity
and the estimate.

Assumptions:
* No air resistance at any altitude.
* Earth is a perfect sphere.
* Earth's gravity and acceleration due to gravity is uniform.
* The object has negligible mass compared the Earth's mass.

## Newton's Cannonball Thought Experiment
Imagine a cannonball being fired out of a cannon. It should travel in a
straight line, if not for acceleration due to gravity.

Gravity will cause the cannonball to fall towards Earth at a constant rate
of acceleration.

When the cannon is fired at normal velocity, the cannonball will fall to the
ground at some distance from the cannon.

When the cannon is fired at a higher velocity, the cannonball fly even further
before falling to the ground.

At orbital velocity, the cannonball will be falling as quickly as the surface
of Earth is curving away from the cannonball.

## How This Model Estimates Orbital Velocity
This model estimates the orbital velocity by calculating how long it takes for
the cannonball to drop an arbitrary distance of 1km.

In the time it takes for the cannonball to drop that distance, the cannonball
will have to had travelled such a distance that the Earth curves away from it
by the same arbitrary distance of 1km.

The orbital velocity can be calculated by dividing that horizontal distance
by the time it must have taken to cover that distance.

A more detailed walk-through can be found on my blog post:
[http://www.enochko.com/blog/newtons-cannonball-and-orbital-velocity]