import yaml

def read_config(file):
    with open(file,'r') as stream:
        cxr_config = yaml.full_load(stream)
    return cxr_config