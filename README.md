# Image Augmentator
#### Video Demo: https://youtu.be/15jNDjeQHYs
#### Description:

Originally, I conceived the program for augmenting test images (JPEG, JFIF, and Adobe JPEG files) for a neural network.
However, in general, my final project can be used for image editing. __Works only with JPEG, JFIF, and Adobe JPEG files__.

My project is written in Python and consists of the following files:
* _project.py_: The main file of the project.
* _test_project.py_: A file for testing the project.
* _1.jpg_: An auxiliary image for testing implementation.
* _requirements.txt_: A text file containing any pip-installable libraries that my project requires.
* _README.md_: A text file that includes the project title, the URL of my video instruction, and a description of the project.

To run the project, go to the project directory using command __cd %project_directory%__ and enter the following command in the command line:
__python project.py -mode mode_parameter__

The __modes__, their __mode_parameters__ and their descriptions:

* _-file_ allows you to specify the path to a file or a directory containing files. By default, the program will process all images in the current folder.
* _-r_ allows you to rotate the image by a specified number of _degrees_ counterclockwise. If the number is negative, the rotation will be clockwise.
* _-f_ performs horizontal reflection if the parameter is _"h"_ and vertical reflection if the parameter is _"v"_.
* _-cb_ expects 4 arguments as parameters: coordinates of the top-left point _(x1, y1)_ and coordinates of the bottom-right point _(x2, y2)_. A rectangle is then constructed from these two points, cut out from the original image, and outputted.
* _-cr_ takes an integer _n_ as a parameter from 1 to 99 and randomly cuts out a rectangle of size n% from the original size of the input image, saving it as output.
* _-fltr_ takes one of the following options as a parameter:
    * __blur__ - applies a simple blur effect to the image, making it smoother by averaging the pixel values in the neighborhood.
    * __contour__ - emphasizes the contours of objects in the image, highlighting the boundaries between different regions.
    * __detail__ - enhances the fine details in the image, making subtle features more pronounced.
    * __edge_enhance__ - accentuates the edges of objects in the image, making them more distinct and visible.
    * __edge_enhance_more__ - a stronger version of __edge_enhance__, providing a more pronounced enhancement of edges.
    * __emboss__ - creates a three-dimensional relief effect, highlighting the raised and lowered areas in the image.
    * __find_edges__ - identifies and highlights the edges in the image, often resulting in a binary image with clear edge information.
    * __sharpen__ - increases the contrast along the edges in the image, making them appear sharper and more defined.
    * __smooth__ - applies a simple smoothing effect to the image, reducing noise and making transitions between colors more gradual.
    * __smooth_more__ - a stronger version of the __smooth__ filter, providing a more pronounced smoothing effect on the image.
* _-clr_ takes an integer _w_ as a parameter from 1 to 254 and adds this value to the current values of the R, G, B of the original image. Once the sum for a specific color channel exceeds 255, the channel value is reset to zero, and the remaining value of w is added to it.
* _-rgb_ divides the image into three one-channeled images R, G, and B, shuffles them randomly, and merges these channels back in a different order. It does not require a parameter.

The output is the modified image or images with generated names like:
**proc_mode1parameter1_..._modeNparameter1-...-parameterP_filename.jpg**.

