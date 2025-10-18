########################################################################
###	Gmsh format version 2
########################################################################

def export_Gmsh_ver2(cubit, FileName):

	with open(FileName, 'w') as fid:

		fid.write("$MeshFormat\n")
		fid.write("2.2 0 8\n")
		fid.write("$EndMeshFormat\n")

		fid.write("$PhysicalNames\n")
		fid.write(f'{cubit.get_block_count()}\n')
		for block_id in cubit.get_block_id_list():
			name = cubit.get_exodus_entity_name("block", block_id)
			if len(cubit.get_block_nodes(block_id)) > 0:
				fid.write(f'0 {block_id} "{name}"\n')
			elif len(cubit.get_block_edges(block_id)) > 0:
				fid.write(f'1 {block_id} "{name}"\n')
			elif len(cubit.get_block_tris(block_id)) + len(cubit.get_block_faces(block_id))> 0:
				fid.write(f'2 {block_id} "{name}"\n')
			else:
				fid.write(f'3 {block_id} "{name}"\n')
		fid.write('$EndPhysicalNames\n')

		fid.write("$Nodes\n")
		node_list = set()
		for block_id in cubit.get_block_id_list():
			elem_types = ["hex", "tet", "wedge", "pyramid", "tri", "face", "edge", "node"]
			for elem_type in elem_types:
				if elem_type == "hex":
					func = getattr(cubit, f"get_block_{elem_type}es")
				else:
					func = getattr(cubit, f"get_block_{elem_type}s")
				for element_id in func(block_id):
					node_ids = cubit.get_expanded_connectivity(elem_type, element_id)
					node_list.update(node_ids)

		fid.write(f'{len(node_list)}\n')
		for node_id in node_list:
			coord = cubit.get_nodal_coordinates(node_id)
			fid.write(f'{node_id} {coord[0]} {coord[1]} {coord[2]}\n')
		fid.write('$EndNodes\n')

		hex_list = set()
		tet_list = set()
		wedge_list = set()
		pyramid_list = set()
		tri_list = set()
		quad_list = set()
		edge_list = set()
		node_list = set()

		for block_id in cubit.get_block_id_list():
			tet_list.update(cubit.get_block_tets(block_id))
			hex_list.update(cubit.get_block_hexes(block_id))
			wedge_list.update(cubit.get_block_wedges(block_id))
			pyramid_list.update(cubit.get_block_pyramids(block_id))
			tri_list.update(cubit.get_block_tris(block_id))
			quad_list.update(cubit.get_block_faces(block_id))
			edge_list.update(cubit.get_block_edges(block_id))
			node_list.update(cubit.get_block_nodes(block_id))

		element_id = 0
		fid.write('$Elements\n')
		fid.write(f'{len(hex_list) + len(tet_list) + len(wedge_list) + len(pyramid_list) + len(tri_list) + len(quad_list) + len(edge_list) + len(node_list)}\n')

		for block_id in cubit.get_block_id_list():

			tet_list = cubit.get_block_tets(block_id)
			for tet_id in tet_list:
				element_id += 1
				node_list = cubit.get_expanded_connectivity("tet", tet_id)
				if len(node_list)==4:
					fid.write(f'{element_id} { 4} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]}\n')
				if len(node_list)==10:
					fid.write(f'{element_id} {11} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]} {node_list[6]} {node_list[7]} {node_list[9]} {node_list[8]}\n')
				if len(node_list)==11:
					fid.write(f'{element_id} {35} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]} {node_list[6]} {node_list[7]} {node_list[9]} {node_list[8]} {node_list[10]}\n')

			hex_list = cubit.get_block_hexes(block_id)
			for hex_id in hex_list:
				element_id += 1
				node_list = cubit.get_expanded_connectivity("hex", hex_id)
				if len(node_list)==8:
					fid.write(f'{element_id} { 5} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]} {node_list[6]} {node_list[7]}\n')
				if len(node_list)==20:
					fid.write(f'{element_id} {17} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]} {node_list[6]} {node_list[7]} {node_list[8]} {node_list[11]} {node_list[12]} {node_list[9]} {node_list[13]} {node_list[10]} {node_list[14]} {node_list[15]} {node_list[16]} {node_list[19]} {node_list[17]} {node_list[18]}\n')

			wedge_list = cubit.get_block_wedges(block_id)
			for wedge_id in wedge_list:
				element_id += 1
				node_list = cubit.get_expanded_connectivity("wedge", wedge_id)
				if len(node_list)==6:
					fid.write(f'{element_id} { 6} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]}\n')
				if len(node_list)==15:
					fid.write(f'{element_id} {18} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]} {node_list[6]} {node_list[8]} {node_list[9]} {node_list[7]} {node_list[10]} {node_list[11]} {node_list[12]} {node_list[14]} {node_list[13]}\n')

			pyramid_list = cubit.get_block_pyramids(block_id)
			for pyramid_id in pyramid_list:
				element_id += 1
				node_list = cubit.get_expanded_connectivity("pyramid", pyramid_id)
				if len(node_list)==6:
					fid.write(f'{element_id} { 7} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]}\n')
				if len(node_list)==13:
					fid.write(f'{element_id} {19} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]} {node_list[8]} {node_list[9]} {node_list[6]} {node_list[10]} {node_list[7]} {node_list[11]} {node_list[12]} \n')

			tri_list = cubit.get_block_tris(block_id)
			for tri_id in tri_list:
				element_id += 1
				node_list = cubit.get_expanded_connectivity("tri", tri_id)
				if len(node_list)==3:
					fid.write(f'{element_id} { 2} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]}\n')
				if len(node_list)==6:
					fid.write(f'{element_id} { 9} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]}\n')
				if len(node_list)==7:
					fid.write(f'{element_id} {42} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]} {node_list[6]}\n')

			quad_list = cubit.get_block_faces(block_id)
			for quad_id in quad_list:
				element_id += 1
				node_list = cubit.get_expanded_connectivity("quad", quad_id)
				if len(node_list)==4:
					fid.write(f'{element_id} { 3} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]}\n')
				if len(node_list)==8:
					fid.write(f'{element_id} {16} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]} {node_list[6]} {node_list[7]}\n')
				if len(node_list)==9:
					fid.write(f'{element_id} {10} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]} {node_list[6]} {node_list[7]} {node_list[8]}\n')

			edge_list = cubit.get_block_edges(block_id)
			for edge_id in edge_list:
				element_id += 1
				node_list = cubit.get_expanded_connectivity("edge", edge_id)
				if len(node_list)==2:
					fid.write(f'{element_id} {1} {2} {block_id} {block_id} {node_list[0]} {node_list[1]}\n')
				if len(node_list)==3:
					fid.write(f'{element_id} {8} {2} {block_id} {block_id} {node_list[0]} {node_list[1]} {node_list[2]}\n')

			node_list = cubit.get_block_nodes(block_id)
			for node_id in node_list:
				element_id += 1
				fid.write(f'{element_id} {15} {2} {block_id} {block_id} {node_id}\n')

		fid.write('$EndElements\n')
		fid.close()
	return cubit

########################################################################
###	Nastran file
########################################################################

def export_Nastran(cubit, FileName, DIM="3D", PYRAM=True):

	import datetime
	formatted_date_time = datetime.datetime.now().strftime("%d-%b-%y at %H:%M:%S")
	fid = open(FileName,'w',encoding='UTF-8')
	fid.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
	fid.write("$\n")
	fid.write("$                         CUBIT NX Nastran Translator\n")
	fid.write("$\n")
	fid.write(f"$            File: {FileName}\n")
	fid.write(f"$      Time Stamp: {formatted_date_time}\n")
	fid.write("$\n")
	fid.write("$\n")
	fid.write("$                        PLEASE CHECK YOUR MODEL FOR UNITS CONSISTENCY.\n")
	fid.write("$\n")
	fid.write("$       It should be noted that load ID's from CUBIT may NOT correspond to Nastran SID's\n")
	fid.write("$ The SID's for the load and restraint sets start at one and increment by one:i.e.,1,2,3,4...\n")
	fid.write("$\n")
	fid.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
	fid.write("$\n")
	fid.write("$\n")
	fid.write("$ -------------------------\n")
	fid.write("$ Executive Control Section\n")
	fid.write("$ -------------------------\n")
	fid.write("$\n")
	fid.write("SOL 101\n")
	fid.write("CEND\n")
	fid.write("$\n")
	fid.write("$\n")
	fid.write("$ --------------------\n")
	fid.write("$ Case Control Section\n")
	fid.write("$ --------------------\n")
	fid.write("$\n")
	fid.write("ECHO = SORT\n")
	fid.write("$\n")
	fid.write("$\n")
	fid.write("$ Name: Initial\n")
	fid.write("$\n")
	fid.write("$\n")
	fid.write("$ Name: Default Set\n")
	fid.write("$\n")
	fid.write("SUBCASE = 1\n")
	fid.write("$\n")
	fid.write("LABEL = Default Set\n")
	fid.write("$\n")
	fid.write("$ -----------------\n")
	fid.write("$ Bulk Data Section\n")
	fid.write("$ -----------------\n")
	fid.write("$\n")
	fid.write("BEGIN BULK\n")
	fid.write("$\n")
	fid.write("$ Params\n")
	fid.write("$\n")
	fid.write("$\n")
	fid.write("$ Node cards\n")
	fid.write("$\n")

	node_list = set()
	for block_id in cubit.get_block_id_list():
		elem_types = ["hex", "tet", "wedge", "pyramid", "tri", "face", "edge", "node"]
		for elem_type in elem_types:
			if elem_type == "hex":
				func = getattr(cubit, f"get_block_{elem_type}es")
			else:
				func = getattr(cubit, f"get_block_{elem_type}s")
			for element_id in func(block_id):
				node_ids = cubit.get_connectivity(elem_type, element_id)
				node_list.update(node_ids)
	for node_id in node_list:
		coord = cubit.get_nodal_coordinates(node_id)
		if DIM == "3D":
			fid.write(f"GRID*   {node_id:>16}{0:>16}{coord[0]:>16.5f}{coord[1]:>16.5f}\n*       {coord[2]:>16.5f}\n")
		else:
			fid.write(f"GRID*   {node_id:>16}{0:>16}{coord[0]:>16.5f}{coord[1]:>16.5f}\n*       {0}\n")

	element_id = 0
	fid.write("$\n")
	fid.write("$ Element cards\n")
	fid.write("$\n")
	for block_id in cubit.get_block_id_list():
		name = cubit.get_exodus_entity_name("block",block_id)
		fid.write("$\n")
		fid.write(f"$ Name: {name}\n")
		fid.write("$\n")
		tet_list = cubit.get_block_tets(block_id)

		if DIM=="3D":
			for tet_id in tet_list:
				node_list = cubit.get_connectivity('tet',tet_id)
				element_id += 1
				fid.write(f"CTETRA  {element_id:>8}{block_id:>8}{node_list[0]:>8}{node_list[1]:>8}{node_list[2]:>8}{node_list[3]:>8}\n")
			hex_list = cubit.get_block_hexes(block_id)
			for hex_id in hex_list:
				node_list = cubit.get_connectivity('hex',hex_id)
				element_id += 1
				fid.write(f"CHEXA   {element_id:>8}{block_id:>8}{node_list[0]:>8}{node_list[1]:>8}{node_list[2]:>8}{node_list[3]:>8}{node_list[4]:>8}{node_list[5]:>8}+\n+       {node_list[6]:>8}{node_list[7]:>8}\n")
			wedge_list = cubit.get_block_wedges(block_id)
			for wedge_id in wedge_list:
				node_list = cubit.get_connectivity('wedge',wedge_id)
				element_id += 1
				fid.write(f"CPENTA  {element_id:>8}{block_id:>8}{node_list[0]:>8}{node_list[1]:>8}{node_list[2]:>8}{node_list[3]:>8}{node_list[4]:>8}{node_list[5]:>8}\n")
			pyramid_list = cubit.get_block_pyramids(block_id)
			for pyramid_id in pyramid_list:
				node_list = cubit.get_connectivity('pyramid',pyramid_id)
				if PYRAM:
					element_id += 1
					fid.write(f"CPYRAM  {element_id:>8}{block_id:>8}{node_list[0]:>8}{node_list[1]:>8}{node_list[2]:>8}{node_list[3]:>8}{node_list[4]:>8}\n")
				else:
					element_id += 1
					fid.write(f"CHEXA   {element_id:>8}{block_id:>8}{node_list[0]:>8}{node_list[1]:>8}{node_list[2]:>8}{node_list[3]:>8}{node_list[4]:>8}{node_list[4]:>8}+\n+       {node_list[4]:>8}{node_list[4]:>8}\n")

		tri_list = cubit.get_block_tris(block_id)
		for tri_id in tri_list:
			node_list = cubit.get_connectivity('tri',tri_id)
			element_id += 1
			if DIM=="3D":
				fid.write(f"CTRIA3  {element_id:<8}{block_id:<8}{node_list[0]:<8}{node_list[1]:<8}{node_list[2]:<8}\n")
			else:
				surface_id = int(cubit.get_geometry_owner("tri", tri_id).split()[1])
				normal = cubit.get_surface_normal(surface_id)
				if normal[2] > 0:
					fid.write(f"CTRIA3  {element_id:<8}{block_id:<8}{node_list[0]:<8}{node_list[1]:<8}{node_list[2]:<8}\n")
				else:
					fid.write(f"CTRIA3  {element_id:<8}{block_id:<8}{node_list[0]:<8}{node_list[2]:<8}{node_list[1]:<8}\n")
		quad_list = cubit.get_block_faces(block_id)
		for quad_id in quad_list:
			node_list = cubit.get_connectivity('quad',quad_id)
			element_id += 1
			if DIM=="3D":
				fid.write(f"CQUAD4  {element_id:<8}{block_id:<8}{node_list[0]:<8}{node_list[1]:<8}{node_list[2]:<8}{node_list[3]:<8}\n")
			else:
				surface_id = int(cubit.get_geometry_owner("quad", quad_id).split()[1])
				normal = cubit.get_surface_normal(surface_id)
				node_list = cubit.get_connectivity('quad',quad_id)
				if normal[2] > 0:
					fid.write(f"CQUAD4  {element_id:<8}{block_id:<8}{node_list[0]:<8}{node_list[1]:<8}{node_list[2]:<8}{node_list[3]:<8}\n")
				else:
					fid.write(f"CQUAD4  {element_id:<8}{block_id:<8}{node_list[0]:<8}{node_list[3]:<8}{node_list[2]:<8}{node_list[1]:<1}\n")
		edge_list = cubit.get_block_edges(block_id)
		for edge_id in edge_list:
			element_id += 1
			node_list = cubit.get_connectivity('edge', edge_id)
			fid.write(f"CROD    {element_id:<8}{block_id:<8}{node_list[0]:<8}{node_list[1]:<8}\n")
		node_list = cubit.get_block_nodes(block_id)
		for node_id in node_list:
			element_id += 1
			fid.write(f"CMASS   {element_id:<8}{block_id:<8}{node_id:<8}\n")
	fid.write("$\n")
	fid.write("$ Property cards\n")
	fid.write("$\n")

	for block_id in cubit.get_block_id_list():
		name = cubit.get_exodus_entity_name("block",block_id)
		fid.write("$\n")
		fid.write(f"$ Name: {name}\n")
		if len(cubit.get_block_nodes(block_id)) > 0:
			fid.write(f"PMASS    {block_id:< 8}{block_id:< 8}\n")
		elif len(cubit.get_block_edges(block_id)) > 0:
			fid.write(f"PROD     {block_id:< 8}{block_id:< 8}\n")
		elif len(cubit.get_block_tris(block_id)) + len(cubit.get_block_faces(block_id))> 0:
			fid.write(f"PSHELL   {block_id:< 8}{block_id:< 8}\n")
		else:
			fid.write(f"PSOLID   {block_id:< 8}{block_id:< 8}\n")
		fid.write("$\n")

	fid.write("ENDDATA\n")
	fid.close()
	return cubit

########################################################################
###	ELF meg file
########################################################################

def export_meg(cubit, FileName, DIM='T', MGR2=[]):

	fid = open(FileName,'w',encoding='UTF-8')
	fid.write("BOOK  MEP  3.50\n")
	fid.write("* ELF/MESH VERSION 7.3.0\n")
	fid.write("* SOLVER = ELF/MAGIC\n")
	fid.write("MGSC 0.001\n")
	fid.write("* NODE\n")

	node_list = set()
	for block_id in cubit.get_block_id_list():
		elem_types = ["hex", "tet", "wedge", "pyramid", "tri", "face", "edge"]
		for elem_type in elem_types:
			if elem_type == "hex":
				func = getattr(cubit, f"get_block_{elem_type}es")
			else:
				func = getattr(cubit, f"get_block_{elem_type}s")
			for element_id in func(block_id):
				node_ids = cubit.get_connectivity(elem_type, element_id)
				node_list.update(node_ids)
	for node_id in node_list:
		coord = cubit.get_nodal_coordinates(node_id)
		if DIM=='T':
			fid.write(f"MGR1 {node_id} 0 {coord[0]} {coord[1]} {coord[2]}\n")
		if DIM=='K':
			fid.write(f"MGR1 {node_id} 0 {coord[0]} {coord[1]} {0}\n")
		if DIM=='R':
			fid.write(f"MGR1 {node_id} 0 {coord[0]} {0} {coord[2]}\n")

	element_id = 0
	fid.write("* ELEMENT K\n")
	for block_id in cubit.get_block_id_list():
		name = cubit.get_exodus_entity_name("block",block_id)

		if DIM=='T':
			tet_list = cubit.get_block_tets(block_id)
			for tet_id in tet_list:
				node_list = cubit.get_connectivity('tet',tet_id)
				element_id += 1
				fid.write(f"{name[0:4]}{DIM} {element_id} 0 {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]}\n")

			hex_list = cubit.get_block_hexes(block_id)
			for hex_id in hex_list:
				node_list = cubit.get_connectivity('hex',hex_id)
				element_id += 1
				fid.write(f"{name[0:4]}{DIM} {element_id} 0 {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]} {node_list[6]} {node_list[7]}\n")

			wedge_list = cubit.get_block_wedges(block_id)
			for wedge_id in wedge_list:
				node_list = cubit.get_connectivity('wedge',wedge_id)
				element_id += 1
				fid.write(f"{name[0:4]}{DIM} {element_id} 0 {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[5]}\n")

			pyramid_list = cubit.get_block_pyramids(block_id)
			for pyramid_id in pyramid_list:
				node_list = cubit.get_connectivity('pyramid',pyramid_id)
				element_id += 1
				fid.write(f"{name[0:4]}{DIM} {element_id} 0 {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]} {node_list[4]} {node_list[4]} {node_list[4]} {node_list[4]}\n")

		tri_list = cubit.get_block_tris(block_id)
		for tri_id in tri_list:
			node_list = cubit.get_connectivity('tri',tri_id)
			element_id += 1
			fid.write(f"{name[0:4]}{DIM} {element_id} 0 {block_id} {node_list[0]} {node_list[1]} {node_list[2]}\n")

		quad_list = cubit.get_block_faces(block_id)
		for quad_id in quad_list:
			node_list = cubit.get_connectivity('quad',quad_id)
			element_id += 1
			fid.write(f"{name[0:4]}{DIM} {element_id} 0 {block_id} {node_list[0]} {node_list[1]} {node_list[2]} {node_list[3]}\n")

		edge_list = cubit.get_block_edges(block_id)
		for edge_id in edge_list:
			node_list = cubit.get_connectivity('edge',edge_id)
			element_id += 1
			fid.write(f"{name[0:4]}{DIM} {element_id} 0 {block_id} {node_list[0]} {node_list[1]}\n")

		node_list = cubit.get_block_nodes(block_id)
		for node_id in node_list:
			element_id += 1
			fid.write(f"{name[0:4]}{DIM} {element_id} 0 {block_id} {node_id}\n")

	fid.write("* NODE\n")
	for node_id in range(len(MGR2)):
		fid.write(f"MGR2 {node_id+1} 0 {MGR2[node_id][0]} {MGR2[node_id][1]} {MGR2[node_id][2]}\n")
	fid.write("BOOK  END\n")
	fid.close()
	return cubit

########################################################################
###	vtk format
########################################################################

def export_vtk(cubit, FileName, ORDER="2nd"):

	fid = open(FileName,'w')
	fid.write('# vtk DataFile Version 3.0\n')
	fid.write(f'Unstructured Grid {FileName}\n')
	fid.write('ASCII\n')
	fid.write('DATASET UNSTRUCTURED_GRID\n')
	fid.write(f'POINTS {cubit.get_node_count()} float\n')

	for node_id in range(cubit.get_node_count()+1):
		if cubit.get_node_exists(node_id):
			coord = cubit.get_nodal_coordinates(node_id)
			fid.write(f'{coord[0]} {coord[1]} {coord[2]}\n')

	hex_list = set()
	tet_list = set()
	wedge_list = set()
	pyramid_list = set()
	tri_list = set()
	quad_list = set()
	edge_list = set()
	nodes_list = set()

	for block_id in cubit.get_block_id_list():
		tet_list.update(cubit.get_block_tets(block_id))
		hex_list.update(cubit.get_block_hexes(block_id))
		wedge_list.update(cubit.get_block_wedges(block_id))
		pyramid_list.update(cubit.get_block_pyramids(block_id))
		tri_list.update(cubit.get_block_tris(block_id))
		quad_list.update(cubit.get_block_faces(block_id))
		edge_list.update(cubit.get_block_edges(block_id))
		nodes_list.update(cubit.get_block_nodes(block_id))

	if ORDER=="2nd":
		fid.write(f'CELLS {len(tet_list) + len(hex_list) + len(wedge_list) + len(pyramid_list) + len(tri_list) + len(quad_list) + len(edge_list) + len(nodes_list)} {11*len(tet_list) + 21*len(hex_list) + 16*len(wedge_list) + 14*len(pyramid_list) + 7*len(tri_list) + 9*len(quad_list) + 4*len(edge_list) + 2*len(nodes_list)}\n' )
	else:
		fid.write(f'CELLS {len(tet_list) + len(hex_list) + len(wedge_list) + len(pyramid_list) + len(tri_list) + len(quad_list) + len(edge_list) + len(nodes_list)} { 5*len(tet_list) +  9*len(hex_list) +  7*len(wedge_list) +  6*len(pyramid_list) + 4*len(tri_list) + 5*len(quad_list) + 3*len(edge_list) + 2*len(nodes_list)}\n' )

	for tet_id in tet_list:
		node_list = cubit.get_expanded_connectivity("tet", tet_id)
		if len(node_list)==4:
			fid.write(f'4 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} {node_list[3]-1}\n')
		if len(node_list)==10:
			fid.write(f'10 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} {node_list[3]-1} {node_list[4]-1} {node_list[5]-1} {node_list[6]-1} {node_list[7]-1} {node_list[8]-1} {node_list[9]-1}\n')
	for hex_id in hex_list:
		node_list = cubit.get_expanded_connectivity("hex", hex_id)
		if len(node_list)==8:
			fid.write(f'8 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} {node_list[3]-1} {node_list[4]-1} {node_list[5]-1} {node_list[6]-1} {node_list[7]-1}\n')
		if len(node_list)==20:
			fid.write(f'20 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} {node_list[3]-1} {node_list[4]-1} {node_list[5]-1} {node_list[6]-1} {node_list[7]-1} {node_list[8]-1} {node_list[9]-1} {node_list[10]-1} {node_list[11]-1} {node_list[16]-1} {node_list[17]-1} {node_list[18]-1} {node_list[19]-1} {node_list[12]-1} {node_list[13]-1} {node_list[14]-1} {node_list[15]-1}\n')
	for wedge_id in wedge_list:
		node_list = cubit.get_expanded_connectivity("wedge", wedge_id)
		if len(node_list)==6:
			fid.write(f'6 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} {node_list[3]-1} {node_list[4]-1} {node_list[5]-1} \n')
		if len(node_list)==15:
			fid.write(f'15 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} {node_list[3]-1} {node_list[4]-1} {node_list[5]-1} {node_list[6]-1} {node_list[7]-1} {node_list[8]-1} {node_list[12]-1} {node_list[13]-1} {node_list[14]-1} {node_list[9]-1} {node_list[10]-1} {node_list[11]-1} \n')

	for pyramid_id in pyramid_list:
		node_list = cubit.get_expanded_connectivity("pyramid", pyramid_id)
		if len(node_list)==5:
			fid.write(f'5 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} {node_list[3]-1} {node_list[4]-1} \n')
		if len(node_list)==13:
			fid.write(f'13 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} {node_list[3]-1} {node_list[4]-1} {node_list[5]-1} {node_list[6]-1} {node_list[7]-1} {node_list[8]-1} {node_list[9]-1} {node_list[10]-1} {node_list[11]-1} {node_list[12]-1} \n')
	for tri_id in tri_list:
		node_list = cubit.get_expanded_connectivity("tri", tri_id)
		if len(node_list)==3:
			fid.write(f'3 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} \n')
		if len(node_list)==6:
			fid.write(f'6 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} {node_list[3]-1} {node_list[4]-1} {node_list[5]-1} \n')
	for quad_id in quad_list:
		node_list = cubit.get_expanded_connectivity("quad", quad_id)
		if len(node_list)==4:
			fid.write(f'4 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} {node_list[3]-1} \n')
		if len(node_list)==8:
			fid.write(f'8 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} {node_list[3]-1} {node_list[4]-1} {node_list[5]-1} {node_list[6]-1} {node_list[7]-1}\n')
	for edge_id in edge_list:
		node_list = cubit.get_expanded_connectivity("edge", edge_id)
		if len(node_list)==2:
			fid.write(f'2 {node_list[0]-1} {node_list[1]-1} \n')
		if len(node_list)==3:
			fid.write(f'3 {node_list[0]-1} {node_list[1]-1} {node_list[2]-1} \n')
	for node_id in nodes_list:
		fid.write(f'1 {node_id-1} \n')

	fid.write(f'CELL_TYPES {len(tet_list) + len(hex_list) + len(wedge_list) + len(pyramid_list) + len(tri_list) + len(quad_list) + len(edge_list) + len(nodes_list)}\n')
	if ORDER=="2nd":
		for tet_id in tet_list:
			fid.write('24\n')
		for hex_id in hex_list:
			fid.write('25\n')
		for wedge_id in wedge_list:
			fid.write('26\n')
		for pyramid_id in pyramid_list:
			fid.write('27\n')
		for tri_id in tri_list:
			fid.write('22\n')
		for quad_id in quad_list:
			fid.write('23\n')
		for edge_id in edge_list:
			fid.write('21\n')
		for node_id in nodes_list:
			fid.write('1\n')
	else:
		for tet_id in tet_list:
			fid.write('10\n')
		for hex_id in hex_list:
			fid.write('12\n')
		for wedge_id in wedge_list:
			fid.write('13\n')
		for pyramid_id in pyramid_list:
			fid.write('14\n')
		for tri_id in tri_list:
			fid.write('5\n')
		for quad_id in quad_list:
			fid.write('9\n')
		for edge_id in edge_list:
			fid.write('3\n')
		for node_id in nodes_list:
			fid.write('1\n')
	fid.write(f'CELL_DATA {len(tet_list) + len(hex_list) + len(wedge_list) + len(pyramid_list) + len(tri_list) + len(quad_list) + len(edge_list) + len(nodes_list)}\n')
	fid.write('SCALARS scalars float\n')
	fid.write('LOOKUP_TABLE default\n')
	for tet_id in tet_list:
		fid.write('1\n')
	for hex_id in hex_list:
		fid.write('2\n')
	for wedge_id in wedge_list:
		fid.write('3\n')
	for pyramid_id in pyramid_list:
		fid.write('4\n')
	for tri_id in tri_list:
		fid.write('5\n')
	for quad_id in quad_list:
		fid.write('6\n')
	for edge_id in edge_list:
		fid.write('0\n')
	for node_id in nodes_list:
		fid.write('-1\n')
	return cubit

