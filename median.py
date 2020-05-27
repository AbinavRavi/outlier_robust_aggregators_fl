import torch
import numpy as np
import utils

def median_grad(grads,num_machines,num_class,num_feature):
    grad_array = np.array(grads)
    grad_array = grad_array.reshape(num_machines,num_class*(num_feature+1))
    med = np.median(grad_array, axis=0)
    med = med.reshape(num_class,num_feature+1)
    return med