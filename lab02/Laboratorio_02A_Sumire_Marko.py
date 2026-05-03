import cv2
import matplotlib.pyplot as plt

def mean_filter(img, kernel_size):
    dist = kernel_size // 2
    img_filtered = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # sum pixel intensities
            sum = 0
            # counter for valid pixels inside image bounds
            actual_pixels = 0
            for k in range(-dist, dist + 1):
                for l in range(-dist, dist + 1):
                    if i+k >= 0 and i+k < img.shape[0] and j+l >= 0 and j+l < img.shape[1]:
                        # converts uint8 to int, as img handles uint8 datatype
                        sum += int(img[i+k][j+l])
                        actual_pixels += 1
            img_filtered[i][j] = sum / actual_pixels
    return img_filtered

def median_filter(img, kernel_size):
    dist = kernel_size // 2
    img_filtered = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pixels = []
            for k in range(-dist, dist + 1):
                for l in range(-dist, dist + 1):
                    if i+k >= 0 and i+k < img.shape[0] and j+l >= 0 and j+l < img.shape[1]:
                        pixels.append(img[i+k][j+l])
            # sorting neighbour pixels to apply statistics filter
            pixels.sort()
            # then find the median pixel
            img_filtered[i][j] = pixels[len(pixels) // 2]
    return img_filtered

in_files = [
    "figuraV.png",
    "figures.jpg",
    "riceB.png"
]

mask_sizes = [3, 5, 7, 9, 11]

for in_file in in_files:
    img = cv2.imread(in_file, 0)
    for mask_size in mask_sizes:
        img_filtered = mean_filter(img, mask_size)
        img_filtered_median = median_filter(img, mask_size)
        # save image to file
        out_file_mean = in_file.split('.')[0] + '_mean_' + str(mask_size) + '.png'
        out_file_median = in_file.split('.')[0] + '_median_' + str(mask_size) + '.png'
        cv2.imwrite(out_file_mean, img_filtered)
        cv2.imwrite(out_file_median, img_filtered_median)
