import os,sys
import yaml
from motherboard.utils.main_utils import read_yaml_file
from motherboard.logger import logging
from motherboard.exception import AppException
from motherboard.entity.config_entity import ModelTrainerConfig
from motherboard.entity.artifacts_entity import ModelTrainerArtifact



class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config


    

    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            os.system("unzip data.zip")
            os.system("rm data.zip")
           
            os.system(f"yolo task=detect mode=train model={self.model_trainer_config.weight_name} data=data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true")


            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"cp runs/detect/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
           
            os.system("rm -rf yolov8s.pt")
            os.system("rm -rf train")
            os.system("rm -rf valid")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")
            os.system("rm -rf runs")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="artifacts/model_trainer/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise AppException(e, sys)
