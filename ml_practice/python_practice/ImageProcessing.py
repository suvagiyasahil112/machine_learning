# You are working on a simple image processing task. The image is represented as a 2D grayscale matrix,
#  where each value is the pixel intensity (0 for black, 255 for white).

#  Perform basic operations on this "image."

# Create a 5x5 NumPy array where pixel values are random integers between 0 and 255.

# Normalize the pixel values to a range between 0 and 1.

# Identify the positions of the brightest pixels (value > 0.8 after normalization).

# Identify the positions of the darkest pixels (value < 0.2 after normalization).

# Pixels with values ≥ 0.5 are set to 1 (white).

# Pixels with values < 0.5 are set to 0 (black).

# Horizontally (left-to-right).

# Vertically (top-to-bottom).

# Add random noise (values between -0.1 and 0.1) to the normalized array
#  and clip the values to stay within [0, 1].

# Create a 3x3 kernel filter and apply convolution to blur the image.

# Save the final processed image to a file.
import numpy as np
import pandas as pd
import random

img=np.random.randint(0,255,size=25)
print(img)


image_array=img.reshape(5,5)
print(image_array)

normalized_ary=image_array/255

print(normalized_ary)
nmr=normalized_ary
# brightest=normalized_ary


df=pd.DataFrame(normalized_ary)
# print(df.describe())

# brightest=np.percentile(normalized_ary,80)
brightest=[]
count=0
for i in normalized_ary:
    if count<5:
        # if i>=0.8:
            brightest.append(i)
            count+=1





print("---------------",brightest)

# darkest=[]

# df.sort_values(0,ascending=True)
# print(df.head(5))
