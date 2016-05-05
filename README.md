**README for CBB_Bioinformatics_FinalProject_4.1**
---------------------------------------------------------------
Tool that calculates the net Lennard-Jones potential at a given query point

## Note: 
This tool is part of a set of bioinformatic and biological structure tools created for CBB752 at Yale University in the Spring 2016. The website containing links to the set of tools can be found at: http://cbb752spring2016.github.io/

# The R tool that accomplishes this task is named LJpotential.Rmd.

## General

The R tool that accomplishes this task is named LJpotential. LJpotential takes 4 required inputs (inputfile, x, y, z) and 2 optional inputs (epsilon_h, sigma). The x, y, and z inputs are the coordinates of the query point. The inputfile is the name of the PDB file from which we will calculate the Lennard-Jones potential. Because default PDB files include all atoms in an amino acid residue, not just the alpha carbons, we have written this code so that it can process either a default PDB file or a PDB file containing only alpha carbons. The code will run after loading the function from the LJpotential.rmd file. The calculated Lennard-Jones potential, expressed in kcal/mol, will display in the console.

### Input Options for LJpotential:

Required:

1. inputfile - the name of the input file (1AHO.pdb)
2. x - x-coordinate of the query point, in angstroms
3. y - y-coordinate of the query point, in angstroms
4. z - z-coordinate of the query point, in angstroms

Optional:

5. epsilon_h - hydrophobic potential, in kcal/mol
6. sigma - Van der Waals radius of amino acids, in angstroms

If optional inputs are not specified, we will use a default epsilon_h value of 1 kcal/mol and a default sigma value of 5 angstroms, adapted from Veitshans, Klimov, & Thirumalai (1996).

### Usage

```{r}
LJpotential(inputfile = "1AHO.pdb", ???, ???, ???)
```
