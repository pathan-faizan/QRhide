from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Steganography')
subparser = parser.add_subparsers(dest='command')

merge = subparser.add_parser('unmerge')
merge.add_argument('--image', required=True, help='Image path')
    # merge.add_argument('--image2', required=True, help='Image2 path')
merge.add_argument('--output', required=True, help='Output path')
args = parser.parse_args()

im = Image.open(args.image)
pix = im.load()

for x in range(im.size[0]):
	for y in range(im.size[1]):
		if sum(pix[x,y])%2:
			pix[x,y] = (255, 255, 255)
		else:
			pix[x,y] = (0, 0, 0)

im.save(args.output)
