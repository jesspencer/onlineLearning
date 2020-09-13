# -*- coding: utf-8 -*-
"""
python 3

-script is an automated etl pipeline to prepare data for Future of Online Learning Tableau Dashbaord.

-script takes the most recent Excel file you downloaded and saved in the your Future of Online Learning folder. 

-script takes World Bank data which is formatted by year and places all years into one column.

-script creates columns 8 columns to better organize the data prior to putting it in Tableau.

-script saves to excel file as "Revised"

Created on Thu Aug 20 16:47:13 2020

@author: Spencer-Jessica-E
"""
import os
import glob
import os.path
import pandas as pd
import numpy as np
import json

data_cfg_fp = 'cfg/configg.json'


class World():
    def __init__(self, dest_db=None):            
        # get phishing_cfg
        with open(data_cfg_fp) as json_file:
            data_cfg = json.load(json_file)
        
        self.cfg = data_cfg["World_Bank"]
   
    def Get_latestfile(self, check_directory):
        list_of_files = glob.glob(check_directory)
        latest_file = max(list_of_files, key=os.path.getctime)
#        latest_file_crtime = time.ctime(os.path.getmtime(latest_file))
        return latest_file

        
    def Column_add(self, series_code = None, newColumnName = None):
        df = self.df2
        # add columns needed
        cxo_conditions = [
        (df["Series Code"] == series_code)]
        cxo_conditions_values = [df["Values"].tolist()]
        df[newColumnName] = np.select( cxo_conditions, cxo_conditions_values)
        return df
    
    
    def Clean_Country(self):
        df = self.df2
        # filtering based on country name 
        df = df[df["Country Name"].isin(["Argentina", "Australia","Brazil",
           "China", "France", "Germany", "India", "Indonesia", "Italy", 
           "Japan", "Korea","Mexico", "Netherlands", "Russian Federation",
           "Saudi Arabia", "Spain", "Switzerland", "Turkey", "United Kingdom",
           "United States"])] 
        return df 
        
    def Execute(self):     
        #get file
        self.latest_file = self.Get_latestfile(self.cfg["homedir"] +  self.cfg["filetype"] )
        self.df = pd.read_excel(self.latest_file, sheet_name = self.cfg["sheet_name"])
        self.df2 = pd.melt(self.df, id_vars =["Series Code", "Series Name", "Country Name", "Country Code"], var_name = "Year1", value_name = "Values")
        # cleans data in year col
        self.df2["Year"]=self.df2["Year1"].str.extract(r'(\d\d\d\d)')
        #create 7 cols needed
        self.df2 = self.Column_add( "IT.CEL.SETS.P2", "Mobile Cellular Subscriptions")
        self.df2 = self.Column_add(  "IT.NET.USER.ZS", "Internet Usage Ratio")
        self.df2 = self.Column_add( "NY.GDP.MKTP.CD", "GDP")
        self.df2 = self.Column_add( "NY.GDP.MKTP.KD.ZG", "GDP Annual Growth")
        self.df2 = self.Column_add(  "SE.SEC.PRIV.ZS", "Secondary Enrollment")
        self.df2 = self.Column_add(  "EG.USE.ELEC.KH.PC", "Electrical Power Consumption")
        self.df2 = self.Column_add( "SP.POP.TOTL","Population" )
        
        #getting rid of Values col created during the melt
        self.df2.pop('Values') 
        self.df2.pop('Year1') 
        self.df2 = self.Clean_Country()
        #removes nan and resets index 
        self.df2.dropna().reset_index(drop=True)
        #load df to excel
        #path to where i want to save modified file along with the modified file name 
        file = self.cfg["homedir"] + "/" + "Revised.xlsx"
        self.df2.to_excel(file, index = False)
        return self.df2


#run script

a = World()
a.Execute()
