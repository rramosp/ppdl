import matplotlib.pyplot as plt

from skimage.transform import rescale, resize, downscale_local_mean
from skimage.io import imread

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--video_name', dest='video_name', type=str, 
                    help='the name of the video, include \\n for separating lines')

parser.add_argument('--destination_file', dest='destination_file', type=str,
                    help='file to store the generated png image')

parser.add_argument('--background_file', dest='background_file', type=str,
                    help='png file with the background')


args = parser.parse_args()

assert args.destination_file.endswith(".png"), "destination_file name must end with '.png'"
assert args.background_file.endswith(".png"), "background_file name must end with '.png'"

video_name = args.video_name.replace("\\n", "\n")

background = imread(args.background_file)
background = resize(background, (1080, 1920), anti_aliasing=True)
h,w,_ = background.shape

my_dpi=80
fig = plt.figure(figsize=(w/my_dpi, h/my_dpi), dpi=my_dpi)

plt.imshow(background)

course_name = "probabilistic programming\nfor deep learning "

t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")

for i,t in enumerate(course_name.split("\n")):
    txt = plt.text(50,200+100*i, t, ha='left', va='top', wrap=False, fontsize=60)

for i,t in enumerate(video_name.split("\n")):
    txt = plt.text(50,550+200*i, t, ha='left', va='top', wrap=False, fontsize=120)

plt.axis("off")
plt.savefig(args.destination_file, dpi=my_dpi, pad_inches=0, bbox_inches='tight')
plt.close(fig)

print (f"banner written to {args.destination_file}")
