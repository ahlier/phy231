import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1
imcal = Image.open('Graticule100x.jpg')
pixcal = np.array(imcal)
# convert the image into a 2-D array, with number representing its intensity

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
# creates a plot with 2 subplots
ax[0].imshow(pixcal, cmap='gnuplot2')
ax[0].axhline(y=450, color='r')  # draw a horizontal line at position 450
ax[0].set_xlabel('Position (pixel)')
ax[0].set_ylabel('Position (pixel)')

ax[1].plot(pixcal[450, ::], 'r-')
# plot the light intensity at horizontal line position 450,
# it is actually near the middle of the graph
fig.suptitle('Intensity Graph', fontsize=16)
ax[1].set_xlabel('Position (pixel)')
ax[1].set_ylabel('Light Intensity')
plt.show()
# The separation between the lines is approximately 160 pixels

# 2
imeco = Image.open('Ecoli100x.jpg')
pixcal_eco = np.array(imeco)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
ax[0].imshow(pixcal_eco, cmap='plasma')
ax[0].set_xlabel('Position (pixel)')
ax[0].set_ylabel('Position (pixel)')

ax[1].set(yscale='log')
ax[1].hist(pixcal_eco.flatten(), 60)
ax[1].set_xlabel('Light Intensity')
ax[1].set_ylabel('Frequency')

fig.suptitle('Image of E-coli and Distribution of Light Intensity')
plt.show()

# From the histogram, the threshold window for E.coli is roughly between 8 and 50

# 3
newpix = ((pixcal_eco<50) & (pixcal_eco>8)).astype('float')
# This will return numbers in pixcal_eco that is between 8 and 50

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
ax[0].imshow(pixcal_eco, cmap='plasma')
ax[0].set_xlabel('Position (pixel)')
ax[0].set_ylabel('Position (pixel)')
ax[0].set_title('Original Image')

ax[1].imshow(newpix,cmap='plasma')
ax[1].set_xlabel('Position (pixel)')
ax[1].set_ylabel('Position (pixel)')
ax[1].set_title('Image After Background Filtration')
plt.show()


# 4
Ecoli_pix = ((pixcal_eco<50) & (pixcal_eco>8))
# This will return True for numbers that satisfies the conditions, else False
percentage = 100*np.sum(Ecoli_pix)/np.size(Ecoli_pix)
# np.sum(Ecoli_pix) total number of pixels that are E-coli,
# np.size(Ecoli_pix) is total number of pixel
print('{}% of the image is covered by E-coli'.format(percentage))
# 0.7221766880580357% of the image is covered by E-coli



