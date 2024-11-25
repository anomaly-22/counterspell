shader_type canvas_item;
uniform sampler2D SCREEN_TEXTURE : hint_screen_texture, filter_linear_mipmap;

void fragment(){
	vec4 bg = texture(SCREEN_TEXTURE, SCREEN_UV);
	if (bg == vec4(0.0,0.0,0.0,1.0)){
		COLOR = vec4(bg.r, bg.g, bg.b, 1.0);
	}
	else{
		COLOR = vec4(bg.r-0.3, bg.g-0.3, bg.b-0.3, 0.0);
	}

}
