import SimpleCV
from SimpleCV import Image, Color, Display

# start local webcam
camera = SimpleCV.Camera()

while 1:
	# load an image from webcam
	image = camera.getImage()

	# use a keypoint detector to find areas of interest
	feats = image.findKeypoints()

	# draw the list of keypoints
        feats.draw(color=Color.RED)

        # apply the stuff we found to the image.
        output = image.applyLayers()

        # save the results
        output.save("test.png")
	
	# show the  resulting image.
	image.show()
