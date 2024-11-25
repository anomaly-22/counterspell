extends CharacterBody2D


const SPEED = 300.0
const slowDown = 20
@onready var uh = $"."



func _physics_process(delta: float) -> void:
	# Add the gravity.


	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var xDirection := Input.get_axis("ui_left", "ui_right")
	var yDirection := Input.get_axis("ui_up", "ui_down")
	if xDirection or yDirection:
		velocity.x = xDirection * SPEED
		velocity.y = yDirection * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, slowDown)
		velocity.y = move_toward(velocity.y, 0, slowDown)
		
	var force = 1000

	if uh.move_and_slide(): # true if collided
		for i in uh.get_slide_collision_count():
			var col = uh.get_slide_collision(i)
			if col.get_collider() is RigidBody2D:
				col.get_collider().apply_force(col.get_normal() * -force)

	move_and_slide()
