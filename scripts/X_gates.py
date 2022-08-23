from godot import exposed, export
from godot import *
from godot.bindings import *
from godot.globals import *


@exposed
class X_gates(Spatial):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		self.get_node("X_gate").connect("body_entered",self,"_on_X_gate_body_entered")
		pass
		
	def _on_X_gate_body_entered(self,false):
		#print("qubit passes X-gate")
		# write the qiskit code below
		pass
