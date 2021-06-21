from pydantic import BaseConfig


class sizeConfig(BaseConfig):
    width: int = 1080
    height: int = 1080
    nX: int = 50
    nY: int = 50
    xSize = width / nX
    ySize = height / nY


class colorConfig(BaseConfig):
    bg: tuple = (10, 10, 10)
    live: tuple = (255, 255, 255)
    dead: tuple = (55, 128, 128)
