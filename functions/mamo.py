import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tf_keras_vis.utils import normalize
from matplotlib import cm 
from tf_keras_vis.gradcam import Gradcam

def get_result_and_class_mamo(image_path):
    model_i = models.load_model('models/vgg16_ft_2layer_2cl_best.h5')
    model = model_i.get_layer('vgg16')

    img1_array = image_path
    img1_array = cv2.resize(img1_array,(150,150))
    img1_array_p = cv2.cvtColor(np.array(img1_array),cv2.COLOR_RGB2BGR)
    images = np.asarray(np.array(img1_array_p))
    X = preprocess_input(images)
    def loss(output):
        return(output)
    def model_modifier(mdl):
        mdl.layers[-1].activation = tf.keras.activations.linear # we change the activation function of last layer to linear
    gradcam = Gradcam(model,model_modifier=model_modifier,clone=False)
    cam = gradcam(loss, X , penultimate_layer=-1 )# the layer befor the softmax
    cam = normalize(cam)
    heatmapImg1 = np.uint8(cm.jet(cam[0])[..., :3] * 255 )
    heatmapImg1 = cv2.applyColorMap(heatmapImg1 , cv2.COLORMAP_JET)
    alpha = 0.85
    result1 = cv2.addWeighted(img1_array, alpha, heatmapImg1 , 1-alpha, 0)
    scale_precent = 300
    w = int(heatmapImg1.shape[1] * scale_precent / 100)
    h = int(heatmapImg1.shape[0] * scale_precent / 100)
    dim = (w,h)
    result1 = cv2.resize(result1, dim , interpolation=cv2.INTER_AREA)
    img1_array = cv2.resize(img1_array, dim , interpolation=cv2.INTER_AREA)
    img1_array_p = np.expand_dims(img1_array_p, axis=0)
    prediccion = model_i.predict(img1_array_p)
    probabilidad = prediccion[0][0]
    # Obtener clase
    if probabilidad > 0.5:
        clase = 1
    else:
        clase = 0
    return result1, img1_array, clase

