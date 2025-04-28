@namespace
class SpriteKind:
    HOME = SpriteKind.create()

def on_up_pressed():
    global directionX, directionY
    directionX = 0
    directionY = -1
    animation.run_image_animation(yay,
        [img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f f 2 f e f . .
                . . f f f 2 f e e 2 2 f f f . .
                . . f e 2 f f e e 2 f e e f . .
                . f f e f f e e e f e e e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . . e f f f f f f f f 4 e . .
                . . . 4 f 2 2 2 2 2 e d d 4 . .
                . . . e f f f f f f e e 4 . . .
                . . . . f f f . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e f 2 f f f 2 f 2 e f . .
                . . f f f 2 2 e e f 2 f f f . .
                . . f e e f 2 e e f f 2 e f . .
                . f f e e e f e e e f f e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f e . . .
                . . 4 d d e 2 2 2 2 2 f 4 . . .
                . . . 4 e e f f f f f f e . . .
                . . . . . . . . . f f f . . . .
                """)],
        500,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap(sprite, otherSprite):
    yay.say_text("yay", 200, True)
sprites.on_overlap(SpriteKind.player, SpriteKind.HOME, on_on_overlap)

def on_a_pressed():
    global projectile, projectile2
    if directionX == 1:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . 1 1 3 . . . . . .
                . . . . . . 1 3 . 3 3 . . . . .
                . . . . . . 1 . . . 3 2 2 3 . .
                . . . . . 1 3 . . . 2 2 1 3 3 .
                . . . . . 1 3 . 2 2 3 1 1 1 3 .
                . . 2 2 2 1 3 3 3 3 3 1 1 1 3 .
                . . 1 1 1 1 3 1 1 1 1 1 1 1 3 .
                . . 2 2 2 1 3 3 3 3 3 1 1 1 3 .
                . . . . . 1 3 . 2 2 3 1 1 1 3 .
                . . . . . 1 3 . . . 2 2 1 3 3 .
                . . . . . . 1 . . . 3 2 2 3 . .
                . . . . . . 1 3 . 3 3 . . . . .
                . . . . . . . 1 1 3 . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            yay,
            100,
            0)
    else:
        projectile2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . 3 1 1 . . . . . . .
                . . . . . 3 3 . 3 1 . . . . . .
                . . 3 2 2 3 . . . 1 . . . . . .
                . 3 3 1 2 2 . . . 3 1 . . . . .
                . 3 1 1 1 3 2 2 . 3 1 . . . . .
                . 3 1 1 1 3 3 3 3 3 1 2 2 2 . .
                . 3 1 1 1 1 1 1 1 3 1 1 1 1 . .
                . 3 1 1 1 3 3 3 3 3 1 2 2 2 . .
                . 3 1 1 1 3 2 2 . 3 1 . . . . .
                . 3 3 1 2 2 . . . 3 1 . . . . .
                . . 3 2 2 3 . . . 1 . . . . . .
                . . . . . 3 3 . 3 1 . . . . . .
                . . . . . . 3 1 1 . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            yay,
            -100,
            0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    global directionX, directionY
    directionX = -1
    directionY = 0
    animation.run_image_animation(yay,
        [img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d e e e e e f . . .
                . . . f e 4 e d d 4 f . . . . .
                . . . f 2 2 e d d e f . . . . .
                . . f f 5 5 f e e f f f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """),
            img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e d d 4 . . . .
                . . . f 2 2 2 2 e d d e . . . .
                . . f f 5 5 4 4 f e e f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """)],
        500,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile(sprite2, location):
    global OpenPortal
    if info.score() < 30:
        OpenPortal = 1
        portal(OpenPortal)
    if info.score() < 30:
        game.show_long_text("sorry gentleman,you can't enter yet,you HAVE to reach 30 points.",
            DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite3, location2):
    if controller.B.is_pressed():
        game.show_long_text("hello gentleman,you can't enter the portal unless ... you have 30 points!",
            DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile2)

def on_right_pressed():
    global directionX, directionY
    directionX = 1
    directionY = 0
    animation.run_image_animation(yay,
        [img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 2 2 2 f . . .
                . . . . . e d d e 2 2 2 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e e e d d d f . . .
                . . . . . f 4 d d e 4 e f . . .
                . . . . . f e d d e 2 2 f . . .
                . . . . f f f e e f 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """),
            img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 2 2 2 f . . .
                . . . . . e d d e 2 2 2 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . 4 d d e 4 4 4 e f . . .
                . . . . e d d e 2 2 2 2 f . . .
                . . . . f e e f 4 4 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """)],
        500,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    global directionX, directionY
    directionX = 0
    directionY = 1
    animation.run_image_animation(yay,
        [img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . . f e 4 d d d d 4 e f e . .
                . . f e f 2 2 2 2 e d d 4 e . .
                . . e 4 f 2 2 2 2 e d d e . . .
                . . . . f 4 4 5 5 f e e . . . .
                . . . . f f f f f f f . . . . .
                . . . . f f f . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f e e 2 2 2 2 2 2 e f f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . e f e 4 d d d d 4 e f . . .
                . . e 4 d d e 2 2 2 2 f e f . .
                . . . e d d e 2 2 2 2 f 4 e . .
                . . . . e e f 5 5 4 4 f . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . . . . f f f . . . .
                """)],
        500,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap2(sprite4, otherSprite2):
    sprites.destroy(otherSprite2, effects.ashes, 100)
    info.change_score_by(1)
    music.play(music.melody_playable(music.magic_wand),
        music.PlaybackMode.IN_BACKGROUND)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def portal(CurrentPortal: number):
    if CurrentPortal == 0:
        tiles.set_current_tilemap(tilemap("""
            level2
            """))
        info.start_countdown(30)
    tiles.place_on_random_tile(yay, sprites.dungeon.collectible_insignia)

def on_on_overlap3(sprite5, otherSprite3):
    sprites.destroy(otherSprite3, effects.ashes, 500)
    info.change_score_by(4)
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.IN_BACKGROUND)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

def on_on_overlap4(sprite6, otherSprite4):
    sprites.destroy(otherSprite4, effects.disintegrate, 100)
    info.change_life_by(-1)
    music.play(music.melody_playable(music.wawawawaa),
        music.PlaybackMode.IN_BACKGROUND)
    tiles.place_on_random_tile(yay, sprites.dungeon.collectible_insignia)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

OpenPortal = 0
projectile2: Sprite = None
projectile: Sprite = None
directionY = 0
directionX = 0
ENEMY1: Sprite = None
chicken_nuggettt: Sprite = None
yay: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
    """))
yay = sprites.create(img("""
        ........................
        .....ffff...............
        ...fff22fff.............
        ..fff2222fff............
        .fffeeeeeefff...........
        .ffe222222eef...........
        .fe2ffffff2ef...........
        .ffffeeeeffff...........
        ffefbf44fbfeff..........
        fee41fddf14eef..........
        .ffffdddddeef...........
        fddddf444eef............
        fbbbbf2222f4e...........
        fbbbbf2222fd4...........
        .fccf45544f44...........
        ..ffffffff..............
        ....ff..ff..............
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
        """),
    SpriteKind.player)
controller.move_sprite(yay)
scene.camera_follow_sprite(yay)
tiles.place_on_random_tile(yay, sprites.dungeon.collectible_insignia)
Rumah = sprites.create(img("""
        ....................8a8aa8a8....................
        .................aaa888aa8a8aaa.................
        ..............aaa8aa8a8aa888aa8aaa..............
        ...........8aa8aa8888a8aa8a8888aa8aa8...........
        ........8888aa8aa8aa8a8aa8a8aa8aa8aa8888........
        .....aaa8aa8aa8888aa8a8aa8a8aa8888aa8aa8aaa.....
        ...aa8888aa8aa8aa8aa888aa888aa8aa8aa8aa8888aa...
        dccaa8aa8aa8888aa8aa8a8aa8a8aa8aa8888aa8aa8aaccd
        bcb888aa8aa8aa8aa8aa8a8aa8a8aa8aa8aa8aa8aa888bcb
        dbbaa8aa8888aa8aa8888a8aa8a8888aa8aa8888aa8aabbd
        dbbaa8aa8aa8aa8888aa8a8aa8a8aa8888aa8aa8aa8aabbd
        dccaa8888aa8aa8aa8aa888aa888aa8aa8aa8aa8888aaccd
        bcbaa8aa8aa8888aa8aa8a8aa8a8aa8aa8888aa8aa8aabcb
        dbb888aa8aa8aa8aa8aa8a8aa8a8aa8aa8aa8aa8aa888bbd
        dbbaa8aa8888aa8aa8aa8a8aa8a8aa8aa8aa8888aa8aabbd
        dccaa8aa8aa8aa8aa8888a8aa8a8888aa8aa8aa8aa8aaccd
        bcbaa8888aa8aa8888aa888aa888aa8888aa8aa8888aabcb
        dbbaa8aa8aa8888aa8aa8a8aa8a8aa8aa8888aa8aa8aabbd
        dbb888aa8aa8aa8aa8aa8a8aa8a8aa8aa8aa8aa8aa888bbd
        dccaa8aa8888aa8aa8aa8a8aa8a8aa8aa8aa8888aa8aaccd
        bcbaa8aa8aa8aa8aa8aa888aa888aa8aa8aa8aa8aa8aabcb
        dbbaa8888aa8aa8aa888ccbbbbcc888aa8aa8aa8888aabbd
        dbbaa8aa8aa8aa888ccbbbbbbbbbbcc888aa8aa8aa8aabbd
        dcc888aa8aa888ccbbbbbccccccbbbbbcc888aa8aa888ccd
        bcbaa8aa888ccbbbbbccbddddddbccbbbbbcc888aa8aabcb
        dbbaa8aaccbbbbbccbddddddddddddbccbbbbbccaa8aabbd
        dbbaaccbbbbcccbddddddddddddddddddbcccbbbbccaabbd
        dcccbbbbcccbdddbccbbbbbbbbbbbbccbdddbcccbbbbcccd
        ccccccccbbbbbbbcbddddddddddddddbcbbbbbbbcccccccc
        bddddddddddddbcddddddddddddddddddcbddddddddddddb
        bbcbdddddddddcbd1111111111111111dbcdddddddddbcbb
        bbbcccccccccccd1bbbbbbbbbbbbbbbb1dcccccccccccbbb
        bbbbdddddddddc11beeeeeeeeeeeeeeb11cdddddddddbbbb
        bbb8aaaaaaa8dc1be3b33b33b33b33beb1cd8aaaaaaa8bbb
        bbb888888888dc1be3b33b33b33b33beb1cd888888888bbb
        bbb833333338dcbbf3b3effffffe33bebbcd833333338bbb
        bbb83ff3ff38dcbbf3bffffffffff3bebbcd83ff3ff38bbb
        bbb83cc3cc38dcbbf3effffffffffebebbcd83cc3cc38bbb
        bbb833333338dcbbf3eeeeeeeeeeeebebbcd833333338bbb
        cbb83ff3ff38dcbbe3b33b33b33b33bebbcd83ff3ff38bbc
        cbb83cc3cc38dcbbe3b33b33b33b33bebbcd83cc3cc38bbc
        ccbbbbbbbbbbdcbbe3b33b33b33feeeebbcdbbbbbbbbbbcc
        .cbbdddddddddcbbe3b33b33b33ffffebbcdddddddddbbc.
        ..cbdbbbdbbbdcbbf3b33b33b33f33febbcdbbbdbbbdbc..
        ...cdbbbdbbbdcbbf3b33b33b33bffeebbcdbbbdbbbdc...
        ....bddddddddcbbf3b33b33b33b33bebbcddddddddb....
        .....bdbbbdddcbbf3b33b33b33b33bebbcdddbbbdb.....
        ......bcccbbbcbbe3b33b33b33b33bebbcbbbcccb......
        """),
    SpriteKind.HOME)
tiles.place_on_random_tile(Rumah, sprites.dungeon.collectible_insignia)
info.set_life(3)
for value in tiles.get_tiles_by_type(assets.tile("""
    myTile1
    """)):
    chicken_nuggettt = sprites.create(img("""
            ..........bbbbbb........
            .......bbb444444bb......
            .....2244444ddd444b.....
            ....244444444dddd44e....
            ...244444444444ddd4be...
            ..244444444444444d44be..
            .2b444444444444444d4be..
            .2b44444444444444444bbe.
            2bbb4444444444444444bbe.
            2bbb4444444444444444bbe.
            2bb4b4444444444444444bbe
            2bb4444444444444444444be
            2bb44444444444444444444e
            2bbb444bbb4444444444444e
            22bbb444bb4bb444444444be
            .2bbbbb44bbbb44444444bbe
            .22bbbbbbbb44bbb444444bb
            ..eeebbbbbbb44bbb444444b
            ...eeeeebbbbbbbb44b4444b
            .....eeeeee222bb44bbb4bb
            .......eeeee222bb44bbbbe
            ............e222bbbbbbbe
            ..............ee2bbbbeeb
            .................eeeeecd
            """),
        SpriteKind.food)
    tiles.place_on_tile(chicken_nuggettt, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
        """))
    animation.run_movement_animation(chicken_nuggettt,
        animation.animation_presets(animation.bobbing),
        1000,
        True)
for value2 in tiles.get_tiles_by_type(assets.tile("""
    myTile2
    """)):
    ENEMY1 = sprites.create(img("""
            7777777ccc777777777777777777
            777777cb5c777777777777777777
            7777ccc55ccc7777777777777777
            77ccbc5555cccc77777777777777
            7cbb5b5555b5bbc7777777777777
            7cb55bb55bb55bc7777777777777
            77f555bbbb555c77777777777777
            77ff55555555ff77777777777777
            77fffbfeefbfff77777777777777
            77fff1fbbf1fff77777777777777
            777ffbbbbbbff777777777777777
            777eefeeeefee777777777777777
            77ebcb5bb5bfbe77777777777777
            77eef555555fee77777777777777
            7777cb5555bc7777777777777777
            77777ffffff77777777777777777
            7777777777777777777777777777
            7777777777777777777777777777
            7777777777777777777777777777
            7777777777777777777777777777
            7777777777777777777777777777
            7777777777777777777777777777
            7777777777777777777777777777
            7777777777777777777777777777
            7777777777777777777777777777
            7777777777777777777777777777
            7777777777777777777777777777
            7777777777777777777777777777
            """),
        SpriteKind.enemy)
    tiles.place_on_tile(ENEMY1, value2)
    tiles.set_tile_at(value2, assets.tile("""
        transparency16
        """))
    animation.run_movement_animation(ENEMY1,
        animation.animation_presets(animation.bobbing),
        1000,
        True)
directionX = 1
directionY = 1