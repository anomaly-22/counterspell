extends Node2D
@onready var dish = $"."
@export var dishDirt : Sprite2D
@export var character : CharacterBody2D
var inside = false
@onready var particles = $CPUParticles2D
@onready var globals = $"/root/Globals"

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	particles.emitting = false
	


func _process(delta: float) -> void:
	
	if inside == true:
		dishDirt.self_modulate.a -= abs(character.velocity.x/45000)
		particles.emitting = true
		


func _on_detection_body_entered(body: Node2D) -> void:
	particles.visible = true
	inside = true
	print("isndie")


func _on_detection_body_exited(body: Node2D) -> void:
	particles.visible = true
	inside = false
	print("getout")
