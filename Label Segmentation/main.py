from tensorflow.keras.models import load_model
import cv2
import numpy as np

model = load_model("cargo_model.keras") # Model is not uploaded to GitHub due to privacy reasons

class_names = ['AMAZON', 'C-PLT', 'FEDX', 'MIAM', 'UPS', 'USPS']

def predict_image(img_path):
    # Resmi oku ve yeniden boyutlandır
        image = cv2.imread(img_path)
        image_resized = cv2.resize(image, (64, 64))

        # Resmi bir diziye dönüştür ve boyutunu genişlet
        img_array = np.expand_dims(image_resized, axis=0)

        img_array = img_array / 255.0

        # Tahmini yap
        name_prediction, position_prediction = model.predict(img_array)

        # Tahmin edilen etiketi al
        predicted_index = np.argmax(name_prediction[0])
        predicted_class = class_names[predicted_index]

        # Bounding box koordinatlarını al
        x_coords = position_prediction[0][::2]
        y_coords = position_prediction[0][1::2]

        x_min = min(x_coords)
        x_max = max(x_coords)
        y_min = min(y_coords) 
        y_max = max(y_coords)

        # Text konumunu hesapla
        x = int(x_min)
        y = int(y_min - (y_max - y_min)/4) 

        cv2.putText(image, 
                    predicted_class,
                    (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    4, 
                    (0,0,255),  
                    10)

        cv2.imwrite(img_path, image) # Orijinal resmin üzerine yaz

#Kullanıcdan resim yolu al
image_path = input("Enter the path of the image: ")

predict_image(image_path)