import os, sys
import numpy as np
sys.path.append("C:/Program Files/Coreform Cubit 2025.3/bin")

import cubit
cubit.init(['cubit','-nojournal','-batch'])


cubit.cmd('create Cylinder height 80.0 radius 40.0 ')
cubit.cmd('mesh volume 1 ')
cubit.cmd('block 1 add ( hex all with z > 0 ) in volume 1')
cubit.cmd('block 1 name "work"')
cubit.cmd(f'save cub5 "c:/cubit.cub5" overwrite journal')

for block_id in cubit.get_block_id_list():

	all_nodes = set()
	elem_types = ["hex", "tet", "wedge", "pyramid"]
	for elem_type in elem_types:
		if elem_type == "hex":
			func = getattr(cubit, f"get_block_{elem_type}es")
		else:
			func = getattr(cubit, f"get_block_{elem_type}s")
		for element_id in func(block_id):
			node_ids = cubit.get_connectivity(elem_type, element_id)
			all_nodes.update(node_ids)

		print(f"block_id = {block_id}  node_list = {all_nodes}")



