import arcade

arcade.open_window(600,600,"my first arcade game")

arcade.start_render()

(arcade.set_background_color(arcade.color.AERO_BLUE))

arcade.draw_rectangle_filled(300,300,50,30,arcade.color.DEEP.JUNGLE_GREEN)

arcade.run()