from datasets import load_dataset, DatasetDict, Dataset
from ..base import (
    BaseDataset,
    DATASETS,
    build_from_cfg,
    TranformsErrorType,
    KeyTransformsNotInDataset,
)
import pandas as pd
import logging
from typing import Any, Union, Dict, List


@BaseDataset.register
@DATASETS.register_module()
class CSVDataset(object):
    def __init__(self, data_files: Union[str, Dict, List[str]]) -> None:
        self.type = "csv"
        self.data_files = data_files
        self.dataset = self.__load__()

    def __load__(self) -> Union[DatasetDict, Dataset]:
        if isinstance(self.data_files, str):
            logging.info("Load data from {self.data_files}")
        elif isinstance(self.data_files, dict):
            str_keys = "--".join(list(self.data_files.keys()))
            logging.info(
                f"Load data from speciflic CSV file: {self.data_files} with key split is: {str_keys}"
            )
        elif isinstance(self.data_files, list):
            logging.info(f"Load multiple CSV files: {' '.join(self.data_files)}")
        dataset = load_dataset(self.type, data_files=self.data_files)
        logging.info("Done loading dataset")
        return dataset

    def apply(self, transforms: Dict) -> Union[Dataset, DatasetDict]:
        if not isinstance(transforms, dict):
            raise TranformsErrorType(self.tranfroms)
        for key, value in transforms.items():
            if isinstance(self.dataset, Dataset):
                if key not in self.dataset:
                    raise KeyTransformsNotInDataset(key)
                self.dataset = self.dataset.cast_column(key, value)
            else:
                for k in self.dataset:
                    if key not in self.dataset[k]:
                        raise KeyTransformsNotInDataset(key)
                    self.dataset[k] = self.dataset[k].cast_column(key, value)
        return self.dataset

    def __repr__(self) -> str:
        return self.dataset.features

    def __save__(self) -> Any:
        raise NotImplementedError()
