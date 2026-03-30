def extract_text(input_data, is_image=False):
    if not is_image:
        return input_data  # direct text

    try:
        import pytesseract
        from PIL import Image

        text = pytesseract.image_to_string(Image.open(input_data))
        return text
    except:
        return "Error reading image"