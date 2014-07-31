'''
This module estiamtes the calculates the orbital velocity (in km/s) of an object around Earth at a given altitude (in km) above sea level by using Newton's "firing a cannonball" analogy, pythagoras theorem, and s = ut + 1/2at**2.
Author: Enoch Ko
Email:  contact (at) enochko.com
Website: http://www.enochko.com/
'''
import math

# Declare constants
radius_earth = 6371.0	# radius of Earth in km
g0 = 9.80665			# acceleration due to gravity at sea level in ms**-2
m_per_km = 1000.0		# m to km conversion factor
drop_increment = 1.0	# incremental distance in km

def orbit_velocity_calc(altitude):
	# Calculate orbit radius in km
    radius_orbit = radius_earth + float(altitude)

	# Calculate radius at drop point in km
    # The drop point is the location where the distance between ground at sea level
    # and the tangent to the point of origin equals the drop increment.
    radius_drop = radius_orbit + drop_increment
    
	# Calculate the distance from the origin to the drop point (in km) using the pythagoras theorem.
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

def main():
    altitude = input("What is the orbital altitude above Earth's sea level (in km)? ")
    orbital_velocity = orbit_velocity_calc(altitude)
    print "The circular orbital velocity around Earth at", altitude, "km above sea level is", orbital_velocity, "km/s."

if __name__ == "__main__":
    main()