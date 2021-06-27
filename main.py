def on_button_released():
    global path, distance
    grid.snap(duck)
    path = scene.a_star(tiles.location_of_sprite(enemy),
         tiles.location_of_sprite(duck))
    distance = len(path) - 1
    print(distance)
    if distance <= 10:
        scene.follow_path(enemy, path)
controller.any_button.on_event(ControllerButtonEvent.RELEASED, on_button_released)

distance = 0
path: List[tiles.Location] = []
tiles.set_tilemap(tilemap("""level1"""))
duck = sprites.create(assets.image("""duck_r"""), SpriteKind.player)
controller.move_sprite(duck)
tiles.place_on_random_tile(duck, sprites.dungeon.collectible_insignia)
scene.camera_follow_sprite(duck)
enemy = sprites.create(assets.image("""cat"""), SpriteKind.enemy)
tiles.place_on_random_tile(enemy, sprites.dungeon.door_open_north)
