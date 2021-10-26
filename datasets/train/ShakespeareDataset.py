# from os import path
from torch.utils.data import Dataset
import json
import glob
import wget
import torch


""""
List of JSON Objects:

@json:

    [
      {
      "Dataline": 1,
      "Play": "Henry IV",
      "PlayerLinenumber": "",
      "ActSceneLine": "",
      "Player": "",
      "PlayerLine": "ACT I"
      }, ...

"""

class ShakespeareDataset(Dataset):
    def __init__(self, path):
        #json object
        self.open_file = open(path)
        
        #preprocessed data
        self.torch_dataset = self.iter_over_json()

    def __len__(self):
        """
        @return int is the length of the dataset
        """
        return len(self.torch_dataset)

    def __getitem__(self, index):
        """
        @param index is the index
        @return is the string
        """
        return self.torch_dataset[index]

    def iter_over_json(self) -> [str]:
        """
        @returns a list of strings, with each element being a line from shakespeare
        """
        #grab the json object
        data = json.load(self.open_file)

        #data container for the json
        shakespeare_data = []

        #unpack json
        for obj in data:
            #grab the player, playerline
            shakespeare_data.append(obj["Player"] + ": " + obj["PlayerLine"])
    
        #data = [Player: lines, Player: lines, Player: lines....]

        #return list
        return shakespeare_data

