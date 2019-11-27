# face_predictor
Basic face detection


Hit the problem endpoint, grab the image_url value. The link expires in 5 seconds.

In the linked image you'll see a 8x8 grid of tiles, some of which contain faces.

Your task is straightforward: detect which tiles have a face in them. The result should be a list of two-element lists indictating which tiles successfuly went through face detection.

Use zero based indexing for row and column. So in a 8x8 tile grid, top left image is [0, 0], bottom right will be [7, 7].

For example, if there's only one face-containing tile and it's in the second row, fifth column, the answer would be [[1, 4]].

https://hackattic.com/challenges/basic_face_detection
