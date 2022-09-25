import pandas as pd
from cryptocmd import CmcScraper
from datetime import date
import os,shutil
path = "C://Users//Milan Stojanovski//Desktop//CryptoApp"
# Get the list of all files and directories
def move_to_folder():
    path = "C://Users//Milan Stojanovski//Desktop//CryptoApp"
    dir_list = os.listdir(path)
    moveto = "C://Users//Milan Stojanovski//Desktop//CryptoApp//Historical Data"
    for x in os.listdir():
        if x.endswith(".csv"):
            src = path+"//"+x
            dst = moveto+"//"+x
            shutil.move(src,dst)
def rename(f_path):

    files = os.listdir(f_path)
    i = 1
    for f in files:
        old_name = f_path+"//"+f.split(".")[0]+".csv"
        new_name = f_path+"//"+f.split("_")[0]+"_DATA"+".csv"
        os.rename(old_name,new_name)
    i+=1

def generate_new_data_to_csv(crypto,startdate,enddate):

    scraper = CmcScraper(crypto, startdate, enddate)
    headers, data = scraper.get_data()
    json_data = scraper.get_data("json")
    scraper.export("csv")
    move_to_folder()
    rename(f_path=path)

def csv_to_dataframe(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data, columns=data.columns)
    return df

