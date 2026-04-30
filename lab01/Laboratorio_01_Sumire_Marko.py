import cv2
from matplotlib import pyplot as plt

def plot_hist(hist, file):
    plt.plot(hist)
    plt.title(file)
    plt.xlabel('Value')
    plt.ylabel('Freq')
    plt.xlim([0, 256])
    plt.show()

def count_pixels(img):
    hist = [0] * 256
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist[img[i][j]] += 1
    return hist

def equalize_hist(hist, total_pixels):
    hist_map = [0] * 256
    # se calcula la frequencia relativa acumulada de la intensidad y se multiplica por la canidad de pixeles
    for i in range(256):
        hist_map[i] = sum(hist[:i+1]) * 255 / total_pixels
    return hist_map

def equalize_image(img):
    hist = count_pixels(img)
    hist_map = equalize_hist(hist, img.shape[0] * img.shape[1])
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = hist_map[img[i][j]]
    return img

in_files = [
    "fz_gray.jpeg",
    "jo_gray.jpeg",
    "qw_gray.jpeg",
    "tft_gray.jpeg"
]

img
hist
eq_hist
eq_img

for in_file in in_files:
    img = cv2.imread(in_file, 0)
    if img is None:
        print(f"Error reading {in_file}")
        continue
    hist = count_pixels(img)
    eq_img = equalize_image(img)
    eq_hist = count_pixels(eq_img)
    plot_hist(hist, in_file + " - Original")
    plot_hist(eq_hist, in_file + " - Equalized")
    cv2.imwrite(in_file.split(".")[0] + "_eq.jpeg", eq_img)
