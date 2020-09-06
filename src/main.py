from PIL import Image
import os
import numpy as np
import pandas as pd
import plotly.express as px

__author__ = "Sarsiz Chauhan"

img_name="keanu"
img_path = os.path.join(os.getcwd(), 'images/{}.jpg'.format(img_name))
# img_path = os.path.join(os.getcwd(), 'images/saz copy.jpg')

im = Image.open(img_path)

width, height = im.size
im_gray = im.convert("L")

# resize the image to set dimensions
new_w = 70
wpercent = (new_w/float(im_gray.size[0]))
new_h = int((float(im_gray.size[1])*float(wpercent)))
dimensions = new_w, new_h

# im_gray.resize(dimensions, Image.ANTIALIAS)
im_gray.thumbnail(dimensions, Image.ANTIALIAS)

# brightness = 1 - np.array(im_gray)/255

# Custom plots will do later, for time being just plotting normal scatter plot
df = pd.DataFrame((np.asarray(im_gray)/255)*100).astype('int')

ndf = df.stack().reset_index().rename(columns={'level_0': 'x', 'level_1': 'y', '0': 'value'})
ndf[1] = ndf[0].apply(lambda x: (x/100))

fig = px.scatter(ndf, y=ndf['x'], x=ndf['y'], color=1, symbol=1)

fig.update_layout(
    coloraxis_showscale=False,
    showlegend=False,
    yaxis=dict(
        autorange='reversed',
        mirror=False,
        showticklabels=False,
        visible=False,
    ),
    xaxis=dict(
        showticklabels=False,
        visible=False,
    ),
    height=800,
    width=700,
)

fig.show()
fig.write_image('output/{}_plotted_symb.png'.format(img_name))
