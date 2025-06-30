import cv2
import numpy as np

# Load image and convert to grayscale
img = cv2.imread('digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Split the image into 5000 cells, each 20x20
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
# Convert list of lists to a numpy array of shape (50, 100, 20, 20)
x = np.array(cells)

# Prepare train and test data
train = x[:, :50].reshape(-1, 400).astype(np.float32)  # 2500 samples
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)  # 2500 samples

# Corrected label generation
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]  # shape (2500, 1)
test_labels = train_labels.copy()

# Create and train kNN model
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

# Perform prediction
ret, result, neighbors, dist = knn.findNearest(test, k=1)

# Compare result with test_labels
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * 100.0 / result.size

print(accuracy)
