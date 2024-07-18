import matplotlib.pyplot as plt
import numpy as np

# Number of intermediate geometries
num_geometries = 11

# Create x-axis data: intermediate geometries from 1 to num_geometries
geometries = np.arange(1, num_geometries + 1)

# Energy values for geometries in Hartrees (only using the first two geometries for simplicity)
# Energy values for geometries in Hartrees
# CASSCF(4,4) T_initial to T_Final
energies_casscf_44_S0 = [-2.253695659, -2.253828217, -2.253866263, -2.253946743, -2.253976027, -2.253985344, -2.253976027, -2.253946743, -2.253866263, -2.253828217, -2.253695659]
energies_casscf_44_S1 = [-1.799969747, -1.800866190, -1.802144538, -1.803232981, -1.803987754, -1.804259683, -1.803987754, -1.803232981, -1.802144538, -1.800866190, -1.799969747]
energies_casscf_44_S2 = [-1.798194642, -1.797274034, -1.796160055, -1.795249009, -1.794682943, -1.794489520, -1.794682943, -1.795249009, -1.796160055, -1.797274034, -1.798194642]
energies_casscf_44_T1 = [-1.897944497, -1.897744908, -1.897015035, -1.896148470, -1.894934459, -1.893827015, -1.894934459, -1.896148470, -1.897138315, -1.897744908, -1.897944497]
energies_casscf_44_T2 = [-1.828350179, -1.828003567, -1.826538409, -1.824774647, -1.822016124, -1.819348553, -1.822016124, -1.824774647, -1.826858329, -1.828003567, -1.828350179]

#EOMCCSD
energies_eomccsd_S0 = [-63.38163566, -63.38128355, -63.38046492, -63.37931322, -63.37829481, -63.37785851, -63.37829481, -63.37931322, -63.38046492, -63.38128355, -63.38163566]
energies_eomccsd_S1 = [-50.73353566, -50.75448355, -50.79426492, -50.83171322, -50.85749481, -50.86665851, -50.85749481, -50.83171322, -50.79426492, -50.75448355, -50.73353566]
energies_eomccsd_S2 = [-50.62553566, -50.60808355, -50.57746492, -50.55071322, -50.53319481, -50.52715851, -50.53319481, -50.55071322, -50.57746492, -50.60808355, -50.62553566]

# CASSCF(4,4) L_initial to L_Final
energies_casscf_44_S0 = [-2.254390617, -2.254350365, -2.254231739, -2.254011720, -2.253728718, -2.252927160, -2.253728718, -2.254011720, -2.254231739, -2.254350365, -2.254390617]
energies_casscf_44_S1 = [-1.802462861, -1.801642435, -1.800165373, -1.801036185, -1.804333013, -1.805623400, -1.804333013, -1.801036185, -1.800165373, -1.801642435, -1.802462861]
energies_casscf_44_S2 = [-1.792605989, -1.793849045, -1.797017425, -1.798856838, -1.797860246, -1.796594355, -1.797860246, -1.798856838, -1.797017425, -1.793849045, -1.792605989]
energies_casscf_44_T1 = [-1.891074341, -1.892755466, -1.895795785, -1.897051086, -1.897085036, -1.898288141, -1.897085036, -1.896840940, -1.895795785, -1.892755466, -1.891074341]
energies_casscf_44_T2 = [-1.820004863, -1.821535447, -1.828371160, -1.833333968, -1.832469863, -1.857125342, -1.832469865, -1.826470623, -1.828371154, -1.821535448, -1.820004864]

# EOMCCSD
energies_eomccsd_S0 = [-63.38106259, -63.37974444, -63.37981895, -63.38014285, -63.37848302, -63.37668693, -63.37848302, -63.38014285, -63.38029051, -63.37848302, -63.38106259]
energies_eomccsd_S1 = [-50.82406259, -50.78394444, -50.70691895, -50.76324285, -50.86478302, -50.90018693, -50.86478302, -50.76324285, -50.70439051, -50.86478302, -50.82406259]
energies_eomccsd_S2 = [-50.43226259, -50.48574444, -50.62001895, -50.65174285, -50.63328302, -50.63028693, -50.63328302, -50.65174285, -50.64299051, -50.63328302, -50.43226259]

#CASSCF(4,4) T_L
energies_casscf_44_S0 = [-2.253695659, -2.253721701, -2.253753001, -2.253737763, -2.253618890, -2.253759462, -2.253974981, -2.254157290, -2.254289463, -2.254361565, -2.254390617]
energies_casscf_44_S1 = [-1.799969747, -1.801621808, -1.803667061, -1.804877796, -1.804843704, -1.803286151, -1.800909217, -1.799879053, -1.800984647, -1.801981233, -1.802462861]
energies_casscf_44_S2 = [-1.798194642, -1.796913170, -1.795823082, -1.795584661, -1.795992883, -1.797430986, -1.798631219, -1.797948019, -1.795283766, -1.793337864, -1.792605989]
energies_casscf_44_T1 = [-1.897944497, -1.897595601, -1.896631792, -1.895400946, -1.896142801, -1.897353770, -1.897641122, -1.896946568, -1.895015729, -1.892298152, -1.891074341]
energies_casscf_44_T2 = [-1.828350179, -1.827811200, -1.825501478, -1.821200233, -1.823248025, -1.828005068, -1.829822013, -1.828662471, -1.824874255, -1.821018730, -1.820004862]

# EOMCCSD
energies_eomccsd_S0 = [-63.38163566, -63.38091262, -63.37908647, -63.37753581, -63.37778904, -63.37939125, -63.38044994, -63.38029051, -63.37972698, -63.37994049, -63.38106259]
energies_eomccsd_S1 = [-50.73353566, -50.77831262, -50.84328647, -50.88113581, -50.87888904, -50.83739125, -50.76424994, -50.70439051, -50.74932698, -50.80054049, -50.82406259]
energies_eomccsd_S2 = [-50.62553566, -50.59831262, -50.57488647, -50.57583581, -50.59128904, -50.61239125, -50.63884994, -50.64299051, -50.54812698, -50.46314049, -50.43226259]

# Compute overall minima in Hartrees
min_casscf_44 = np.min([
    np.min(energies_casscf_44_S0)
])

# Compute relative energies in Hartrees
rel_energies_casscf_44_S0 = energies_casscf_44_S0 - min_casscf_44
rel_energies_casscf_44_S1 = energies_casscf_44_S1 - min_casscf_44
rel_energies_casscf_44_S2 = energies_casscf_44_S2 - min_casscf_44
rel_energies_casscf_44_T1 = energies_casscf_44_T1 - min_casscf_44
rel_energies_casscf_44_T2 = energies_casscf_44_T2 - min_casscf_44

# Convert relative energies from Hartrees to electronvolts (eV)
hartree_to_ev = 27.2114

rel_energies_casscf_44_S0_ev = rel_energies_casscf_44_S0 * hartree_to_ev
rel_energies_casscf_44_S1_ev = rel_energies_casscf_44_S1 * hartree_to_ev
rel_energies_casscf_44_S2_ev = rel_energies_casscf_44_S2 * hartree_to_ev
rel_energies_casscf_44_T1_ev = rel_energies_casscf_44_T1 * hartree_to_ev
rel_energies_casscf_44_T2_ev = rel_energies_casscf_44_T2 * hartree_to_ev

# Print final relative energies method by method
def print_relative_energies(geometries, rel_energies, method_name, labels):
    for i, geometry in enumerate(geometries):
        print(f"{method_name} relative energies for {'T configuration' if i == 0 else 'L configuration'} (eV):")
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
        plt.scatter(geometries, energy)
    plt.title(f'Relative Energies of Different Excited States for {method_name}')
    plt.xlabel('Geometries')
    plt.ylabel('Relative Energy (eV)')
    plt.legend()
    plt.xticks(np.arange(1, num_geometries + 1, 1), ['T Geometry', 'L Geometry'])
    plt.show()

# Plot the relative energies
plot_relative_energies(geometries, [rel_energies_casscf_44_S0_ev, rel_energies_casscf_44_S1_ev, rel_energies_casscf_44_S2_ev, rel_energies_casscf_44_T1_ev, rel_energies_casscf_44_T2_ev], "CASSCF(4,4)", ['S0', 'S1', 'S2', 'T1', 'T2'])







