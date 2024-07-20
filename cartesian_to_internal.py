import numpy as np

def cartesian_to_internal(cartesian_coords):
    # Calculate interatomic distances
    dist_H1_H2 = np.linalg.norm(cartesian_coords[1] - cartesian_coords[0])
    dist_H3_H4 = np.linalg.norm(cartesian_coords[3] - cartesian_coords[2])
    
    # Calculate the centre of masses of both systems
    com_H12 = center_of_mass([cartesian_coords[0], cartesian_coords[1]])
    print('com_H12:', com_H12)
    com_H34 = center_of_mass([cartesian_coords[2], cartesian_coords[3]])
    print('com_H34:', com_H34)
    
    # Define the distances between their centers of mass
    R = np.linalg.norm(com_H34 - com_H12)

    # Calculate theta 
    theta_1 = np.arccos(np.dot((cartesian_coords[0] - com_H12), (com_H34 - com_H12)) / (np.linalg.norm(cartesian_coords[0] - com_H12) * np.linalg.norm(com_H34 - com_H12)))
    theta_2 = np.arccos(np.dot((cartesian_coords[2] - com_H34), (com_H34 - com_H12)) / (np.linalg.norm(cartesian_coords[3] - com_H34) * np.linalg.norm(com_H34 - com_H12)))

    # Calculate dihedral angle
    S_1 = np.cross((cartesian_coords[0] - com_H12), (com_H34 - com_H12))
    S_2 = np.cross((cartesian_coords[2] - com_H34), (com_H34 - com_H12))
    Phi = np.arccos(np.dot(S_1, S_2) / (np.linalg.norm(S_1) * np.linalg.norm(S_2)))

    # Print all the internal coordinates
    print("Interatomic Distances:")
    print("r1:", dist_H1_H2)
    print("r2:", dist_H3_H4)
    print ("R:", R)
    print("Angles:")
    print("theta_1:", theta_1)
    print("theta_2:", theta_2)
    print("Phi:", Phi)
    

def center_of_mass(atoms):
    total_mass = sum([1.008 for _ in atoms])  # Masses of H atoms in atomic mass units
    com = np.zeros(3)
    for atom in atoms:
        com += atom
    com /= len(atoms)
    return com

# Define coordinates in the code
H1 = np.array([0.03981336, 1.2923869, 0])
H2 = np.array([-0.03981336 , -1.2923869,  0.00000000e+00 ])
H3 = np.array([4.28016006, 1.76337737, 1.35766406])
H4 = np.array([5.71983994, -1.76337737, -1.35766406])
cartesian_coords = [H1, H2, H3, H4]

cartesian_to_internal(cartesian_coords)

