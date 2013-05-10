import SimpleCV

# start local webcam
camera = SimpleCV.Camera()

while 1:
	# load an image from webcam
	image = camera.getImage()
	
	# show the  resulting image.
	image.show()
