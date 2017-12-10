from collections import namedtuple

from .defaultpalette import default_palette

Size = namedtuple('Size', 'x y z')
Color = namedtuple('Color', 'r g b a')
Voxel = namedtuple('Voxel', 'x y z c')
Model = namedtuple('Model', 'size voxels')
Material = namedtuple('Material', 'id type weight props')

def get_default_palette():
    return [ Color( *tuple(i.to_bytes(4,'little')) ) for i in default_palette ]

class Vox(object):

    def __init__(self, models, palette, materials):
        self.models = models
        self.default_palette = not palette
        self.palette = palette or get_default_palette()
        self.materials = materials

    def to_dense_rgba(self, model_idx=0):

        import numpy as np
        m = self.models[model_idx]
        res = np.zeros(( m.size.y, m.size.z, m.size.x, 4 ), dtype='B')

        for v in m.voxels:
            res[v.y, m.size.z-v.z-1, v.x] = self.palette[v.c]

        return res

    def __str__(self):
        return 'Vox(%s)'%(self.models)
