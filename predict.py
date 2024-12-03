import numpy as np
import os
from tensorflow import keras
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
# from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import render_template
import io


class plantleaf:

    def predictPlantImage(self, image_file):

        self.image_file = image_file

        # load the model
        model = load_model('CNN_Model.h5')

        basepath = os.path.dirname(__file__) # - org
        #basepath = os.path.dirname('Last Try')

        file_path = os.path.join(basepath, 'uploads', secure_filename(self.image_file.filename)) # - org
        # secure_filename - Pass it a filename and it will return a secure version of it.
        # This filename can then safely be stored on a regular file system and passed to os.

        #file_path = os.path.dirname('Last Try/temp')

        self.image_file.save(file_path)  # save the image for further use - org

        test_image = image.load_img(file_path, target_size=(224, 224)) # should be same as given in the code for input
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255
        test_image = np.expand_dims(test_image, axis=0)  # expand dimension - flattening it

        preds = model.predict(test_image)
        #print(preds)

        preds = np.argmax(preds,axis=1)  # The numpy. argmax() function returns indices of the max element of the array in a particular axis.
        #print(preds)

        if preds == 0:
            prediction = "Cassava Bacterial Blight"
            return prediction
        elif preds == 1:
            prediction = "Cassava Brown Streak Disease"
            return prediction
        elif preds == 2:
            prediction = "Cassava Green Mottle"
            return prediction
        elif preds == 3:
            prediction = "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot"
            return prediction
        elif preds == 4:
            prediction = "Corn_(maize)___Common_rust"
            return prediction
        elif preds == 5:
            prediction = "Corn_(maize)___healthy"
            return prediction
        elif preds == 6:
            prediction = "Corn_(maize)___Northern_Leaf_Blight"
            return prediction
        elif preds == 7:
            prediction = "Pumpkin__Alternaria cucumerina"
            return prediction
        elif preds == 8:
            prediction = "Pumpkin__Alternaria leaf blight"
            return prediction
        elif preds == 9:
            prediction = "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot"
            return prediction
        elif preds == 10:
            prediction = "Tomato___Bacterial_spot"
            return prediction
        elif preds == 11:
            prediction = "Tomato___Early_blight"
            return prediction
        elif preds == 12:
            prediction = "Tomato___Leaf_Mold"
            return prediction
        elif preds == 13:
            prediction = "Tomato___Septoria_leaf_spot"
            return prediction
        