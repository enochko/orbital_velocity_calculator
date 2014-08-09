'''
This module contains:
(1) newtons_orbital_velocity(radius_orbit, g, drop_increment) function to
estimate the orbital velocity (in km/s) of an object in a circular orbit around
a primary body with an orbit radius of radius_orbit (in km), an acceleration
due to gravity of g, and a drop increment of drop_increment (in km) by using
Newton's cannonball thought experiment, Pythagoras's theorem, and the constant
linear acceleration formula.

(2) v(mu, r, a) function to
calculate the precise orbital velocity (in km/s) of an object in an elliptical
orbit around a primary body, where the object has a negligible mass (compared
to the primary body), and the body has a standard gravitational parameter of mu,
the object is at distance r, and the semi-major axis of the elliptical orbit is
a.

This module also contains the following constants:
(1) radius_Earth = radius of Earth, 6371.0 km
(2) g0 = standard acceleration due to gravity of Earth at sea level, 9.80665 ms**-2
(3) mu_Earth = standard gravitational constant of Earth, 398600.4418 km**3 s**-2


Author: Enoch Ko
Email:  contact@enochko.com
Website: http://www.enochko.com/
'''
import math

# Declare global constants
radius_Earth = 6371.0	# radius of Earth in km
g0 = 9.80665			# acceleration due to gravity of Earth at sea level in ms**-2
mu_Earth = 398600.4418	# standard gravitational constant of Earth in km**3 s**-2

def newtons_orbital_velocity(radius_orbit, g = g0, drop_increment = 1.0):
    '''
    This function estimates the orbital velocity (in km/s) using Newton's
    cannonball thought experiment, Pythagoras's theorem, and the constant
    linear acceleration formula.
    
    newtons_orbital_velocity = estimated orbital velocity in km/s [float]
    radius_orbit = radius of orbit (in km) [positive, float, no default]
    g = acceleration due to gravity at orbital radius (in km/s**2) [positive,
    		float, default = g0]
    drop_increment = distance (in km) for the object to fall [positive, float,
    		default = 1.0]
    		
    Author: Enoch Ko
    Email:  contact@enochko.com
    Website: http://www.enochko.com/
    '''

	# Calculate time required (in seconds) to fall through the drop increment.
	# Using the constant linear acceleration formula: s = ut + 1/2 at**2
	# Where initial vertical velocity u is 0 km/s.
    m_per_km = 1000.0		# m to km conversion factor
    time_to_drop = math.sqrt(2 * drop_increment * m_per_km / g)
    

	# Calculate radius at drop point in km
    # The drop point is the location where the vertical distance between the
    # orbit and the tangent to the point of origin equals the drop increment.
    radius_drop = radius_orbit + drop_increment
    
	# Calculate the distance from the origin to the drop point (in km) using
	# Pythagoras's theorem.
    distance_origin_to_drop = math.sqrt(radius_drop ** 2 - radius_orbit ** 2)

    # The orbital velocity will be the point at which the object will travel
    # the distance from the origin to the drop point in the time it takes for
    # accleration due to gravity to cause it to fall the drop increment.
    # i.e. the object will fall as fast as Earth is curving away from it.
    orbital_velocity = distance_origin_to_drop / time_to_drop # in km/s
    return orbital_velocity

def v(r, a, mu = mu_Earth):
    '''
    This function calculates the precise orbital velocity (in km/s) of an
    object in an elliptical orbit around a primary body using orbital mechanics,
    assuming the orbiting object has negligible mass as compared to the primary
    body.
    
    v = orbital velocity of the object in km/s [float]
    r = distance of object from centre of the primary body in km [positive,
    		float]
    a = length of semi-major axis of the elliptical orbit [positive, float]
	mu = standard gravigational constant in km**3 s**-2 [positive, float,
			default = mu_Earth]
	0
	Author: Enoch Ko
	Email:  contact@enochko.com
	Website: http://www.enochko.com/
	'''
    # Calculate the orbital velocity using orbital mechanics formula
    velocity = math.sqrt(mu * (2.0 / r - 1.0 / a))
    return velocity

def main():
    # Get user input of orbit altitude
    altitude = float(input("What is the orbital altitude above Earth's " \
							"sea level (in km)? "))
    
    # Calculate orbit radius in km
    radius_orbit = radius_Earth + altitude
    
    # Calculate the acceleration due to gravity of Earth in ms**-2, scaled 
    # for the effect of altitude above sea level
    gh = g0 * (radius_Earth / radius_orbit) ** 2
    
	# Set drop increment distance
    drop_increment = 1.0	# km
    
    # Calculate and print estimated orbital velocity
    orbital_velocity_est = newtons_orbital_velocity(radius_orbit, gh, drop_increment)
    print "\nThe estimated orbital velocity of an object in", \
    "circular orbit around Earth at", altitude, "km above", \
    "sea level is approximately", orbital_velocity_est, "km/s.\n"
    
    # Calculate the length of the semimajor axis of the orbit in km
    # For circular orbits:
    semimajor_axis = radius_orbit
    
    # Calculate and print precise orbital velocity
    orbital_velocity_precise = v(radius_orbit, semimajor_axis, mu_Earth)
    print "The precise orbital velocity of an object in", \
    "circular orbit around Earth at", altitude, "km above", \
    "sea level is", orbital_velocity_precise, "km/s.\n"
    
    # Calculate and print variance between precise and estimated orbital
    # velocity.
    variance = orbital_velocity_precise - orbital_velocity_est
    print "The variance between the precise orbital velocity", \
    "and the estimated orbital velocity is", variance, "km/s." 


if __name__ == "__main__":
    main()