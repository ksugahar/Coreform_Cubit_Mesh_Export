import os, sys
import numpy as np
sys.path.append("C:/Program Files/Coreform Cubit 2025.3/bin")

import cubit
cubit.init(['cubit','-nojournal','-batch','nographics','-nogui','-noecho'])

if len(sys.argv) > 1:
	FileName = sys.argv[1]
else:
	FileName = 'SPM'
with open(FileName + '.jou','r') as fid:
	strLines = fid.readlines()
	for n in range(len(strLines)):
		cubit.cmd(strLines[n])

import cubit_mesh_export
cubit_mesh_export.export_2D_gmsh_ver2(cubit, FileName + '.msh')

cubit.cmd(f'save cub5 "C:/cubit.cub5" overwrite journal')

