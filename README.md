# kumaon
Customisable NLP Pipeline based out of `Hydra`, `Datasets` and `Transformers`. [ Under Development ]

### How to generate the dataset from `kumaon`

1. Run the setup.py initially by using the following command. `develop` is for installing a package from the local directory 
  ```python
  python setup.py develop
  ```
2. Now add your datasets to the respective folder and provide the path to the files in the `data_master.yaml` file, so that we can pass the data_files option to the HF datasets.

The optimal file directory structure will be as follows:
```
|-- data
|  |-- data_master.yaml
|  |-- ende
|  |  |-- RAW
|  |    |-- \\ raw data files goes here
|  |  |-- ende.py \\ name of this file should be same as of the directory it resides
|  |-- tanzil
|  |  |-- RAW
|  |    |-- \\ raw data files goes here
|  |  |-- tanzil.py \\ name of this file should be same as of the directory it resides
|-- kumaon
|   |-- __init__.py
|   |-- readers \\ add custom dataset codes unique to that dataset
|   |   |-- __init__.py
|   |   |-- ende_ds.py 
|   |   |-- tanzil_ds.py
|   |-- utils \\ text cleaning utils
|   |   |-- text_clean.py
|-- setup.py
|-- requirements.txt
|-- README.md
|-- .gitignore
```

### [WIP] Sample usage
The final library should be amenable for usage as follows:
```
import kumaon

# The following should read paracrawl data and write to LOCAL_PATH for specified langauges
ds_paracrawl_hf = kumaon.ParallelTextReader( data_key='para_crawl', version_str='RAW', 
      data_master=None, data_root=LOCAL_PATH, force_write_mode=True, 
      kwargs={lang_pairs='eng_deu, eng_fra', format='l1l2'} )

# The following should read the local data and write a CLEAN version to disk
ds_local = kumaon.ParallelTextReader( data_key='local', version_str='CLEAN', 
      data_master=LOCAL_MASTER_PATH, data_root=LOCAL_PATH, force_write_mode=True, )
```
* Prioritise reading HF data because there is enough of it available and we might not need a lot more beyond that. We can get to custom data later.
     
