#!/usr/bin/env python

import ase.io
import numpy as np
import sys, os

def load_data(filename):
  ''' Input:    filename   - string, name of traj containing the data
      Returns:  atoms_list - list of ASE atoms objects https://wiki.fysik.dtu.dk/ase/ase/atoms.html
                atoms_data - list of dictionaries (same len/order as in atoms_list); keys: 
                             'idx': indices of Al atoms in the ASE atoms objects (np.array)
                             'iso': isotropic shielding of Al atoms (np.array)
  '''
  # load ASE trajectory file https://wiki.fysik.dtu.dk/ase/ase/io/io.html
  atoms_list = ase.io.read(filename, index=':', format='traj')
  
  # features and target values in data will have the same order as in key_names
  atoms_data = []
  for atoms in atoms_list:
    # get indices of Al atoms in the structure
    idx = np.where(atoms.get_atomic_numbers() == 13)[0]
    # get isotropic shielding from the 'info' dictionary for every Al atom in 'atoms'
    iso = np.array([v['iso'] for v in atoms.info.values()])
    atoms_data.append({'idx': idx,
                       'iso': iso})
  return atoms_list, atoms_data

### TASK
# A) write a function that generates structural features describing the atomic environment of the Al atoms in 
#    the structures stored as ASE atoms objects in 'atoms_list'


# B) write a function that correlates the structural features with the isotropic shieldings stored in 'atoms_data'
#    (the atoms indices 'idx' of the Al atoms are probably helpful; you can use one or more regression techniques of your choice)
# C) quantify the performance of the regressor(s)
  
if __name__ == "__main__":
  ifile = sys.argv[1]
  atoms_list, atoms_data = load_data(ifile)
  # execute your functions here
