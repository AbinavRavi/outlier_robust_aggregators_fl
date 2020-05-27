import torchvision.datasets as datasets
from torchvision.transforms import transforms
import utils

config = utils.read_config('./config.yml')
path = config['model']['data_path']

transform = transforms.ToTensor()
train_data = datasets.MNIST(root=path,train=True,download=False,transform=transform)
test_data = datasets.MNIST(root=path,train=False,download=False,transform=transform)


