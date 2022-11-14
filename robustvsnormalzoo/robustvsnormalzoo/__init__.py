from robustbench.model_zoo import model_dicts as all_rb_models
from robustbench.model_zoo.enums import BenchmarkDataset, ThreatModel
from robustbench.utils import load_model as robustbench_load_model
import pandas as pd
import timm
import os
from glob import glob 
from tqdm import tqdm
import requests
import tarfile
import torch
import sys


MAPPING_CSV = os.path.join(os.path.split(os.path.abspath(__file__))[0], "model_mappings.csv")
CHECKPOINT_PATH = "./models_normal"
CLOUD_PATH = "https://zenodo.org/record/7097538/files/%DATASET%_normal_robustbench_%PAPERID%.tar"


def _download_file(url, path):
    response = requests.get(url)

    with open(path, "wb") as handle:
        for data in tqdm(response.iter_content(), desc=f"Downloading {url}", unit="B", unit_scale=True):
            handle.write(data)


def _download_checkpoint(dataset: str, model_id: str):
    # create folder if not exists
    local_path = os.path.join(CHECKPOINT_PATH, dataset, "Linf")
    os.makedirs(local_path, exist_ok=True)

    #download file
    cloud_path = CLOUD_PATH.replace("%DATASET%", dataset).replace("%PAPERID%", model_id)
    temp_file = os.path.join(local_path, f".{model_id}.temp.tar")
    _download_file(cloud_path, temp_file)

    # extract file
    tar = tarfile.open(temp_file)
    tar.extractall(local_path)
    tar.close()

    # clean up
    os.remove(temp_file)


def load_model(dataset: str, paper_id: str, robust: bool):

    assert dataset in ["cifar10", "cifar100", "imagenet"]

    if robust:
        # get model from robustbench
        model = robustbench_load_model(dataset=dataset, model_name=paper_id, threat_model=ThreatModel.Linf)
    else:

        # We only trained one model for identical archs, so we sometime need to map the name
        df_mapping = pd.read_csv(MAPPING_CSV, index_col=0)
        mapped_id = df_mapping[(df_mapping.Robust == paper_id) & (df_mapping.Dataset == dataset)].Normal.values[0]

        if dataset == "imagenet":
            # get model from timm
            model = timm.create_model(mapped_id, pretrained=True)

        else:
            ds_class = None
            for k in list(BenchmarkDataset):
                if k.value == dataset:
                    ds_class = k

            model = all_rb_models[ds_class][ThreatModel.Linf][paper_id]["model"]()

            # check if tar file exists
            ckpt_path = os.path.join(CHECKPOINT_PATH, dataset, "Linf/robustbench_" + mapped_id)
            matches = list(glob(os.path.join(ckpt_path, "version_0/checkpoints/*.ckpt")))
            if len(matches) == 0:
                _download_checkpoint(dataset, mapped_id)

            utils_path = os.path.split(os.path.realpath(__file__))[0]
            sys.path.append(utils_path) # this is an ultra hacky way to load ptl checkpoints
            state = torch.load(matches[0], map_location="cpu")
            sys.path.remove(utils_path)

            model.load_state_dict({k.replace("model.", "") : v for k, v in state["state_dict"].items()})

    return model


def list_models():
    df_mapping = pd.read_csv(MAPPING_CSV, index_col=0)
    models = []
    for _, row in df_mapping.iterrows():
        models.append((row.Dataset, row.Robust))
    return models


def download_all_checkpoints():
    df_mapping = pd.read_csv(MAPPING_CSV, index_col=0)
    for dataset in ["cifar10", "cifar100", "imagenet"]:
        for paper_id in df_mapping[df_mapping.Dataset == dataset].Robust.values:
            load_model(dataset, paper_id, robust=True)
            load_model(dataset, paper_id, robust=False)
