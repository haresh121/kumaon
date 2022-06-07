class ParallelTextReader(BaseReader):
  def __init__(self, data_key, version_str, 
            data_master, data_root, 
            force_write_mode=False, cache_dir=None, kwargs=None
        ):
    
  def get_version2flow_mapping(self, version_str):
    return { name: function }
  
  def read_raw_hfhub( self ):
    overload to read translation datasets from hfhub
    
  def filter_dataset( self, lang_pairs, splits ): # assume specific key format for datasets like split.lang_pair.lang1/2 etc
  def alpha_correct_dataset( self ): # use pycountry library
  def pair_parallel_data( self, lang_pairs ): # think how one would use flores datasets with 101 languages
  def prepend_to_data_key( self, prefix ): # when concating datasets ensure keys arent repeated by prepending datakey to keys in datasetdict
  def writerevision_XXX( self, source_dir, target_dir ):
