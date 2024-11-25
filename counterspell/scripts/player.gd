extends CharacterBody2D
@export var sprite : Sprite2D

const SPEED = 450.0
const slowDown = 20



func _physics_process(delta: float) -> void:
	var xDirection := Input.get_axis("ui_left", "ui_right")
	var yDirection := Input.get_axis("ui_up", "ui_down")
	if xDirection or yDirection:
		velocity.x = xDirection * SPEED
		velocity.y = yDirection * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, slowDown)
		velocity.y = move_toward(velocity.y, 0, slowDown)

		

	move_and_slide()
