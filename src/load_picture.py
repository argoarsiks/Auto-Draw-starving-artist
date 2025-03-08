from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def load_picture():
    Tk().withdraw()
    file_path = askopenfilename(title="The image must be 32x32 pixels in size.", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    image = Image.open(file_path).convert("RGB")
    if image.size != (32, 32):
        print("The image must be 32x32 pixels in size.")
        exit()
    pixels = image.load()
    return pixels