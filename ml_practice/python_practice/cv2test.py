
# import cv2

# import pandas as pd
# import numpy as np
# import pytesseract
# from PIL import Image,ImageFont,ImageDraw
# from PIL import ImageFilter
# from deep_translator import GoogleTranslator

# # img =  cv2.imread("one.png")
# # cv2.imshow("image window",img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows() 

# # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # cv2.imshow("gray image",gray)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # resized = cv2.resize(img,(100,75))
# # cv2.imshow("resized image",resized)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # edges = cv2.Canny(img,200,100)
# # cv2.imshow("edges image",edges)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # gussain_blur = cv2.GaussianBlur(img,(5,5),0)
# # median = cv2.medianBlur(img,5)

# # cv2.imshow("gussain blur",gussain_blur)

# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # cv2.imshow("median blur",median)

# # cv2.waitKey(0)
# # cv2.destroyAllWindows()



# img = cv2.imread("lion.jpg")
# # cv2.imshow("image of lion",img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()


# resized = cv2.resize(img,(400,300))
# cv2.imshow("resized image",resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# edges = cv2.Canny(resized,100,200)
# cv2.imshow("edges",edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 
# import cv2
# import numpy as np

# # Load and convert image to grayscale
# img = cv2.imread('lion.jpg')

# resized = cv2.resize(img,(400,300))
# cv2.imshow("resized image",resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)


# # Apply binary threshold
# _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# # Create a kernel (you can change the size)
# kernel = np.ones((5, 5), np.uint8)

# # Apply erosion
# erosion = cv2.erode(thresh, kernel, iterations=1)

# # Apply dilation
# dilation = cv2.dilate(thresh, kernel, iterations=1)

# # Show results
# cv2.imshow("Original", resized)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imshow("Thresholded", thresh)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imshow("Erosion", erosion)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imshow("Dilation", dilation)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import pytesseract
import numpy as np
from deep_translator import GoogleTranslator
from PIL import Image, ImageDraw, ImageFont

# Configure Tesseract path for Windows users
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
image_path = "free.png"
image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Error loading image: {image_path}")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding for better OCR accuracy
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# OCR text detection
detection_data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
translator = GoogleTranslator(source='auto', target='gu')  # Gujarati language

# Convert OpenCV image to PIL format
pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(pil_image)

# Load a font that supports Gujarati (Ensure you have a suitable font file)
font_path = "D:\\python_practice\\Noto_Sans_Gujarati\\NotoSansGujarati-VariableFont_wdth,wght.ttf"  # Path to the Gujarati font
font = ImageFont.truetype(font_path, 30)  # Adjust size as needed

# Iterate through detected text and translate
for i in range(len(detection_data["text"])):
    text = detection_data["text"][i].strip()
    if text:
        x, y, w, h = (
            detection_data["left"][i],
            detection_data["top"][i],
            detection_data["width"][i],
            detection_data["height"][i],
        )

        try:
            translated_text = translator.translate(text)
            print(f"Original: {text} -> Translated: {translated_text}")
        except Exception as e:
            print(f"Translation error for '{text}': {e}")
            translated_text = text  # Use original text if translation fails

        # Draw a white rectangle over detected text (for clear space)
        draw.rectangle([x, y, x + w, y + h], fill="white")

        # Calculate text size and adjust font size if necessary to fit within the box
        text_bbox = draw.textbbox((x, y), translated_text, font=font)  # Get the bounding box of the text
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]  # width and height

        while text_width > w and font.size > 10:  # Reduce font size until text fits
            font = ImageFont.truetype(font_path, font.size - 1)
            text_bbox = draw.textbbox((x, y), translated_text, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # Overlay translated text using PIL (adjust the position to avoid text clipping)
        draw.text((x + (w - text_width) // 2, y + (h - text_height) // 2), translated_text, font=font, fill="black")

# Convert back to OpenCV format
image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

# Save and display modified image
output_path = "translated_image1.png"
cv2.imwrite(output_path, image)
print(f"Translated image saved as {output_path}")

cv2.imshow("Translated Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


