class BaseReader:
  '''
  Sample usage:
  '''
  def __init__(self, data_key, version_str,
               data_master=None, data_path=None # if master none, check in HF hub
               force_write_mode=False, cache_raw_dir='RAW_CACHE', #basic_cleaning_dir='BASIC_CLEANING', 
               cache_dir=None, kwargs:dict=None
              ):
    self.data_master = None
    self.hfhub = False
    if data_master:
      self.data_master = Path(data_master)
      # assert it is absolute path and exists
      # set builtins.DATA_MASTER_PATH
      # read self.conf from it
    else:
      self.hfhub = True
      
    self.data_key = builtins.DATA_KEY = data_key
    self.version_str = version_str
    
    if data_root:
      self.data_root <- data_root
      builtins.DATA_ROOT
      self.data_dir <- data_root/data_key
      self.target_dir <- data_dir/version_str
      
    self.force_write_mode = force_write_mode
    self.cache_raw_dir = cache_raw_dir
    self.cache_raw_path = data_dir / cache_raw_dir
    self.cache_dir = cache_dir
    self.kwargs = kwargs
    
  def get_version2flow_mapping (self, version_str) :
        raise NotImplementedError
  def read_raw(self):
  def read_raw_hfhub(self):
  def read_from_cache(self):
  def write_to_cache(self):
  def read_flow_write(self, **kwargs):
      
      
