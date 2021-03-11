import json

# Data to be written
dictionary = {
    "default":
"""left = Inches(0)
top = Inches(0)
width = Inches(self.sign.width)
height = Inches(self.sign.height)
shape = self.canvas.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
)
shape.fill.solid()  # 实心填充
shape.fill.fore_color.rgb = NAVYBLUE  # 填充颜色
shape.line.fill.background()  # 边缘线无填充
shape.adjustments[0] = ROUND_DEGREE  # 圆角程度调整 0-1
shape.shadow.inherit = False  # 取消形状阴影

left = Inches(0.15)
top = Inches(0.15)
width = Inches(self.sign.width-0.3)
height = Inches(self.sign.height-0.3)
shape = self.canvas.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
)
shape.fill.background()  # 无填充
shape.line.fill.solid()  # 边缘线填充
shape.line.fill.fore_color.rgb = WHITE
shape.line.width = Pt(8)  # 线的粗细
shape.adjustments[0] = ROUND_DEGREE  # 圆角程度调整 0-1
shape.shadow.inherit = False
"""
}

# Serializing json

json_object = json.dumps(dictionary, indent=4)
with open('background_style.json', 'w') as outfile:
    json.dump(dictionary, outfile)

# with open('background_style.json', 'r') as file:
#     background_style = json.load(file)
#     print(background_style.keys())