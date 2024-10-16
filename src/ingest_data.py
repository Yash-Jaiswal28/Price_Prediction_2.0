import os
import zipfile
from abc import ABC, abstractmethod

import pandas as pd

# Define an abstract class for Data Ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str)-> pd.DataFrame:
        """Abstract method to ingest data from a given file."""
        pass


# Implement a concrete class for ZIP ingestion:
class ZipDataIngestor(DataIngestor):
    def ingest(self,file_path: str) -> pd.DataFrame:
        """Extract a .zip file and returns the content as a pandas DataFrame."""
         # Ensure the file is a .zip file
        if not file_path.endswith(".zip"):
            raise ValueError("Invalid file format. Please provide a .zip file.")
        
        # Extract the zip file
        with zipfile.ZipFile(file_path,"r") as zip_ref:
            zip_ref.extractall("extracted_data")

        # Find the extracted CSV file (assuming there is one CSV file inside the zip)
        extracted_files =  os.listdir("extracted_data")
        csv_file = [f for f in extracted_files if f.endswith(".csv")]

        if len(csv_file) == 0:
            raise ValueError("No CSV file found in the extracted data.")
        
        if len(csv_file) > 1:
            raise ValueError("Multiple CSV files found in the extracted data.")
        
        csv_file_path = os.path.join("extracted_data",csv_file[0])

        df = pd.read_csv(csv_file_path)

        return df
    
# Implement a Factory to create DataIngestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        """Returns the appropriate DataIngestor based on the file extension"""
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"Unsupported file extension: {file_extension}")
        

if __name__=="__main__":
    # Specift the file path
    file_path=r"D:\Yash-python\python\Tasks\Prediction_2.0\data\archive.zip"

    # Determine the file extension
    file_extension = os.path.splitext(file_path)[1]

    # Get the approriate DataIngestor
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    # Ingest the data and load it into a DataFrame
    df = data_ingestor.ingest(file_path)

    # Now df contains the DataFrame from the extracted CSV
    print(df.head())

