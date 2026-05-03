import cv2
import numpy as np

def convolve(image, kernel):
    iH, iW = image.shape
    kH, kW = kernel.shape
    
    # calculate padding sizes to handle image boundaries:
    # for even kernel sizes, top and left paddings are greater than bottom and right ones
    # this results later in matching the current pixel with the bottom right zone of the kernel
    pad_top = kH // 2
    pad_bottom = kH - pad_top - 1
    pad_left = kW // 2
    pad_right = kW - pad_left - 1
    
    # create padded image replicating borders of the image on the padding zones
    padded_img = np.pad(image, ((pad_top, pad_bottom), (pad_left, pad_right)), mode='edge')
    
    output = np.zeros_like(image, dtype=np.float64)
    
    for y in range(iH):
        for x in range(iW):
            # determine the patch chunk corresponding to the current pixel
            # in padded_img the actual image was shifted, thus [y : y + kH, x : x + kW]
            patch = padded_img[y : y + kH, x : x + kW]
            # apply linear combination of the kernel with the patch chunk
            output[y, x] = np.sum(patch * kernel)
            
    return output

def magnitude(grad_x, grad_y):
    # compute euclidean magnitude and normalize it between 0-255
    magnitude = np.sqrt(grad_x**2 + grad_y**2)
    magnitude = (magnitude / magnitude.max()) * 255
    return magnitude.astype(np.uint8)

def roberts_filter(img):
    rx_kernel = np.array([[1, 0], [0, -1]], dtype=np.float64)
    ry_kernel = np.array([[0, 1], [-1, 0]], dtype=np.float64)
    rx = convolve(img, rx_kernel)
    ry = convolve(img, ry_kernel)
    return magnitude(rx, ry)

def prewitt_filter(img):
    px_kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float64)
    py_kernel = np.array([[-1, -1, -1], [ 0,  0,  0], [ 1,  1,  1]], dtype=np.float64)
    prewittx = convolve(img, px_kernel)
    prewitty = convolve(img, py_kernel)
    return magnitude(prewittx, prewitty)

def sobel_filter(img):
    sx_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float64)
    sy_kernel = np.array([[-1, -2, -1], [ 0,  0,  0], [ 1,  2,  1]], dtype=np.float64)
    sobelx = convolve(img, sx_kernel)
    sobely = convolve(img, sy_kernel)
    return magnitude(sobelx, sobely)

def laplacian_filter(img):
    l_kernel = np.array([[0,  1, 0], [1, -4, 1], [0,  1, 0]], dtype=np.float64)
    laplacian = convolve(img, l_kernel)
    laplacian = np.abs(laplacian)
    laplacian = (laplacian / laplacian.max()) * 255
    return laplacian.astype(np.uint8)

in_files = [
    "gato1.jpg",
    "figures.jpg",
    "figuraV2.jpg",
    "cameraman.jpg"
]

for in_file in in_files:
    img = cv2.imread(in_file, 0)
    if img is None:
        print(f"Error reading {in_file}")
        continue
    roberts = roberts_filter(img)
    prewitt = prewitt_filter(img)
    sobel = sobel_filter(img)
    laplacian = laplacian_filter(img)
    cv2.imwrite(in_file.split(".")[0] + "_roberts.jpg", roberts)
    cv2.imwrite(in_file.split(".")[0] + "_prewitt.jpg", prewitt)
    cv2.imwrite(in_file.split(".")[0] + "_sobel.jpg", sobel)
    cv2.imwrite(in_file.split(".")[0] + "_laplacian.jpg", laplacian)
