# -*- coding: utf-8 -*-
import pandas as pd 
import os

path=input('paste the full path')

file_name=input('what is the name of the excel file?')
extension=input('what is the files extension?')        
           

final_file=os.path.join(path,file_name + extension)

print (final_file)

path_save= os.path.join(path,file_name +"_merged"+extension)

print(path_save)

df= pd.read_excel(final_file)
df_lst=pd.read_excel(final_file,sheet_name=None).values()

print (df_lst)

df_lst = [dfx.transpose().reset_index().transpose() for dfx in df_lst]
df_result = pd.concat(df_lst, ignore_index=True)
df_result.to_excel(path_save, index=False, header=False)

