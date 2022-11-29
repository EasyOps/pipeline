from abc import ABC, abstractmethod
from ..utils import Registry, build_from_cfg

DATASETS = Registry('dataset')

def build_dataset(cfg, default_args=None):
    dataset = build_from_cfg(cfg, DATASETS, default_args)
    return dataset

class BaseDataset(ABC):
    
    @abstractmethod
    def __load__(self, *args, **kwargs):
        ...
        
    def __save__(self, *args, **kwargs):
        ...
    
    