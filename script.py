import argparse
from os import listdir, path, unlink
from PIL import Image, ImageFont, ImageDraw

def create_thumb(image_path, image_output_path, font_path, text_size, text_x_position, text_y_position, text, number, number_size, text_color = (0xff, 0xff, 0xff)):
    original_img = Image.open(image_path)
    editable_img = ImageDraw.Draw(original_img)

    font_text = ImageFont.truetype(font_path, text_size)
    font_number = ImageFont.truetype(font_path, number_size)

    width, height = original_img.size 
    pos_x = width * text_x_position 
    pos_y = height * text_y_position

    text_w, text_h = font_text.getsize(text)
    editable_img.text((pos_x - (text_w / 2), pos_y), text, text_color, font=font_text)

    number_w, number_h = font_number.getsize(number)
    editable_img.text((pos_x - (number_w / 2), pos_y + text_h), number, text_color, font=font_number)

    original_img.save(image_output_path)

def command_line_args(avaliable_images):
    parser = argparse.ArgumentParser(prog="Thumbnail generator", description="Avaliable arguments thumb generator")

    parser.add_argument("-i", "--image", dest="Image", choices=avaliable_images, help="Image file (include image format)")
    parser.add_argument("-t", "--text",  dest="Text", help="Image text")
    parser.add_argument("-n", "--number", dest="Number", help="Image number")
    parser.add_argument("-x", "--coorX", dest="CoorX", type=float, help="Text X position (between 0 and 1)")
    parser.add_argument("-y", "--coorY", dest="CoorY", type=float, help="Text Y position (between 0 and 1)")
    parser.add_argument("-st", "--fontSizeText", dest="FontSizeText", type=int, help="Font size text")
    parser.add_argument("-sn", "--fontSizeNumber", dest="FontSizeNumber", type=int, help="Font size number")
    parser.add_argument("-I", "--Iterator", dest="Iterator", type=int, default=1, help="Quantity of thumbs to generate")
    parser.add_argument("-U", "--useArgs", dest="UseArgs", action='store_true', help="Should be informed to enable command line args.")
    parser.add_argument("-C", "--clearOutputDir", dest="ClearOutputDir", action='store_true', help="Remove all thumbs in output dir before add new ones.")

    return parser.parse_args()

def clear_output_dir(output_dir):
    for filename in listdir(output_dir):
        file_path = path.join(output_dir, filename)
        try:
            if path.isfile(file_path) or path.islink(file_path):
                unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

if __name__ == '__main__':
    font_path = './assets/Montserrat-Bold.ttf' 
    templates_dir = './templates'
    output_dir = './thumbs'

    avaliable_images = listdir(templates_dir)

    args = command_line_args(avaliable_images)

    if args.UseArgs:
        image_name, image_extension = path.splitext(args.Image)
        image_path = path.join(templates_dir, f"{image_name}{image_extension}")

        if args.ClearOutputDir: clear_output_dir(output_dir)

        for iteration in range(args.Iterator): 
            number = str(int(args.Number) + iteration)
            image_output_path = path.join(output_dir, f"{image_name}_{number}{image_extension}")
            create_thumb(image_path, image_output_path, font_path, args.FontSizeText, args.CoorX, args.CoorY, args.Text, number, args.FontSizeNumber)
    else:
        print("Welcome to Thumbnail Generator")
        print("Select a template image")

        for img in range(len(avaliable_images)):
            print(f"{img} - {avaliable_images[img]}")

        image = avaliable_images[int(input("Template image: "))]
        thumb_text = input("Thumbnail text: ")
        thumb_number = input("Thumbnail number: ")
        x_pos = float(input("Text horizontal position (between 0 and 1): "))
        y_pos = float(input("Text vertical position (between 0 and 1): "))
        text_size = int(input("Text size: ")) 
        number_size = int(input("Number size: ")) 
        iterations = int(input("Quantity of thumbs to be generated: "))
        should_clear_output_dir = True if 'y' in input("Should clear output directory [y/n]: ") else False 
        
        image_name, image_extension = path.splitext(image)
        image_path = path.join(templates_dir, f"{image_name}{image_extension}")

        if should_clear_output_dir: clear_output_dir(output_dir)

        for iteration in range(iterations): 
            number = str(int(thumb_number) + iteration)
            image_output_path = path.join(output_dir, f"{image_name}_{number}{image_extension}")
            create_thumb(image_path, image_output_path, font_path, text_size, x_pos, y_pos, thumb_text, number, number_size)

