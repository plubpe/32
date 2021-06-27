controller.anyButton.onEvent(ControllerButtonEvent.Released, function on_button_released() {
    
    grid.snap(duck)
    path = scene.aStar(tiles.locationOfSprite(enemy), tiles.locationOfSprite(duck))
    distance = path.length - 1
    console.log(distance)
    if (distance <= 10) {
        scene.followPath(enemy, path)
    }
    
})
let distance = 0
let path : tiles.Location[] = []
tiles.setTilemap(tilemap`level1`)
let duck = sprites.create(assets.image`duck_r`, SpriteKind.Player)
controller.moveSprite(duck)
tiles.placeOnRandomTile(duck, sprites.dungeon.collectibleInsignia)
scene.cameraFollowSprite(duck)
let enemy = sprites.create(assets.image`cat`, SpriteKind.Enemy)
tiles.placeOnRandomTile(enemy, sprites.dungeon.doorOpenNorth)
