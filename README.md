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
