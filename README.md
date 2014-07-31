Orbital Velocity Calculator
===========================

This Python 2-based calculator estimates the orbital velocity of an object in a circular orbit around Earth at a given altitude above sea level.

The calculator estimates the velocity based on Newton's cannonball analogy, with a little pythygoras theorem and the s = ut + 1/2*(at^2) formula.

Assumptions:
* No air resistance at any altitude.
* Earth is a perfect sphere.
* Earth's acceleration due to gravity (and gravity) is uniform.

Imagine a cannonball being fired out of a cannon. It should travel in a straight line, if not for acceleration due to gravity. At orbital velocity, the cannonball will be falling as quickly as the surface of Earth is curving away from the cannonball. This model estimates the orbital velocity where the cannonball drops an arbitrary distance of 1km and the Earth curves away from it by the same arbitrary distance of 1km.