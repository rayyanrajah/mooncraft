from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader
from terrain import terrain_dict

app = Ursina()

# textures and soundtrack
white_cube_texture = 'white_cube'
vertical_grad_texture = 'vertical_gradient'
moon_texture = load_texture('assets/moonrock.png')
sky_texture = load_texture('assets/space.png')
minecraft_soundtrack = Audio('minecraft_soundtrack.mp3', loop=True)

block_pick = 1


# for each number key pressed (from 1-6 inclusive),
# there is a different texture and/or colour
def update():
    global block_pick

    for i in range(1, 7):
        if held_keys[f'{i}']: block_pick = i

    # space constantly rotates to give illusion that the moon is moving
    sky.rotate((time.dt, time.dt, time.dt))


# class for block
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=moon_texture, color=color.color(0, 0, random.uniform(0.9, 1.0))):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture=texture,
            color=color,
            shader=basic_lighting_shader
        )

    def input(self, key):
        if self.hovered:
            # place block
            if key == 'left mouse down':
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal, texture=moon_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=white_cube_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=white_cube_texture,
                                                  color=color.light_gray)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=white_cube_texture,
                                                  color=color.dark_gray)
                if block_pick == 5: voxel = Voxel(position=self.position + mouse.normal, texture=white_cube_texture,
                                                  color=color.black)
                if block_pick == 6: voxel = Voxel(position=self.position + mouse.normal, texture=vertical_grad_texture,
                                                  color=color.white)
            # destroy block
            if key == 'right mouse down':
                destroy(self)


# generate initial moon terrain
for z in range(-16, 16):
    for x in range(-16, 16):
        voxel = Voxel(position=(x, 0, z))

        if terrain_dict[(x,z)][0] > 80:
            voxel = Voxel(position=(x, 1, z))
        if terrain_dict[(x,z)][0] > 120:
            voxel = Voxel(position=(x, 2, z))


light = PointLight(x=100,z=300,y=100)
sky = Sky(texture=sky_texture)
player = FirstPersonController(y=20)
app.run()