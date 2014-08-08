'''
This module calculates the orbital velocity (in km/s) of an object
in circular orbit around Earth at a given altitude (in km) above
sea level by using Newton's cannonball analogy, pythagoras theorem,
and the constant linear acceleration formula, and by using orbital
mechanics formula.

Author: Enoch Ko
Email:  contact (at) enochko.com
Website: http://www.enochko.com/
'''
import math

# Declare global constants
radius_earth = 6371.0	# radius of Earth in km
g0 = 9.80665			# acceleration due to gravity of Earth at sea level in ms**-2
m_per_km = 1000.0		# m to km conversion factor
drop_increment = 1.0	# incremental distance in km
std_grav_para = 398600.4418 # standard gravitational constant of Earth in km**3 s**-2

def newtons_orbital_velocity(radius_orbit):
	# Calculate radius at drop point in km
    # The drop point is the location where the distance between ground at sea level
    # and the tangent to the point of origin equals the drop increment.
    radius_drop = radius_orbit + drop_increment
    
	# Calculate the distance from the origin to the drop point (in km) using Pythagoras's theorem.
    distance_origin_to_drop = math.sqrt(radius_drop ** 2 - radius_orbit ** 2)

	# Calculate the acceleration due to gravity in ms**-2, scaled for the effect of altitude above sea level
    gh = g0 * (radius_earth / radius_orbit) ** 2

	# Calculate the time required (in seconds) to drop through the drop increment.
	# Using the s = ut + 1/2 at**2 formula
    time_to_drop = math.sqrt(2 * drop_increment * m_per_km / gh)
    
    # The orbital velocity will be the point at which the object will travel the
    # distance from the origin to the drop point in the time it takes for
    # accleration due to gravity to cause it to fall the drop increment.
    # i.e. the object will fall as fast as Earth is curving away from it.
    orbital_velocity = distance_origin_to_drop / time_to_drop # in km/s
    return orbital_velocity

def orbit_velocity(radius_orbit, semimajor_axis):
    # Calculate the orbital velocity using orbital mechanics formula
    orbital_velocity = math.sqrt(std_grav_para * (2.0 / radius_orbit - 1.0 / semimajor_axis))
    return orbital_velocity

def main():
    altitude = float(input("What is the orbital altitude above Earth's sea level (in km)? "))
    
    # Calculate orbit radius in km
    radius_orbit = radius_earth + altitude
    
    orbital_velocity_est = newtons_orbital_velocity(radius_orbit)
    print "\nThe estimated orbital velocity of an object in", \
    "circular orbit around Earth at", altitude, "km above", \
    "sea level is approximately", orbital_velocity_est, "km/s.\n"
    
    # Calculate the length of the semimajor axis in km
    semimajor_axis = radius_orbit		 # For circular orbits, semimajor axis of orbit = radius of orbit
    
    orbital_velocity_precise = orbit_velocity(radius_orbit, semimajor_axis)
    print "The precise orbital velocity of an object in", \
    "circular orbit around Earth at", altitude, "km above", \
    "sea level is", orbital_velocity_precise, "km/s.\n"
    
    variance = orbital_velocity_precise - orbital_velocity_est
    print "The variance between the precise orbital velocity", \
    "and the estimated orbital velocity is", variance, "km/s." 


if __name__ == "__main__":
    main()