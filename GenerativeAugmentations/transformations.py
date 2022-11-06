import scipy.spatial
import numpy as np
import random
import cv2
import math
from sklearn.cluster import KMeans

def Sketch(img):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img_gray[img_gray<2] = 2
    img_invert = cv2.bitwise_not(img_gray) #gray scale to inversion of the image
    img_smoothing = cv2.GaussianBlur(img_invert,(19,19),sigmaX=0,sigmaY=0) #smooting the inverted image
    
    def dodgeV2(x,y):
        return cv2.divide(x,255-y,scale=256)
    final_img = dodgeV2(img_gray,img_smoothing)
    final_img = cv2.GaussianBlur(final_img,(5,5),sigmaX=0,sigmaY=0)
    return final_img

def oilPainting(img):
    return cv2.xphoto.oilPainting(img, 7, 1)

def pencilSketch(img):
    img = cv2.GaussianBlur(img,(3,3),sigmaX=0,sigmaY=0) #smooting the inverted image
    dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=20, sigma_r=0.04, shade_factor=0.05) # inbuilt function to generate pencil sketch in both color and grayscale
    cv2.imshow("Image", img)
    cv2.imshow("Output2", dst_gray)
    cv2.imshow("Output", dst_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return dst_gray

def colorPencilSketch(img):
    img = cv2.GaussianBlur(img,(3,3),sigmaX=0,sigmaY=0) #smooting the inverted image
    dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=20, sigma_r=0.04, shade_factor=0.05) # inbuilt function to generate pencil sketch in both color and grayscale
    return dst_color



def compute_color_probabilities(pixels, palette):
    distances = scipy.spatial.distance.cdist(pixels, palette)
    maxima = np.amax(distances, axis=1)
    distances = maxima[:, None] - distances
    summ = np.sum(distances, 1)
    distances /= summ[:, None]
    return distances
def get_color_from_prob(probabilities, palette):
    probs = np.argsort(probabilities)
    i = probs[-1]
    return palette[i]
def randomized_grid(h, w, scale):
    assert (scale > 0)
    r = scale//2
    grid = []
    for i in range(0, h, scale):
        for j in range(0, w, scale):
            y = random.randint(-r, r) + i
            x = random.randint(-r, r) + j
    grid.append((y % h, x % w))
    random.shuffle(grid)
    return grid
def get_color_palette(img, n=20):
    clt = KMeans(n_clusters=n)
    clt.fit(img.reshape(-1, 3))
    return clt.cluster_centers_
def complement(colors):
    return 255 - colors

def pointillismArt(img, primary_colors=20):
    
    radius_width = int(math.ceil(max(img.shape) / 1000))
    palette = get_color_palette(img, primary_colors)
    complements = complement(palette)
    palette = np.vstack((palette, complements))
    canvas = img.copy()
    grid = randomized_grid(img.shape[0], img.shape[1], scale=3)
    
    pixel_colors = np.array([img[x[0], x[1]] for x in grid])
    
    color_probabilities = compute_color_probabilities(pixel_colors, palette)
    for i, (y, x) in enumerate(grid):
            color = get_color_from_prob(color_probabilities[i], palette)
            cv2.ellipse(canvas, (x, y), (radius_width, radius_width), 0, 0, 360, color, -1, cv2.LINE_AA)
    return canvas
