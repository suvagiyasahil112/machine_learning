import cv2test
import pytesseract
import numpy as np
from deep_translator import GoogleTranslator
from PIL import Image, ImageDraw, ImageFont

# Configure Tesseract path for Windows users
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
image_path = "free.png"
image = cv2test.imread(image_path)
if image is None:
    raise ValueError(f"Error loading image: {image_path}")

# Convert to grayscale
gray = cv2test.cvtColor(image, cv2test.COLOR_BGR2GRAY)

# Apply thresholding for better OCR accuracy
gray = cv2test.threshold(gray, 0, 255, cv2test.THRESH_BINARY + cv2test.THRESH_OTSU)[1]

# OCR text detection
detection_data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
translator = GoogleTranslator(source='auto', target='gu')  # Gujarati language

# Convert OpenCV image to PIL format
pil_image = Image.fromarray(cv2test.cvtColor(image, cv2test.COLOR_BGR2RGB))
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
image = cv2test.cvtColor(np.array(pil_image), cv2test.COLOR_RGB2BGR)

# Save and display modified image
output_path = "translated_image1.png"
cv2test.imwrite(output_path, image)
print(f"Translated image saved as {output_path}")

cv2test.imshow("Translated Image", image)
cv2test.waitKey(0)
cv2test.destroyAllWindows()


