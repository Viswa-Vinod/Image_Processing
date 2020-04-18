from PIL import Image, ImageFilter

# this file only has code using some of the apis of the Image class in PIL

def show_size(parent_folder, file_name):
    try:
        img = Image.open(f"{parent_folder}/{file_name}")
        print(img.size)
    except FileNotFoundError as err:
        print(f"image file {file_name} not found in folder {parent_folder}")

def save_file_png(folder, file_name, img):
    img.save(f"./{folder}/{file_name}.png", "png")

img = Image.open("./Pokedex/pikachu.jpg")

smooth_pickachu = img.filter(ImageFilter.SMOOTH)
greyscale_pickachu = img.convert("L")

save_file_png("Pokedex", "smooth_pickachu", smooth_pickachu)
save_file_png("Pokedex", "greyscale_pickachu", greyscale_pickachu)


astro_img = Image.open("./Astro/astro.jpg")

resized_astro = astro_img.resize((400, 400))

save_file_png("Astro", "resized_astro", resized_astro)
astro_img_copy = astro_img.copy()
astro_img_copy.thumbnail((400, 400))

save_file_png("Astro","astro_thumbnail", astro_img_copy)

show_size("Astro", "astro_thumbnail.png")
