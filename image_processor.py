from PIL import Image

def enhance_image(image_path, scale=2):
    image = Image.open(image_path)
    new_size = (image.width * scale, image.height * scale)
    enhanced_image = image.resize(new_size)  # تكبير الصورة
    enhanced_path = f"enhanced_{scale}x_" + image_path
    enhanced_image.save(enhanced_path)
    return enhanced_path

