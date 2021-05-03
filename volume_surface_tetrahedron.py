#!/usr/bin/env python3
# Created by: Jonathan Kene
# Created on: May. 3, 2021
# This program asks the user for the edge length
# of the tetrahedron in m. It then
# calculates and displays the volume and
# surface area.
import math


def main():

    # input
    print("Today we will calculate the volume and")
    print("surface area of a tetrahedron")
    edge = int(input("Enter the edge length (m): "))

    # process
    volume = edge**3/6*math.sqrt(2)
    surface_area = math.sqrt(3*edge**2)

    # output
    print("")
    print("volume = {:.2f} m^3". format(volume))
    print("surface_area = {:.2f} m^2". format(surface_area))


if __name__ == "__main__":
    main()
