from pygame import sprite, surface, Vector2

from ..lib import GameMetaData


class TileSprite(sprite.Sprite):
    def __init__(self,
                 image: surface.Surface,
                 position: Vector2,
                 metadata: GameMetaData,
                 collition: bool = True) -> None:
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.position = position
        self.rect = self.rect.move(position)
        self.metadata = metadata
        self.collition = collition

    def update(self, *_, **__) -> None:
        if self.rect is None:
            return
        self.position.x += self.metadata.scroll_value_x
        self.rect.x = int(self.position.x + self.metadata.shake_x)
        self.rect.y = int(self.position.y + self.metadata.shake_y)
        if self.rect.right < 0:
            self.kill()
