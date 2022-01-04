import datasets
from typing import List
from .textcleanutils import op_dict


class CleanText:
    def __init__(self, op, tags=None):
        op = op_dict[op]
        if not tags:
            self._setattr(lambda self, sent: op(sent))
        else:
            self._setattr(lambda self, sent: op(sent, tags))

    @classmethod
    def _setattr(cls, f):
        setattr(cls, '__call__', f)


class ReadSource(object):
    def __init__(self, directory, langs, cache_dir):
        self.dir = directory
        self.langs = langs
        self.cache_dir = cache_dir
    
    def __call__(self):
        return datasets.load_dataset(self.dir, None or self.cache_dir)
    

class ProcessFlow(object):
    def __init__(self):
        # Data should be concatenated
        self.__data__ = None
        self.processed_data = None
        self.filter_cols = []
        self.piped_data = None
        
    def __call__(self, data: datasets.Dataset, flow: dict):
        self.data = data
        
        for op in flow['transform_order']:
            data = self.data.map(lambda sent: flow[op](sent['text']))

        data = data.filter(self.check_filter)
        return data