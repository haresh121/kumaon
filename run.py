from omegaconf import OmegaConf
from omegaconf import DictConfig
from hydra.utils import instantiate
import hydra
from pprint import pprint

@hydra.main(config_path="configs/", config_name="config.yaml")
def main(config: DictConfig):
    config = instantiate(config)
    data = (config.dataprep.datasets.ende.source)()
    print(data)
    flow = config.dataprep.datasets.ende.flow
    execute_flow = config.dataprep.datasets.ende.process_flow
    final_data = execute_flow(data, flow)
    
    print(final_data)
    
    
    

if __name__ == "__main__":
    main()