from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches
from pptx.shapes.autoshape import Shape
from pptx.dml.color import RGBColor
from pptx.util import Pt
from pptx.enum.text import PP_ALIGN


class ArrowBase:
    def __init__(self, pos=(0, 0, 1, 1)):
        self.x = pos[0]
        self.y = pos[1]
        self.width = pos[2]
        self.height = pos[3]
