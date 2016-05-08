### Title: LJpotential.py
### Purpose: A tool that calculates the Lennard-Jones potential between a query point and the alpha carbons of a PBD file in kcal/mol.
### Created Date: 06 May 2016
### Created By: Heather Wells

###Usage: python LJpotential.py -i <input file> -x <query point x-coordinate> -y <query point y-coordinate> -z <query point z-coordinate> -e <epsilon> -s <sigma>

### Example: python LJpotential.py -i 1AHO.pdb -x 10 -y 12 -z 8 -e 2.125 -s 3.8

### Notes: Requires input file in pdb format and x,y,z query point coordinates in angstroms.  Optional epsilon hydrophobic potential must be given in kca/mol, and sigma Van der Waals radius must be given in angstroms.  If no epsilon or sigma is specified, the defaults of 1 kcal/mol and 5 angstroms are used.

#import libraries
import math

#import arguments
import argparse
parser=argparse.ArgumentParser(description='Leonard Jones')
parser.add_argument('-i', '--input', help='input file name', required=True)
parser.add_argument('-x', '--xcoord', help='query point x-coordinate', required=True, type=float)
parser.add_argument('-y', '--ycoord', help='query point y-coordinate', required=True, type=float)
parser.add_argument('-z', '--zcoord', help='query point z-coordinate', required=True, type=float)
parser.add_argument('-e', '--epsilon', help='epsilon hydrophobic potential', default=1, type=float)
parser.add_argument('-s', '--sigma', help='sigma Van der Waals radius', default=5, type=float)
args=parser.parse_args()

def LJpotential(inputfile,x,y,z,epsilon,sigma):
    
    #open and save inputs
    with open(args.input) as input:
        input=input.read().splitlines()

    #initialize empty list for alpha carbons
    alphaC_res=[]
    alphaC_dist=[]

    #pull out only alpha carbons, row always starts with ATOM and includes CA
    #using x,y,z coordinates (character positions are standard for pdb files), calculate distance from query point and store
    #store residue type
    for i in range(0,len(input)):
        if input[i][0:4]=="ATOM":
            if input[i][12:16]==" CA ":
                x_dist=float(input[i][30:38])-x
                y_dist=float(input[i][38:46])-y
                z_dist=float(input[i][46:54])-z
                dist=math.sqrt(math.pow(x_dist,2)+math.pow(y_dist,2)+math.pow(z_dist,2))
                alphaC_res.append(input[i][17:20])
                alphaC_dist.append(dist)

    #initialize with VLJ=0
    #calculate potential based on hydrophobicity of residue type
    #sum potentials for all atoms
    VLJ=0.
    for i in range(0,len(alphaC_res)):
        if alphaC_res[i] in ["ARG","LYS","ASN","GLU","PRO","ASP"]: #lower epsilon for hydrophilic residues
            VLJ+=4*2./3*epsilon*(math.pow(sigma/alphaC_dist[i],12)+math.pow(sigma/alphaC_dist[i],6))
        if alphaC_res[i] in ["THR","HIS","GLY","SER","GLN"]: #no repulsive term for neutral residues
            VLJ+=4*epsilon*(math.pow(sigma/alphaC_dist[i],12))
        if alphaC_res[i] not in ["ARG","LYS","ASN","GLU","PRO","ASP","THR","HIS","GLY","SER","GLN"]: 
            VLJ+=4*epsilon*(math.pow(sigma/alphaC_dist[i],12)+math.pow(sigma/alphaC_dist[i],6))
            
    print VLJ


LJpotential(args.input,args.xcoord,args.ycoord,args.zcoord,args.epsilon,args.sigma)

    
