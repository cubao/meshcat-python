from .geometry import Geometry, Object, Mesh, MeshPhongMaterial, OrthographicCamera, PerspectiveCamera, PointsMaterial, Points, TextTexture
from .path import Path


class SetObject:
    __slots__ = ["object", "path"]
    def __init__(self, geometry_or_object, material=None, path=None):
        if isinstance(geometry_or_object, Object):
            if material is not None:
                raise(ValueError("Please supply either an Object OR a Geometry and a Material"))
            self.object = geometry_or_object
        elif isinstance(geometry_or_object, (OrthographicCamera, PerspectiveCamera)):
            self.object = geometry_or_object
        else:
            if material is None:
                material = MeshPhongMaterial()
            if isinstance(material, PointsMaterial):
                self.object = Points(geometry_or_object, material)
            else:
                self.object = Mesh(geometry_or_object, material)
        if path is not None:
            self.path = path
        else:
            self.path = Path()

    def lower(self):
        return {
            u"type": u"set_object",
            u"object": self.object.lower(),
            u"path": self.path.lower()
        }


class SetTransform:
    __slots__ = ["matrix", "path"]
    def __init__(self, matrix, path):
        self.matrix = matrix
        self.path = path

    def lower(self):
        return {
            u"type": u"set_transform",
            u"path": self.path.lower(),
            u"matrix": list(self.matrix.T.flatten())
        }

class CaptureImage:

    def lower(self):
        return {
            u"type": u"capture_image"
        }


class Delete:
    __slots__ = ["path"]
    def __init__(self, path):
        self.path = path

    def lower(self):
        return {
            u"type": u"delete",
            u"path": self.path.lower()
        }

class SetProperty:
    __slots__ = ["path", "key", "value"]
    def __init__(self, key, value, path):
        self.key = key
        self.value = value
        self.path = path

    def lower(self):
        return {
            u"type": u"set_property",
            u"path": self.path.lower(),
            u"property": self.key.lower(),
            u"value": self.value
        }

class SetAnimation:
    __slots__ = ["animation", "play", "repetitions"]

    def __init__(self, animation, play=True, repetitions=1):
        self.animation = animation
        self.play = play
        self.repetitions = repetitions

    def lower(self):
        return {
            u"type": u"set_animation",
            u"animations": self.animation.lower(),
            u"options": {
                u"play": self.play,
                u"repetitions": self.repetitions
            },
            u"path": ""
        }
