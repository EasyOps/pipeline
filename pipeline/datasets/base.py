from abc import ABC, abstractmethod
from ..utils import (
    Registry,
    build_from_cfg,
    TranformsErrorType,
    KeyTransformsNotInDataset,
)

DATASETS = Registry("dataset")


def build_dataset(cfg, default_args=None):
    dataset = build_from_cfg(cfg, DATASETS, default_args)
    return dataset


class BaseDataset(ABC):
    @abstractmethod
    def __load__(self, *args, **kwargs):
        ...

    @abstractmethod
    def __save__(self, *args, **kwargs):
        ...
