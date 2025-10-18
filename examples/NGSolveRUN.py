import os, sys
from numpy import *

from netgen.read_gmsh import ReadGmsh
#mesh = ReadGmsh('example_2nd_order.msh')
mesh = ReadGmsh('example_2nd_order_tet.msh')

from ngsolve import *
mesh = Mesh(mesh)

import netgen.gui
from ngsolve.internal import viewoptions, visoptions
visoptions.showsurfacesolution = 1
viewoptions.drawfilledtrigs = 1
viewoptions.clipping.enable = 0
viewoptions.clipping.nx = 1
viewoptions.clipping.nx = -1
Draw(mesh)

print(len(mesh.GetMaterials()))
print(mesh.GetMaterials())
print(len(mesh.GetBoundaries()))
print(mesh.GetBoundaries())
