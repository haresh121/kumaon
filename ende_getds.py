from .utils.text_clean import filter_long_short, fix_bad_token, filter_bad_tag
import datasets

class EnDe(object):
    def __init__( self, version_str, source_dir, cache_dir=None ):
        
        self.version_str = version_str
        self.source_dir = source_dir
        self.cache_dir = cache_dir
        self.download_cmd = 'mtdata signature used to download and organize data.'

        if version_str == 'BASIC_CLEANING':
            self.dataset = self.get_revision_basic_cleaning ( source_dir, cache_dir )
        else:
            raise ValueError( f'Version string {version_str} not found.' )

    def get_revision_basic_cleaning( self, source_dir, cache_dir ):
        # read dataset
        hf_dataset = datasets.load_dataset(
            path=self.source_dir, 
            cache_dir=self.cache_dir,
            )

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

        return hf_dataset

