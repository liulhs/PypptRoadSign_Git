from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches
from pptx.shapes.autoshape import Shape
from pptx.dml.color import RGBColor
from pptx.util import Pt
from pptx.enum.text import PP_ALIGN
import json
import os


BLACK = RGBColor(0, 0, 0)  # 黑色
WHITE = RGBColor(255, 255, 255)  # 白色
NAVYBLUE = RGBColor(0, 63, 143)  # 预定的蓝色
ROUND_DEGREE = 0.05  # 圆角程度调整 0-1

# Get the directory of the current file (background.py)
current_directory = os.path.dirname(os.path.abspath(__file__))


class Background:
    def __init__(self, background_style='default', sign=None):
        self.style = background_style
        self.sign = sign
        self.canvas = self.sign.canvas

    def draw(self):
        if not self.sign:
            raise AssertionError("You didn't specify a canvas for the background object!")
        json_file_path = os.path.join(current_directory, 'background_style.json')
        with open(json_file_path, 'r') as file:
            background_style = json.load(file)
            if self.style not in background_style.keys():
                raise AssertionError("{} is not a designed background style!".format(self.style))
            exec(background_style[self.style])

