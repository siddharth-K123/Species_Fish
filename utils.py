import config
import pickle
import numpy as np
import pandas as pd
import json

class FishSpecies:
    def __init__(self, user_data):
        self.model_file_path = "Fish_species_detection.pkl"
        self.user_data = user_data
    
    def load_saved_data(self):
        with open ("Fish_species_detection.pkl", "rb") as f:
            self.model = pickle.load(f)

    def get_prediction(self):
        self.load_saved_data()

        Weight= eval(self.user_data["Weight"])

        Length1=eval(self.user_data["Length1"])
        Length2=eval(self.user_data["Length2"])
        Length3=eval(self.user_data["Length3"])
        Height=eval(self.user_data["Height"])
        Width=eval(self.user_data["Width"])
        test_array = np.array([Weight,Length1,Length2,Length3,Height,Width], ndmin = 2)
        predicted_class = self.model.predict(test_array)[0]
        return predicted_class

if __name__ =="__main__":
    fish = FishSpecies()


