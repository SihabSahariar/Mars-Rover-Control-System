# Paneroma Image From Static Image

# Idea : 
  1. 60 deg ->   1.jpg
  2. 75 deg  ->  2.jpg
  3. 90 deg  ->  3.jpg
  4. 105 deg  -> 4.jpg
  5. 120 deg ->  5.jpg
 ```
  1:3 ratio = 60, 90 , 120 degree (3 image) [height, height*3= width]
 ```

# Algo:
  1. Move  from 60 to 120 degree gradually.
  2. After every 15 degree of rotation in the range capture n.jpg pic
  3. Call Panaroma Function
  4. Save the output.jpg file
  5. Show it in the GUI



# pseudocode :
  ```
  def servo_rotate_shot() // move each angle and take the shot save into jpg
  def panaroma_output() // stich those images and output a .jpg
  def show() // load the output on the GUI
  ```

# Resources:
  1. https://www.pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python/
  2. https://github.com/ndvinh98/Panorama
  3. https://www.mathworks.com/help/vision/examples/feature-based-panoramic-image-stitching.html
  4. https://www.pyimagesearch.com/2016/01/11/opencv-panorama-stitching/
  5. http://ppwwyyxx.com/2016/How-to-Write-a-Panorama-Stitcher/
  6. https://github.com/avinashk442/Panoramic-Image-Stitching-using-invariant-features
  7. https://github.com/kushalvyas/Python-Multiple-Image-Stitching
  8. https://github.com/WillBrennan/ImageStitching
