This repository contains the scripts that I used for my Master Thesis Project 2024. An overview and purpose of each script has been discussed below:
## LIIC (Linear Interpolation in Internal Coordinates) Script

### Description

The **LIIC** (Linear Interpolation in Internal Coordinates) script is designed for computational chemists to facilitate the generation of a reaction pathway by linearly interpolating between the internal coordinates of reactant and product molecular structures. This method is particularly useful in approximating the transition states of chemical reactions.

The script automates the creation of intermediate geometries along the reaction path, which can then be used for further computational analyses, such as energy calculations and transition state searches. The key features of the script include:

- **Input Handling**: Accepts the internal coordinates of reactant and product geometries.
- **Interpolation Process**: Generates a specified number of intermediate geometries between the reactant and product structures by linearly interpolating internal coordinates.
- **Output**: Produces the internal coordinates of intermediate geometries, which are then used to form the z-matrix and then further create the input file for CASSCF (4,4) Calculation in the given directory to be used for Gaussian 16. This creates a linked file for all the intermediate geometries. Separate files can also be created.
This script is a valuable tool for working on reaction mechanisms, providing a straightforward and efficient way to model the reaction pathway and investigate potential transition states.

## CASSCF Energies Script

### Description

The **CASSCF_energies** script facilitates the extraction, calculation, and visualization of energies from CASSCF calculations. This tool is particularly useful for working with electronic structure methods and excited state calculations.

The script performs the following key functions:

- **Input Handling**: Reads energy values from log files generated by Gaussian 16.
- **Energy Calculation**: Processes and calculates the relative energies of different electronic states (ground and excited states) using the extracted data based on the minima of the Potential Energy Surface.
- **Visualization**: Plots the relative energies of various states to aid in analyzing and interpreting computational results.

## Cartesian to Internal Coordinates Script

### Description

The **Cartesian to Internal Coordinates** script is designed to convert Cartesian coordinates of molecular structures into internal coordinates. This script is specific for the H<sub>2</sub> dimer system system considered in 6D

The script provides the following functionalities:

- **Input Handling**: Reads molecular geometries provided in Cartesian coordinates format.
- **Coordinate Transformation**: Converts the Cartesian coordinates into internal coordinates such as bond lengths, bond angles, and dihedral angles.
- **Output**: Outputs the internal coordinates, which can be used for further computational analyses and simulations.

This script is a valuable tool to work with internal coordinates of H<sub>2</sub> dimer in 6D. Another script was also written to do the vice-versa transformation and is named as **Internal to Cartesian**

