from PLI import Image
def images_to_pdf(filename,output):
	images=[]
	for file in filename:
		img=image.open(file)
		img=img.convert('RGG')
		images.append(img)
		images[0].save(output,save_all=True,append_images=images[1:])
images_to_pdf(['binod_mirror.png','binod.png','binod.jpg'],"output.pdf")