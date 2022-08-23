extends KinematicBody

var velocity = Vector3(0,0,0)
const SPEED = 5
const ROTSPEED = 5

func _ready():
	pass

func _physics_process(delta):
		if Input.is_action_pressed("ui_right") and Input.is_action_pressed("ui_left"):
			velocity.x = 0
		elif Input.is_action_pressed("ui_right"):
			velocity.x = SPEED
			$MeshInstance.rotate_z(deg2rad(-ROTSPEED))
		elif Input.is_action_pressed("ui_left"):
			velocity.x = -SPEED
			$MeshInstance.rotate_z(deg2rad(ROTSPEED))
		else:
			velocity.x = lerp(velocity.x,0,0.01)
				
		if Input.is_action_pressed("ui_up") and Input.is_action_pressed("ui_down"):
			velocity.z = 0
		elif Input.is_action_pressed("ui_up"):
			velocity.z = -SPEED
			$MeshInstance.rotate_z(deg2rad(-ROTSPEED))
		elif Input.is_action_pressed("ui_down"):
			velocity.z = SPEED
			$MeshInstance.rotate_z(deg2rad(ROTSPEED))
		else:
			velocity.z = lerp(velocity.z,0,0.01)
		move_and_slide(velocity)
			


func _on_noise_body_entered(body):
	pass # Replace with function body.
