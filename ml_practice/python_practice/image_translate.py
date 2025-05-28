import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pytesseract
from deep_translator import GoogleTranslator
import os

# Load image
image_path = 'free.png'
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file {image_path} not found.")

image = cv2.imread(image_path)
if image is None:
    raise ValueError("Failed to load image.")

# Make a copy to keep original colors
original_image = image.copy()

# Enhanced OCR preprocessing tailored for this image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Adjust contrast and apply adaptive thresholding
gray = cv2.convertScaleAbs(gray, alpha=1.2, beta=0)  # Increase contrast
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                              cv2.THRESH_BINARY, 15, 10)  # Adjusted block size and constant
# Noise reduction
thresh = cv2.medianBlur(thresh, 3)
ocr_image = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

# Get OCR results with bounding boxes
try:
    boxes = pytesseract.image_to_data(ocr_image, lang='eng', output_type=pytesseract.Output.DICT)
except Exception as e:
    raise RuntimeError(f"OCR processing failed: {e}")

# Convert to PIL for drawing
pil_image = Image.fromarray(cv2.cvtColor(original_image, cv2.COLOR_RGB2BGR))
draw = ImageDraw.Draw(pil_image)

# Load Gujarati font with fallback
font_path = r"Noto_Sans_Gujarati\NotoSansGujarati-VariableFont_wdth,wght.ttf"
# font_path= r"komedy-kritters\Komedy Kritters.ttf"
default_font_size = 20
font = None

try:
    font = ImageFont.truetype(font_path, default_font_size)
    print("✅ guj font loaded successfully.")
except Exception as e:
    print(f"❌ Font loading failed: {e}. Using default font.")
    font = ImageFont.load_default()

# Manual translation dictionary based on the image (for accuracy)   
translation_dict = {
    
    # Add more mappings as needed
}

# Translate and draw function
def translate_and_draw(word, x, y, w, h):
    if not word or not word.strip():
        return
    try:
        # Use manual translation if available, otherwise use GoogleTranslator
        translated = translation_dict.get(word.strip(), 
                                        GoogleTranslator(source='auto', target='gu').translate(word.strip()))
        if translated:
            # Sample color from original image at the box center
            roi_color = tuple(original_image[y + h//2, x + w//2].tolist())
            # Ensure rectangle fits within image bounds
            x_end = min(x + w, pil_image.width)
            y_end = min(y + h, pil_image.height)
            draw.rectangle([x, y, x_end, y_end], fill=roi_color)
            # Center the text
            text_bbox = draw.textbbox((x, y), translated, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = x + (w - text_width) // 2
            text_y = y + (h - text_height) // 2
            draw.text((text_x, text_y), translated, fill=(0, 0, 0), font=font)
    except Exception as e:
        print(f"Translation error for word '{word}': {e}")

# Process each detected word
n_boxes = len(boxes['text'])
for i in range(n_boxes):
    if int(boxes['conf'][i]) > 50:  # Confidence threshold
        text = boxes['text'][i].strip()
        if text:
            x, y, w, h = boxes['left'][i], boxes['top'][i], boxes['width'][i], boxes['height'][i]
            translate_and_draw(text, x, y, w, h)

# Save final image
output_path = "translated_final_image_improved.png"
try:
    final_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, final_image)
    print(f"✅ Image saved as {output_path}")
except Exception as e:
    raise RuntimeError(f"Failed to save image: {e}")

# Optional: Display the image (uncomment to use)
# cv2.imshow("Translated Image", final_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
