import numpy as np

def internal_to_cartesian(dist_H1_H2, dist_H3_H4, theta_1, theta_2, Phi, R):
    # Calculate the coordinates of H1 and H2 based on the distance from the center of mass of H1 and H2
    H1_x = (dist_H1_H2 / 2) * np.cos(theta_1)
    H1_y = (dist_H1_H2 / 2) * np.sin(theta_1)
    H1_z = 0

    # Calculate the coordinates of H2
    H2_x = -H1_x
    H2_y = -H1_y
    H2_z = 0

    # Defining the coordinates of R
    R = np.array([R, 0.0, 0.0])

    # Calculate the Cartesian coordinates of H3 and H4
    H3_x = R[0] + (dist_H3_H4 / 2) * np.cos(theta_2)
    H4_x = R[0] - (dist_H3_H4 / 2) * np.cos(theta_2)
    H3_y = (dist_H3_H4 / 2) * np.cos(Phi)
    H4_y = -H3_y
    H3_z = (dist_H3_H4 / 2) * np.sqrt(np.sin(theta_2)**2 - np.cos(Phi)**2)
    H4_z = -H3_z

    # Return the Cartesian coordinates
    return [
        np.array([H1_x, H1_y, H1_z]),
        np.array([H2_x, H2_y, H2_z]),
        np.array([H3_x, H3_y, H3_z]),
        np.array([H4_x, H4_y, H4_z]),
    ]

# Internal coordinates (distances in Å, angles in radians)
dist_H1_H2 = 2.586
dist_H3_H4 = 4.678
theta_1 = 1.54
theta_2 = 14.45
Phi = 7
R =  5

# Convert internal coordinates to Cartesian coordinates
result = internal_to_cartesian(dist_H1_H2, dist_H3_H4, theta_1, theta_2, Phi, R)

print("Cartesian Coordinates:")
for i, atom in enumerate(result):
    print("Atom {}: {}".format(i+1, atom))


