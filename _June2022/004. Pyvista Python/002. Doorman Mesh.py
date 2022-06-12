import pyvista as pv
from pyvista import examples

mesh = examples.download_doorman()
mesh.plot(cpos="xy")
