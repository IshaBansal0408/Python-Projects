import pyvista as pv
from pyvista import examples

plane_file = examples.planefile
plane_mesh = pv.read(plane_file)

cpos = plane_mesh.plot()
plane_plotter = pv.Plotter()

plane_plotter.add_mesh(plane_mesh)
