from dataclasses import dataclass
from typing import Optional
import pyarrow as pa
import datasets
import re

logger = datasets.utils.logging.get_logger(__name__)

# Copied and modified from [https://github.com/huggingface/datasets/blob/master/src/datasets/packaged_modules/text/text.py].

class TextConfig(datasets.BuilderConfig):
    """BuilderConfig for text files."""
    def __init__(self, **kwargs):
        self.features: Optional[datasets.Features] = None
        self.name = "ende"
        self.encoding: str = "utf-8"
        self.chunksize: int = 10 << 20  # 10MB
        self.data_files = {
            'en': '/anx/nlp/dat/ende/en/train.ori.pe',
            'de': '/anx/nlp/dat/ende/de/train.ori.src',
        }
        self.keep_linebreaks: bool = False
        self.sample_by: str = "paragraph"


class Text(datasets.ArrowBasedBuilder):
    BUILDER_CONFIG_CLASS = TextConfig

    def _info(self):
        return datasets.DatasetInfo(features=self.config.features)

    def _split_generators(self, dl_manager):
        """The `data_files` kwarg in load_dataset() can be a str, List[str], Dict[str,str], or Dict[str,List[str]].

        If str or List[str], then the dataset returns only the 'train' split.
        If dict, then keys should be from the `datasets.Split` enum.
        """
        if not self.config.data_files:
            raise ValueError(f"At least one data file must be specified, but got data_files={self.config.data_files}")
        data_files = dl_manager.download_and_extract(self.config.data_files)
        if isinstance(data_files, (str, list, tuple)):
            files = data_files
            if isinstance(files, str):
                files = [files]
            return [
                datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"files": dl_manager.iter_files(files)})
            ]
        splits = []
        for split_name, files in data_files.items():
            if isinstance(files, str):
                files = [files]
            splits.append(datasets.SplitGenerator(name=split_name, gen_kwargs={"files": dl_manager.iter_files(files)}))
        return splits

    def _generate_tables(self, files):
        logger.info('Reading files with custom config.')
        schema = pa.schema(self.config.features.type if self.config.features is not None else {"text": pa.string()})
        for file_idx, file in enumerate(files):
            batch_idx = 0
            with open(file, "r", encoding=self.config.encoding) as f:
                if self.config.sample_by == "line":
                    batch_idx = 0
                    while True:
                        batch = f.read(self.config.chunksize)
                        if not batch:
                            break
                        batch += f.readline()  # finish current line
                        batch = batch.splitlines(keepends=self.config.keep_linebreaks)
                        pa_table = pa.Table.from_arrays([pa.array(batch)], schema=schema)
                        # Uncomment for debugging (will print the Arrow table size and elements)
                        # logger.warning(f"pa_table: {pa_table} num rows: {pa_table.num_rows}")
                        # logger.warning('\n'.join(str(pa_table.slice(i, 1).to_pydict()) for i in range(pa_table.num_rows)))
                        yield (file_idx, batch_idx), pa_table
                        batch_idx += 1
                elif self.config.sample_by == "paragraph":
                    batch_idx = 0
                    batch = ""
                    while True:
                        batch += f.read(self.config.chunksize)
                        if not batch:
                            break
                        batch += f.readline()  # finish current line
                        batch = batch.split("\n")
                        #batch = re.split('\n|\r', batch)
                        pa_table = pa.Table.from_arrays(
                            [pa.array([example for example in batch[:-1] if example])], schema=schema
                        )
                        # Uncomment for debugging (will print the Arrow table size and elements)
                        # logger.warning(f"pa_table: {pa_table} num rows: {pa_table.num_rows}")
                        # logger.warning('\n'.join(str(pa_table.slice(i, 1).to_pydict()) for i in range(pa_table.num_rows)))
                        yield (file_idx, batch_idx), pa_table
                        batch_idx += 1
                        batch = batch[-1]
                elif self.config.sample_by == "document":
                    text = f.read()
                    pa_table = pa.Table.from_arrays([pa.array([text])], schema=schema)
                    yield file_idx, pa_table
