from PIL import Image, ImageDraw, ImageFont

def create_cute_gift(message, font_size=40):
    # Create a blank image with a white background
    width, height = 400, 200
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Load a cute font
    font = ImageFont.truetype("C:\\Users\\payal\\.vscode\\ded\\cool\\Chewy-Regular.ttf", font_size)

    # Calculate text position to center it on the image
    text_width, text_height = draw.textlength(message, font) # type: ignore
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Add the cute message to the image
    draw.text((x, y), message, font=font, fill="black")

    # Save or display the cute image
    image.save("cute_gift.png")
    image.show()

# Example usage
create_cute_gift("You're Awesome!")
