import numpy as np
import os

# Input values for the initial and final geometries
T_initial = np.array([1.40621, 0.23757])  
T_final = np.array([4.0, 1.0])    

# Number of steps for LIIC
N = 21

# Calculate the interpolation vector using the formula
liic = T_final - T_initial

# Initialize arrays to store interpolated geometries
interpolated_geometries = []

# Loop over steps and calculate interpolated geometries
for i in range(N):
    interpolated_geometry = T_initial + (i * liic) / (N-1)
    interpolated_geometries.append(interpolated_geometry)

# Specify the output file
output_file = "D:/M2_STAGE/orbitals/LIIC/LIIC_final/h4_LL_SF_CAS_augpvdz_final_1.com"
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Write the linked file content
with open(output_file, 'w') as f:
    for i, geom in enumerate(interpolated_geometries):
        a1 = geom[0]
        a2 = geom[1]
        
        z_matrix = f"""
%chk=h4_T_CASSCF_augpvdz_{i+1:02d}.chk
#P cas(4,4, Nroot=3, StateAverage)/aug-cc-pVDZ geom=nocrowd pop=full
  gfinput iop(6/7=3) scf=(maxcycles=5000) density=current

h4_T_{i+1:02d}

0 1
X
X 1 1.0
X 1 {a1} 2 90.0
X 3 1.0  1 90.0 2 0.0
H 1 {a2} 3 0.0 4 90.0
H 1 {a2} 2 90.0 5 180.0
H 3 {a2} 1 0.0 2 90.0
H 3 {a2} 4 90.0 7 180.0

0.33 0.33 0.33

"""
        f.write(z_matrix.strip())
        if i < N - 1:
            f.write("\n--Link1--\n")
            f.write(f"%oldchk=h4_T_CASSCF_augpvdz_{i+1:02d}.chk\n")
            f.write(f"%chk=h4_T_CASSCF_augpvdz_{i+2:02d}.chk\n")

print(f"Linked file saved to {output_file}")

