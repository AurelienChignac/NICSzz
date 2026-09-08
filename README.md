# NICSzz
A python script to generate Gaussian input files for NICSzz aromaticity evaluation for small molecules presenting distorted rings. The script allows to generate a Gaussian .gjf input file containing Bq probes orthogonal to a distorted ring adopting a boat- or chair-like conformation.
By default, Bq probes are placed from -8 Angstrom to +8 Angstrom under and above the ring and spaced by 0.1 Angstrom. To place them, the script uses the number of the atoms that constitute the basis of the boat.
