import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import img_to_array
from tf_keras_vis.utils import normalize
from matplotlib import cm 
from tf_keras_vis.gradcam import Gradcam

def get_result_and_class_us(image_path):
    model = models.load_model('models/model1_best.h5')
    img1_array = image_path
    img1_array = cv2.resize(img1_array,(128,128))
    img1_array = cv2.cvtColor(np.array(img1_array),cv2.COLOR_RGB2GRAY)
    img1_array = img1_array.reshape(128, 128, 1)
    images = np.asarray(np.array(img1_array))
    X = images
    X = X.astype('float32') 

    def loss(output):
        return(output)

    def model_modifier(mdl):
        mdl.layers[-1].activation = tf.keras.activations.linear # we change the activation function of last layer to linear

    gradcam = Gradcam(model, model_modifier=model_modifier, clone=False)
    cam = gradcam(loss, X , penultimate_layer=-1 )# the layer befor the softmax
    cam = normalize(cam)

    img1_array = np.repeat(img1_array, 3, axis=2)
    heatmapImg1 = np.uint8(cm.jet(cam[0])[..., :3] * 255 )
    heatmapImg1 = cv2.applyColorMap(heatmapImg1 , cv2.COLORMAP_JET)
    alpha = 0.85
    overlay = heatmapImg1.copy() # copy the image
    result1 = cv2.addWeighted(img1_array, alpha, heatmapImg1 , 1-alpha, 0)

    scale_precent = 300
    w = int(heatmapImg1.shape[1] * scale_precent / 100)
    h = int(heatmapImg1.shape[0] * scale_precent / 100)
    dim = (w,h)
    result1 = cv2.resize(result1, dim , interpolation=cv2.INTER_AREA)
    img1_array = cv2.resize(img1_array, dim , interpolation=cv2.INTER_AREA)

    imagen_gris = cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)
    imagen_redimensionada = cv2.resize(imagen_gris, (128, 128))
    array_imagen = img_to_array(imagen_redimensionada)/255.0
    array_imagen_expandida = np.expand_dims(array_imagen, axis=0)
    y_pred_prob = model.predict(array_imagen_expandida, batch_size=1, verbose=0)
    y_pred = y_pred_prob.argmax(axis=-1)


    return result1, img1_array, y_pred

