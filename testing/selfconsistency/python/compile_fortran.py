import os

names = ["first_neigh","kpm","berry","gauss_inv"] # names of folders
names += ["clean_geometry"] # names of folders
names += ["correlators"] # names of folders

for name in names:
  os.chdir("fortran/"+name) # move to folder
  os.system("sh compile.sh") # compile
  os.chdir("../..") # return to parent

