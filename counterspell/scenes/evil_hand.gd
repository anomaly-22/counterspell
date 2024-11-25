extends CharacterBody2D

const SPEED = 200.0
const slowDown = 2
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _physics_process(delta: float) -> void:
		# Add the gravity.

	if Input.is_action_just_pressed("ui_up") or Input.is_action_just_pressed("ui_down") or Input.is_action_just_pressed("ui_left") or Input.is_action_just_pressed("ui_right"):	
		await get_tree().create_timer(0.5).timeout
	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
		var xDirection := Input.get_axis("ui_left", "ui_right")
		var yDirection := Input.get_axis("ui_up", "ui_down")
		if xDirection or yDirection:
			velocity.x = xDirection * SPEED * randi_range(-1.2,1.2 )
			velocity.y = yDirection * SPEED * randi_range(-1.2,1.2 )
		#else:
		#	velocity.x = move_toward(velocity.x, 0, slowDown)
		#	velocity.y = move_toward(velocity.y, 0, slowDown)
	velocity.x = move_toward(velocity.x, 0, slowDown)
	velocity.y = move_toward(velocity.y, 0, slowDown)

	move_and_slide()
