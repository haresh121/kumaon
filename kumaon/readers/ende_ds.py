from ..utils.text_clean import filter_long_short, fix_bad_token, filter_bad_tag
import datasets
from pathlib import Path

class EnDe(object):
    def __init__( self, version_str, data_dir, write_mode=False ):
        
        self.version_str = version_str
        self.data_dir = data_dir
        self.write_mode = write_mode
        self.download_cmd = ''

        self.Version2Flow_Mapping = {
            'BASIC_CLEANING' : self.writerevision_basic_cleaning
        }

        self.target_dir = Path(self.data_dir, version_str)
        if not self.write_mode :
            if not self.target_dir.exists() :
                raise ValueError(f'Path {self.target_dir} does not exist for reading.')
            self.dataset = datasets.load_from_disk( self.target_dir )
        else : # writing data to disk
            
            flow_executor = self.Version2Flow_Mapping[version_str]
            self.dataset =  flow_executor( self.data_dir, self.target_dir )

    def writerevision_basic_cleaning( self, source_dir, target_dir ):
        # read dataset
        hf_dataset = datasets.load_dataset( path=source_dir )

        # rename columns and concatenate
        hf_dataset['en'] = hf_dataset['en'].rename_column('text', 'en')
        hf_dataset['de'] = hf_dataset['de'].rename_column('text', 'de')
        hf_dataset = datasets.concatenate_datasets( (hf_dataset['en'], hf_dataset['de']), axis=1 )
        
        # apply methods
        hf_dataset = hf_dataset \
            .map ( lambda s: {'en_clean': fix_bad_token(s['en'])} ) \
            .map ( lambda s: {'de_clean': fix_bad_token(s['de'])} ) \
            .map ( lambda s: {'en_clean': fix_bad_token(s['en_clean'])} ) \
            .map ( lambda s: {'de_clean': fix_bad_token(s['de_clean'])} ) \
            .filter ( lambda s: filter_bad_tag(s['en_clean']) ) \
            .filter ( lambda s: filter_bad_tag(s['de_clean']) ) \
            .filter ( lambda s: filter_long_short(s['en_clean'].split(' '), 1, 25) ) \
            .filter ( lambda s: filter_long_short(s['de_clean'].split(' '), 1, 25) )

        hf_dataset.save_to_disk( target_dir )
        return hf_dataset

