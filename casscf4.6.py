import matplotlib.pyplot as plt
import numpy as np
import re

# File path
file_path = 'D:/M2_STAGE/h4_LL_CAS_augpvdz_final_roots.log'

# Initialize lists to store the values
eigenvalue_1 = []
eigenvalue_2 = []
eigenvalue_3 = []
eigenvalue_4 = []
eigenvalue_5 = []

# Match the eigenvalues
pattern_1 = re.compile(r'\(\s*1\)\s*EIGENVALUE\s*(-?\d+\.\d+)')
pattern_2 = re.compile(r'\(\s*2\)\s*EIGENVALUE\s*(-?\d+\.\d+)')
pattern_3 = re.compile(r'\(\s*3\)\s*EIGENVALUE\s*(-?\d+\.\d+)')
pattern_4 = re.compile(r'\(\s*4\)\s*EIGENVALUE\s*(-?\d+\.\d+)')
pattern_5 = re.compile(r'\(\s*5\)\s*EIGENVALUE\s*(-?\d+\.\d+)')

# Read the file and extract the values
with open(file_path, 'r') as file:
    for line in file:
        match_1 = pattern_1.search(line)
        if match_1:
            eigenvalue_1.append(float(match_1.group(1)))
        
        match_2 = pattern_2.search(line)
        if match_2:
            eigenvalue_2.append(float(match_2.group(1)))

        match_3 = pattern_3.search(line)
        if match_3:
            eigenvalue_3.append(float(match_3.group(1)))

        match_4 = pattern_4.search(line)
        if match_4:
            eigenvalue_4.append(float(match_4.group(1)))
        
        match_5 = pattern_5.search(line)
        if match_5:
            eigenvalue_5.append(float(match_5.group(1)))

# Number of intermediate geometries
num_geometries = len(eigenvalue_1)

# Create x-axis data: intermediate geometries from 1 to num_geometries
geometries = np.arange(1, num_geometries + 1)

# Energy values for geometries in Hartrees
energies_casscf_44_S0 = eigenvalue_1
energies_casscf_44_S1 = eigenvalue_2
energies_casscf_44_S2 = eigenvalue_3
energies_casscf_44_T1 = eigenvalue_4
energies_casscf_44_T2 = eigenvalue_5

# Compute overall minima in Hartrees using S0 as reference
min_casscf_44_S0 = np.min(energies_casscf_44_S0)

# Compute relative energies in Hartrees
rel_energies_casscf_44_S0 = energies_casscf_44_S0 - min_casscf_44_S0
rel_energies_casscf_44_S1 = energies_casscf_44_S1 - min_casscf_44_S0
rel_energies_casscf_44_S2 = energies_casscf_44_S2 - min_casscf_44_S0
rel_energies_casscf_44_T1 = energies_casscf_44_T1 - min_casscf_44_S0
rel_energies_casscf_44_T2 = energies_casscf_44_T2 - min_casscf_44_S0

# Convert relative energies from Hartrees to electronvolts (eV)
hartree_to_ev = 27.2114

rel_energies_casscf_44_S0_ev = rel_energies_casscf_44_S0 * hartree_to_ev
rel_energies_casscf_44_S1_ev = rel_energies_casscf_44_S1 * hartree_to_ev
rel_energies_casscf_44_S2_ev = rel_energies_casscf_44_S2 * hartree_to_ev
rel_energies_casscf_44_T1_ev = rel_energies_casscf_44_T1 * hartree_to_ev
rel_energies_casscf_44_T2_ev = rel_energies_casscf_44_T2 * hartree_to_ev

# Print final relative energies method by method
def print_relative_energies(geometries, rel_energies, method_name, labels):
    for i in range(len(geometries)):
        print(f"{method_name} relative energies for geometry {geometries[i]} (eV):")
        for energy, label in zip(rel_energies, labels):
            print(f"{label}: {energy[i]:.6f}")
        print()

print("Final Relative Energies in eV")
print("=============================")
print_relative_energies(geometries, [rel_energies_casscf_44_S0_ev, rel_energies_casscf_44_S1_ev, rel_energies_casscf_44_S2_ev, rel_energies_casscf_44_T1_ev, rel_energies_casscf_44_T2_ev], "CASSCF(4,4)", ['S0', 'S1', 'S2', 'T1', 'T2'])

# Define function to plot relative energies
def plot_relative_energies(geometries, rel_energies, method_name, labels):
    plt.figure(figsize=(12, 8))
    for energy, label in zip(rel_energies, labels):
        plt.plot(geometries, energy, marker='x', label=label)
    plt.title(f'Relative Energies of Different Excited States for {method_name}')
    plt.xlabel('Geometries')
    plt.ylabel('Relative Energy (eV)')
    plt.legend()
    plt.xticks(np.arange(1, num_geometries + 1, 1))
    plt.show()

# Plot the relative energies
plot_relative_energies(geometries, [rel_energies_casscf_44_S0_ev, rel_energies_casscf_44_S1_ev, rel_energies_casscf_44_S2_ev, rel_energies_casscf_44_T1_ev, rel_energies_casscf_44_T2_ev], "CASSCF(4,4)", ['S0', 'S1', 'S2', 'T1', 'T2'])









