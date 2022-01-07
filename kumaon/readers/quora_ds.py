from ..utils.text_clean import filter_long_short, fix_bad_token, filter_bad_tag, filter_invalid_sent
import datasets
from pathlib import Path
from omegaconf import OmegaConf
import builtins



class Quora(object):
    '''
    Sample usage:
        from kumaon.readers.quora_ds import Quora
        quora = Quora(version_str='BASIC_CLEANING', 
                    data_master='/home/ubuntu/out/kumaon/data/data_master.yml', 
                    data_key='quora',
                    write_mode=True)
    '''
    def __init__( self, version_str, data_master, data_key, write_mode=False ):
        # version and fn
        self.version_str = version_str
        self.Version2Flow_Mapping = self.get_version2flow_mapping(self.version_str)
        assert version_str in self.Version2Flow_Mapping.keys()
        # data master and config
        self.data_master = Path(data_master)
        assert ( self.data_master.is_absolute() and self.data_master.exists() )
        builtins.DATA_MASTER_PATH = self.data_master
        self.data_key = data_key
        builtins.DATA_KEY = self.data_key
        # data and target dir
        self.conf = OmegaConf.load(self.data_master)
        self.data_dir = str( Path(self.conf.DATA_ROOT, data_key) )
        self.target_dir = Path(self.data_dir, self.version_str)
        self.write_mode = write_mode
        # read from source, flow through maps and write if required
        self.read_flow_write() 

    def read_flow_write(self):
        if not self.write_mode :
            if not self.target_dir.exists() :
                raise ValueError(f'Path {self.target_dir} does not exist for reading.')
            self.dataset = datasets.load_from_disk( self.target_dir )
        else : # writing data to disk            
            flow_executor = self.Version2Flow_Mapping[self.version_str]
            self.dataset =  flow_executor( self.data_dir, self.target_dir )

    def get_version2flow_mapping(self, version_str):
        return {
            'BASIC_CLEANING' : self.writerevision_basic_cleaning
        }

    def writerevision_basic_cleaning( self, source_dir, target_dir ):
        # read dataset
        hf_dataset = datasets.load_dataset( path=source_dir )

        # rename columns and concatenate
        
        # apply methods
        hf_dataset = hf_dataset \
            .filter( lambda s: filter_invalid_sent(s) ) \
            .map ( lambda s: {'q1_clean': fix_bad_token(s['question1'])} ) \
            .map ( lambda s: {'q2_clean': fix_bad_token(s['question2'])} ) \
            .filter ( lambda s: filter_bad_tag(s['q1_clean']) ) \
            .filter ( lambda s: filter_bad_tag(s['q2_clean']) ) \
            .filter ( lambda s: filter_long_short(s['q1_clean'].split(' '), 1, 25) ) \
            .filter ( lambda s: filter_long_short(s['q2_clean'].split(' '), 1, 25) )

        hf_dataset.save_to_disk( target_dir )
        return hf_dataset

