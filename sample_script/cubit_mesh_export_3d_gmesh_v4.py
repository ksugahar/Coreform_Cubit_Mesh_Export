########################################################################
###	Gmsh format version 4
########################################################################

def export_3D_gmsh_ver4(cubit, FileName):


	with open(FileName, 'w') as fid:

		fid.write('$MeshFormat\n')
		fid.write('4.1 0 8\n')
		fid.write('$EndMeshFormat\n')

		n_block_1d = 0
		n_block_2d = 0
		n_block_3d = 0

		fid.write('$PhysicalNames\n')
		fid.write(f'{cubit.get_block_count()}\n')
		for block_id in cubit.get_block_id_list():
			if len(cubit.get_block_edgess(block_id)) > 0:
				fid.write(f'1 {block_id} "{name}"\n')
				n_block_1d += 1
			elif len(cubit.get_block_tris(block_id)) + len(cubit.get_block_faces(block_id))> 0:
				fid.write(f'2 {block_id} "{name}"\n')
				n_block_2d += 1
			else:
				fid.write(f'3 {block_id} "{name}"\n')
				n_block_3d += 1
		fid.write('$EndPhysicalNames\n')
		fid.write('$Entities\n')
		fid.write(f'{0} {n_block_1d} {n_block_2d} {n_block_3d}\n')

		for nodeset_id in cubit.get_nodeset_id_list():
			surface_list = cubit.get_nodeset_surfaces(nodeset_id)
			for surface_id in surface_list:
				bounding_box = cubit.get_bounding_box("surface", surface_id)
				minx = bounding_box[0]
				maxx = bounding_box[1]
				miny = bounding_box[3]
				maxy = bounding_box[4]
				minz = bounding_box[6]
				maxz = bounding_box[7]
				fid.write(f'{surface_id} {minx} {miny} {minz} {maxx} {maxy} {maxz} {1} {nodeset_id} {0}\n')

		for block_id in cubit.get_block_id_list():
			for volume_id in cubit.get_block_volumes(block_id):
				bounding_box = cubit.get_bounding_box("volume", volume_id)
				minx = bounding_box[0]
				maxx = bounding_box[1]
				miny = bounding_box[3]
				maxy = bounding_box[4]
				minz = bounding_box[6]
				maxz = bounding_box[7]
				fid.write(f'{volume_id} {minx} {miny} {minz} {maxx} {maxy} {maxz} {1} {block_id} {nodeset_surface_count}')
				for nodeset_id in cubit.get_nodeset_id_list():
					surface_list = cubit.get_nodeset_surfaces(nodeset_id)
					for surface_id in surface_list:
						fid.write(f' {surface_id}')
				fid.write(f'\n')

		fid.write('$EndEntities\n')

		counts = 0
		node_all_set = set()
		for nodeset_id in cubit.get_nodeset_id_list():
			surface_list = cubit.get_nodeset_surfaces(nodeset_id)
			for surface_id in surface_list:
				node_list = cubit.get_surface_nodes(surface_id)
				if len(node_list) > 0:
					node_all_set.update(node_list)
					counts += 1

		for block_id in cubit.get_block_id_list():
			for volume_id in cubit.get_block_volumes(block_id):
				node_list = cubit.parse_cubit_list( "node", f"in volume {volume_id}" )
				if len(node_list) > 0:
					node_all_set.update(node_list)
					counts += 1

		fid.write('$Nodes\n')
		fid.write(f'{counts} {len(node_all_set)} {min(node_all_set)} {max(node_all_set)}\n')

		node_all_set.clear()

		for nodeset_id in cubit.get_nodeset_id_list():
			surface_list = cubit.get_nodeset_surfaces(nodeset_id)
			for surface_id in surface_list:
				node_list = cubit.get_surface_nodes(surface_id)
				node_list = set(node_list) - node_all_set
				if len(node_list) > 0:
					node_all_set.update(node_list)
					fid.write(f'2 {surface_id} 0 {len(node_list)}\n')
					for node_id in node_list:
						fid.write(f'{node_id}\n')
					for node_id in node_list:
						coord = cubit.get_nodal_coordinates(node_id)
						fid.write(f'{coord[0]} {coord[1]} {coord[2]}\n')

		for block_id in cubit.get_block_id_list():
			for volume_id in cubit.get_block_volumes(block_id):
				node_list = cubit.parse_cubit_list( "node", f"in volume {volume_id}" )
				node_list = set(node_list) - node_all_set
				if len(node_list) > 0:
					node_all_set.update(node_list)
					fid.write(f'3 {volume_id} 0 {len(node_list)}\n')
					for node_id in node_list:
						fid.write(f'{node_id}\n')
					for node_id in node_list:
						coord = cubit.get_nodal_coordinates(node_id)
						fid.write(f'{coord[0]} {coord[1]} {coord[2]}\n')

		fid.write('$EndNodes\n')

		tri_all_list = []
		quad_all_list = []
		tet_all_list = []
		hex_all_list = []
		wedge_all_list = []

		fid.write('$Elements\n')

		for nodeset_id in cubit.get_nodeset_id_list():
			surface_list = cubit.get_nodeset_surfaces(nodeset_id)
			for surface_id in surface_list:
				tri_all_list += cubit.get_surface_tris(surface_id)
				quad_all_list += cubit.get_surface_quads(surface_id)

		for block_id in cubit.get_block_id_list():
			for volume_id in cubit.get_block_volumes(block_id):
				tet_all_list += cubit.get_volume_tets(volume_id)
				hex_all_list += cubit.get_volume_hexes(volume_id)
				wedge_all_list += cubit.get_volume_wedges(volume_id)

		elementTag = 1

		all_list =  quad_all_list + tri_all_list + hex_all_list + tet_all_list  + wedge_all_list
		if len(all_list) > 0:
			fid.write(f'{ nodeset_surface_count + block_volume_count} {len(all_list)} {min(all_list)} {max(all_list)}\n')
		else:
			fid.write(f'{ nodeset_surface_count + block_volume_count} 0 0 0\n')

		for nodeset_id in cubit.get_nodeset_id_list():
			surface_list = cubit.get_nodeset_surfaces(nodeset_id)
			for surface_id in surface_list:
				tri_list = cubit.get_surface_tris(surface_id)
				if len(tri_list)>0:
					fid.write(f'2 {surface_id} 2 {len(tri_list)}\n')
					for tri_id in tri_list:
						node_list = cubit.get_connectivity("tri", tri_id)
						elementTag +=1
						fid.write(f'{elementTag} {node_list[0]} {node_list[1]} {node_list[2]}\n')

				quad_list = cubit.get_surface_quads(surface_id)
				if len(quad_list)>0:
					fid.write(f'2 {surface_id} 3 {len(quad_list)}\n')
					for quad_id in quad_list:
						node_list = cubit.get_connectivity("quad", quad_id)
						elementTag +=1
						fid.write(f'{elementTag} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]}\n')

		for block_id in cubit.get_block_id_list():
			for volume_id in cubit.get_block_volumes(block_id):
				tet_list = cubit.get_volume_tets(volume_id)
				if len(tet_list)>0:
					fid.write(f'3 {volume_id} 4 {len(tet_list)}\n')
					for tet_id in tet_list:
						node_list = cubit.get_connectivity("tet", tet_id)
						elementTag +=1
						fid.write(f'{elementTag} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]}\n')

				hex_list = cubit.get_volume_hexes(volume_id)
				if len(hex_list)>0:
					fid.write(f'3 {volume_id} 5 {len(hex_list)}\n')
					for hex_id in hex_list:
						node_list = cubit.get_connectivity("hex", hex_id)
						elementTag +=1
						fid.write(f'{elementTag} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]} {node_list[6]} {node_list[7]}\n')

				wedge_list = cubit.get_volume_wedges(volume_id)
				if len(wedge_list)>0:
					fid.write(f'3 {volume_id} 6 {len(wedge_list)}\n')
					for wedge_id in wedge_list:
						node_list = cubit.get_connectivity("wedge", wedge_id)
						elementTag +=1
						fid.write(f'{elementTag} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]}\n')

		fid.write('$EndElements\n')
		fid.close()
	return cubit

