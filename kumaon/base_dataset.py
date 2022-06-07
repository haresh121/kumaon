# Copied and modified from [https://github.com/huggingface/datasets/blob/master/src/datasets/packaged_modules/text/text.py].

# segregating the following so that when writing para_crawl.py or europarl.py 
def _split_generators_default(self, dl_manager):
def _generate_tables_default(self, files):

# we only need to import this and to these like this
'''
master_conf = OmegaConf.load(builtins.DATA_MASTER_PATH)
data_root = builtins.DATA_ROOT
data_params = master_conf[builtins.data_key]
if subpath in data_params:
  data_params = OmegaConf.load( Path(data_root, subpath) )
make_path_absolute

from kumaon.datasets import _split_generators_default, _generate_tables_default

class Text(datasets.ArrowBasedBuilder):
    BUILDER_CONFIG_CLASS = TextConfig

    def _info(self):
        return datasets.DatasetInfo(features=self.config.features)

    def _split_generators(self, dl_manager):
        return  _split_generators_default(self, dl_manager)

    def _generate_tables(self, files):
        logger.info('Reading files with custom config.')
        return _generate_tables_default(self, files)
 '''
