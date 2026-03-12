import os   
import numpy as np  # Array
import matplotlib.pyplot as plt
from PIL import Image # PIL -> Pillow
from sklearn.model_selection import train_test_split
from tensorflow import keras

# os.path.join จะใช้ระบุตำแหน่ง Folder แล้วเอาไปใส่ในตัวแปร ("dataset", "with_mask" = dataset\with_mask)
with_mask_path = os.path.join("dataset", "with_mask")  
without_mask_path = os.path.join("dataset", "without_mask") 

# os.listdir จะทำหน้าที่อ่านไฟล์ทั้งหมดแล้วเก็บในรูปแบบ List (['img1.jpg', 'img2.jpg']....)
with_mask_files = os.listdir(with_mask_path) 
without_mask_files = os.listdir(without_mask_path)

#----------------------------------------------
# Create Labels (Y)

# Machine Learning จะไม่เข้าใจว่า อะไรคือ Wear Mask / Without mask มันเข้าใจแค่ตัวเลข
with_mask_labels = [1] * len(with_mask_files)   # กำหนดเลข 1 = ใส่หน้ากาก / เช่นมี 3 รูป [1] * 3 = [1,1,1]
without_mask_labels = [0] * len(without_mask_files) # กำหนดเลข 0 = ไม่ใส่หน้ากาก เช่นมี 3 รูป [0] * 3 = [0,0,0]
labels = with_mask_labels + without_mask_labels # เอามาต่อกัน [1,1,1,0,0,0]

#----------------------------------------------
# Image Processing เปลี่ยนรูปภาพให้เป็นเลข เพราะคอมพิวเตอร์อ่านไฟล์ .jpg / .png ตรงๆ ไม่ได้

dataset = [] # รับข้อมูลที่ได้มา ตอนนี้เป็นแค่ List (X)

for img_file in with_mask_files:      # img_file = img1.jpg
    image = Image.open(os.path.join(with_mask_path, img_file)) # os.path.join = dataset\with_mask\imag1.jpg / Image.open = เปิดรูป
    image = image.resize((128,128)) # image.resize = ปรับขนาดรูปภาพให้ 128x128 pixels เพื่อให้ Model คงที่
    image =  image.convert("RGB") # image.convert เปลี่ยนรูปให้เป็นสี Red,Green,Blue เพราะบางรูปเป็นขาวดำ / (255,255,255) ถ้าโปร่งใส่จะมี 4 ชุด
    image = np.array(image) # แปลงไฟล์รูปเป็นตัวเลข โดยใช้เลข Pixel 3 ชุด (255,255,255) สแกนทั้งหมดให้เป็น array รวม 128 แถว
    dataset.append(image) # รวบรวมรูปลงไปใน List ชื่อ dataset

for img_file in without_mask_files:
    image = Image.open(os.path.join(without_mask_path, img_file))
    image = image.resize((128,128))
    image = image.convert("RGB")
    image = np.array(image)
    dataset.append(image)

#----------------------------------------------

# เหมือน Flashcard X คำถาม Y คำตอบ
X = np.array(dataset) # (จำนวนรูป, 128, 128, 3)
Y = np.array(labels) # [1,1,1,0,0,0]

# test_size = 0.2 = ให้ Test 20% / X_train, y_train ให้ model Train 80% / x_test, y_test ทดสอบ model 20%
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 2)  #  train_test_split ตัวช่วยสับไพ่ random_state -> With mask / Without_mask

# ปรับให้เรียนรู้เร็วขึ้น
X_train_scaled = X_train / 255
X_test_scaled = X_test / 255

num_of_classes = 2 # 2 อย่าง with mask / without mask

#----------------------------------------------
# Convolutional Neural Network

model = keras.Sequential([     # Sequential model / activation = "relu" = Activation Function เมือนแสกนเสร็จจะได้เลขเยอะมากๆ ถ้าติดลบจะตัดทิ้ง ถ้าบวกจะผ่านได้ / input_shape ให้รู้ว่าเป็น 128x128 RGB / Depth 32 ชั้น
    # CNN Layer 1
    keras.layers.Conv2D (32, kernel_size = (3,3), activation = "relu", input_shape = (128,128,3)), # kernel_size แสกนภาพขนาด 3x3 
    keras.layers.MaxPooling2D(pool_size = (2,2)), # ย่อรูปลงจาก 128x128 เป็น 64x64

    # CNN Layer 2
    keras.layers.Conv2D (64, kernel_size = (3,3), activation = "relu"),
    keras.layers.MaxPooling2D(pool_size = (2,2)), # ย่อรูปลงจาก 64x64 เป็น 32x32

    keras.layers.Flatten(), # ลดมิติลง
 
    # CNN Layer 3
    keras.layers.Dense(128, activation = "relu"), # Dense 128 = 128 Node
    keras.layers.Dropout(0.5),

    # CNN Layer 4
    keras.layers.Dense(64, activation = "relu"),
    keras.layers.Dropout(0.5),

    # CNN Layer 5
    keras.layers.Dense(num_of_classes, activation = "softmax") # activation = "softmax" แปลงตัวเลขเป็น % เช่น [0.95, 0.05] -> 95% ใส่หน้ากาก 5 % ไม่ใส่หน้ากาก
])

model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["acc"]) # optimizer = "adam" ปรับตัวเลข / loss ตรวจสอบว่าพลาดเท่าไร / metrics = ["acc"] ตรวจว่าถูกเท่าไร

# Train the model
history = model.fit(X_train_scaled, y_train, validation_split = 0.1, epochs = 5) # epochs จำนวนรอบ Optimizer

# แสดงผลให้บอกว่า Dataset With_mask / With_out_mask มีกี่รูป
print(f"Number of Mask Picture : {len(with_mask_files)}")
print(f"Number of Without Mask Picture : {len(without_mask_files)}")

# Evaluate for accuracy
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print (f"Test Accuracy - {accuracy}")

plt.figure(figsize = (12,4))

plt.subplot(1,2,1)
plt.plot(history.history["loss"], label = "Train loss")
plt.plot(history.history["val_loss"], label = "Validation loss")
plt.legend()
plt.title("Training Loss")

plt.subplot(1,2,2)
plt.plot(history.history["acc"], label = "Train accuracy")
plt.plot(history.history["val_acc"], label = "Validation accuracy")
plt.legend()
plt.title("Training Accuracy")
plt.show()


# Save Model (mask_model.h5)
model.save('mask_model.h5')
print("Model Saved Successfully as 'mask_model.h5'!")