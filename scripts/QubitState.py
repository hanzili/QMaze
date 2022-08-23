from godot import exposed, export
from godot import *
from qiskit import *
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_bloch_multivector
import random


@exposed
class QubitState(Spatial):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')
	hit1 = -1
	h_time = -1
	x_time = 0
	z_time = 0
	y_time = 0
	circ = QuantumCircuit(1)
	target_circ = QuantumCircuit(1)
	target_outputstate = None

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		self.get_node("../H_gates/H_gate").connect("body_entered",self,"_on_H_gate_body_entered")
		self.get_node("../noise").connect("body_entered",self,"_on_noise_body_entered")
		target_circ = QubitState.target_circ
		for i in range(2):
			a = random.randint(1, 4)
			if a==1:
				target_circ.y(0)
			elif a==2:
				target_circ.x(0)
			elif a==3:
				target_circ.z(0)
			else:
				target_circ.h(0)
		target_circ.measure_all()
		#target_circ.save_statevector()
		#sim = Aer.get_backend('statevector_simulator')
		#qobj = assemble(target_circ)
		#state = sim.run(qobj).result().get_statevector()
		#plot_bloch_multivector(state)
		backend = Aer.get_backend('statevector_simulator')
		job = execute(target_circ, backend)
		result = job.result()
		QubitState.target_outputstate = result.get_statevector(target_circ)
		#print(target_outputstate)
		#print(result.get_statevector(target_circ))
		print(QubitState.target_circ)
		self.get_node("../Control/Label3").text = str(QubitState.target_outputstate)
		pass
		
	def _on_noise_body_entered(body,false):
		if QubitState.hit1 > 0:			
			body.get_tree().change_scene("res://Lose.tscn")
		QubitState.hit1 += 1
		
	def _on_X_gate_body_entered(self, false):
		if QubitState.h_time > 0:
			circ = QubitState.circ
			print("pass X")
			circ.x(0)
		QubitState.h_time+=1

	def _on_Y_gate_body_entered(self, false):
		if QubitState.y_time > 0:
			circ = QubitState.circ
			print("pass Y")
			circ.y(0)
		QubitState.y_time+=1
		
	def _on_H_gate_body_entered(self, false):
		if QubitState.h_time > 0:
			circ = QubitState.circ
			print("pass H")
			circ.h(0)
		QubitState.h_time+=1
		
	def _on_Z_gate_body_entered(self, false):
		if QubitState.z_time > 0:
			circ = QubitState.circ
			print("pass Z")
			circ.z(0)
		QubitState.z_time+=1
	
	def _on_Button_pressed(self):
		circ = QubitState.circ
		circ.measure_all()
		backend = Aer.get_backend('statevector_simulator')
		job = execute(circ, backend)
		result = job.result()
		outputstate = result.get_statevector(circ)
		print(circ)
		self.get_node("../Control/Label2").text = str(outputstate)
		print(QubitState.target_outputstate[0])
		print(QubitState.target_outputstate[1])
		print(outputstate[0])
		print(outputstate[1])
		if outputstate[0] == QubitState.target_outputstate[0] and outputstate[1] == QubitState.target_outputstate[1]:
			print("win!")
			self.get_tree().change_scene("res://Win.tscn")
	
		
