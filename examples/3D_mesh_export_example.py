import os, sys
import numpy as np
sys.path.append("C:/Program Files/Coreform Cubit 2025.3/bin")

import cubit
cubit.init(['cubit','-nojournal','-batch'])

if len(sys.argv) > 1:
	FileName = sys.argv[1]
else:
	FileName = './examples/hex20_pyramid13_tetra10_wedge15'

with open(FileName + '.jou','r', encoding='utf8') as fid:
	strLines = fid.readlines()
	for n in range(len(strLines)):
		cubit.cmd(strLines[n])

#for block_id in cubit.get_block_id_list():
#	print(f'block_id = {block_id}')
#	for edge_id in cubit.get_block_edges(block_id):
#		print(edge_id)
#cubit.cmd(f'save cub5 "O:/cubit.cub5" overwrite journal')

import cubit_mesh_export

cubit_mesh_export.export_Gmsh_ver2(cubit, FileName + '.msh')

cubit_mesh_export.export_3D_Nastran(cubit, FileName + '.bdf', PYRAM=False)

cubit_mesh_export.export_meg(cubit, FileName + '.meg', DIM='T', MGR2=[])

cubit_mesh_export.export_vtk(cubit, FileName + '.vtk')

