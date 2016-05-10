**README for CBB_Bioinformatics_FinalProject_4.1**
---------------------------------------------------------------
Tool that calculates the net Lennard-Jones potential at a query point, given a PDB input file. An R tool that accomplishes the same task can be found [here](https://github.com/graceliu2016/Final-Project-4.2).  
## Note: 
This tool is part of a set of bioinformatic and biological structure tools created for CBB752 at Yale University in the Spring 2016. The website containing links to the set of tools can be found at: http://cbb752spring2016.github.io/

# The Python tool that accomplishes this task is named LJpotential.py.

## General

The Python tool that accomplishes this task is named LJpotential. LJpotential takes 4 required inputs (inputfile, x, y, z) and 2 optional inputs (epsilon_h, sigma). The x, y, and z inputs are the coordinates of the query point. The inputfile is the name of the PDB file from which we will calculate the Lennard-Jones potential. Because default PDB files include all atoms in an amino acid residue, not just the alpha carbons, we have written this code so that it can process either a default PDB file or a PDB file containing only alpha carbons. The total calculated Lennard-Jones potential for the query point, expressed in kcal/mol, will display in the console.

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

```
python LJpotential.py -i <input file> -x <query point x-coordinate> -y <query point y-coordinate> -z <query point z-coordinate> -e <epsilon> -s <sigma>
```
###Example  
```
python LJpotential.py -i 1AHO.pdb -x 10 -y 12 -z 5
>43.2213685538
```

Alternately, using sigma and epsilon values from Kravats et al. [3]
```
python LJpotential.py -i 1AHO.pdb -x 10 -y 12 -z 8 -e 2.125 -s 3.8
>0.39394012214
```

### References

[1] http://www.sigmaaldrich.com/life-science/metabolomics/learning-center/amino-acid-reference-chart.html

[2] Veitshans T, Klimov D, Thirumalai D. Protein folding kinetics: Timescales, pathways and energy landscapes in terms of sequence-dependent properties. Fold Des. 1997;2(1):1–22. 

[3] Kravats A., Jayasinghe M., Stan G. Unfolding and translocation pathway of substrate protein controlled by structure in repetitive allosteric cycles of the ClpY ATPase. Proc. Natl. Acad. Sci. USA. 2011;108:2234–2239.

