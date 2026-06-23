# 👁️ Computer Vision - OpenCV (cv2)

## 📌 Introduction
- OpenCV (Open Source Computer Vision Library)
- Used for image processing and computer vision tasks
- Helps analyze, modify, and extract information from images

---

## 🖼️ Image Handling

### Image Loading
- `cv2.imread()`
- Reads an image from a file

### Image Dimensions
- `img.shape`
- Returns image height, width, and channels

---

## 🎨 Image Processing

### Grayscale Conversion
- `cv2.cvtColor()`
- `cv2.COLOR_BGR2GRAY`
- Converts color images to grayscale for easier processing

---

## 👤 Haar Cascade Classifiers

### Face Detection
- `cv2.CascadeClassifier()`
- Haar Cascade Face Classifier
- Detects human faces in images

### Eye Detection
- Haar Cascade Eye Classifier
- Detects eyes within a face region

---

## 🔍 Object Detection

### `detectMultiScale()`
- Detects multiple objects in an image
- Returns coordinates of detected regions

### Face Localization
- Identifies the location of faces in an image
- Provides bounding box coordinates `(x, y, w, h)`

---

## 📦 Region of Interest (ROI)

### ROI Extraction
- `roi_gray`
- `roi_color`
- Extracts specific image regions for further processing

### Face Cropping
- Crops the detected face from the original image
- Creates focused face images for analysis

---

## ✏️ Image Annotation

### Bounding Boxes
- `cv2.rectangle()`
- Draws rectangles around detected faces and eyes
- Helps visualize object detection results

---

## 👀 Eye Validation

### Face Verification
- Detect eyes inside detected face regions
- Validate whether the face image is usable

### Two-Eye Rule
- Keep images containing two or more detected eyes
- Discard images with insufficient facial features

---

## 🧹 Dataset Cleaning using OpenCV

### Image Validation
- Detect faces in images
- Detect eyes within faces
- Remove invalid images

### Clean Dataset Creation
- Keep only high-quality face images
- Improve dataset consistency

---

## 📂 Dataset Organization

### Class-wise Image Processing
- Process images celebrity by celebrity
- Iterate through image folders

### Directory Management
- Create separate folders for processed images
- Store cleaned images systematically

### Image Saving
- `cv2.imwrite()`
- Save cropped face images to disk

### Unique File Generation
- Generate unique filenames for processed images
- Maintain organized dataset structure

---

## 🗂️ Dataset Mapping

### Celebrity Image Dictionary
- Map celebrity names to image paths
- Store processed image locations for future training

---

## 🎯 Feature Extraction Preparation

### Preprocessing Pipeline
- Face Detection
- Eye Detection
- Face Cropping
- Dataset Cleaning
- Dataset Organization

---

## 🚀 Applications

- Face Detection
- Eye Detection
- Dataset Cleaning
- Image Preprocessing
- Feature Extraction Preparation
- Image Classification Projects

---

## 🌊 Wavelet Transform

### Introduction
- Feature extraction technique used in image processing
- Highlights important patterns while reducing unnecessary details
- Helps machine learning models focus on distinctive image features

---

### PyWavelets
- `pywt`
- Python library for wavelet transformations

---

### Image Preprocessing

#### Grayscale Conversion
- Convert image to grayscale before applying wavelet transform

#### Normalization
- Convert pixel values to range 0–1
- Improves numerical stability

---

### Wavelet Decomposition

#### `pywt.wavedec2()`
- Performs 2D wavelet decomposition
- Extracts low-frequency and high-frequency image information

---

### Wavelet Reconstruction

#### `pywt.waverec2()`
- Reconstructs image using selected wavelet coefficients

---

### Feature Extraction

#### High Frequency Features
- Removes low-frequency information
- Emphasizes edges and facial details

#### Wavelet Image Generation
- Creates transformed image for feature extraction

---

## 🖼️ Image Resizing

### `cv2.resize()`
- Resizes images to fixed dimensions
- Used to standardize image size

### Standard Image Size
- `32 × 32`
- Ensures consistent input dimensions

---

## 🏗️ Feature Engineering

### Raw Image Features
- Extract features from original image

### Wavelet Features
- Extract features from wavelet-transformed image

### Feature Combination
- Combine raw image and wavelet features
- Creates richer feature representation

---

### Image Flattening

#### `reshape()`
- Converts image matrix into a feature vector
- Required for machine learning models

---

### Feature Matrix Creation

#### Input Features (`X`)
- Stores processed image features

#### Labels (`y`)
- Stores celebrity names/classes

---

### Dataset Preparation Pipeline

- Face Detection
- Eye Detection
- Face Cropping
- Wavelet Transform
- Image Resizing
- Feature Extraction
- Feature Vector Creation
- Dataset Generation

---