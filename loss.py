import torch.nn.functional as F
import torch.nn as nn
import torch
import numpy as np

def loss(data,target):
    lf = nn.CrossEntropyLoss()
    loss_value = lf(data,target)
    return loss_value




