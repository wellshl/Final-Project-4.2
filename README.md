**README for CBB_Bioinformatics_FinalProject_4.1**
---------------------------------------------------------------
Tool that calculates the net Lennard-Jones potential at a given query point

## Note: 
This tool is part of a set of bioinformatic and biological structure tools created for CBB752 at Yale University in the Spring 2016. The website containing links to the set of tools can be found at: http://cbb752spring2016.github.io/

# The R tool that accomplishes this task is named LJpotential.Rmd.

## General

The R tool that accomplishes this task is named LJpotential. LJpotential takes 4 required inputs (inputfile, x, y, z) and 2 optional inputs (epsilon_h, sigma). The x, y, and z inputs are the coordinates of the query point. The inputfile is the name of the PDB file from which we will calculate the Lennard-Jones potential. Because default PDB files include all atoms in an amino acid residue, not just the alpha carbons, we have written this code so that it can process either a default PDB file or a PDB file containing only alpha carbons. The code will run after loading the function from the LJpotential.rmd file. The total calculated Lennard-Jones potential for the query point, expressed in kcal/mol, will display in the console.

This tool builds on the BLN model, in which hydrophobic, hydrophilic, and neutral residues have different interaction potentials (epsilon). We classified residues as hydrophobic (B), hydrophilic (L), or neutral (N) based this chart [1] for pH 7. Lennard-Jones potentials for each were type of residue in the BLN model were defined in accordance with Veitshans, Klimov, & Thirumalai (1997) [2].

### Input Options for LJpotential:

Required:

1. inputfile - the name of the input file (1AHO.pdb)
2. x - x-coordinate of the query point, in angstroms
3. y - y-coordinate of the query point, in angstroms
4. z - z-coordinate of the query point, in angstroms

Optional:

5. epsilon_h - hydrophobic potential, in kcal/mol
6. sigma - Van der Waals radius of amino acids, in angstroms

If optional inputs are not specified, we will use a default epsilon_h value of 1 kcal/mol and a default sigma value of 5 angstroms, adapted from Veitshans, Klimov, & Thirumalai (1997) [2].

### Sample Usage

```{r}
LJpotential(inputfile = "1AHO, x = 10, y = 12, z = 8)
```

### References

[1] Veitshans T, Klimov D, Thirumalai D. Protein folding kinetics: Timescales, pathways and energy landscapes in terms of sequence-dependent properties. Fold Des. 1997;2(1):1–22. 
[2] http://www.sigmaaldrich.com/life-science/metabolomics/learning-center/amino-acid-reference-chart.html
