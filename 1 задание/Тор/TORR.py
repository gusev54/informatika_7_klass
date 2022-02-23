import gmsh
import math
import os
import sys

gmsh.initialize()
file = "C:\\Users\\gusev\\Downloads\\tor.STL"
path = os.path.dirname(os.path.abspath(__file__))
gmsh.merge(os.path.join(path, file))

angle = 50
forceParametrizablePatches = True
includeBoundary = True
curveAngle = 180

gmsh.model.mesh.classifySurfaces(angle * math.pi / 180., includeBoundary,
                                 forceParametrizablePatches,
                                 curveAngle * math.pi / 180.)

gmsh.model.mesh.createGeometry()

s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

f = gmsh.model.mesh.field.add("MathEval")


gmsh.model.mesh.field.setString(f, "F", "0.5")
gmsh.model.mesh.field.setAsBackgroundMesh(f)

gmsh.model.mesh.generate(3)
gmsh.write('t13.msh')

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()