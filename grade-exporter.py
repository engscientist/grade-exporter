# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:50:25 2019
 
@author: Li
"""

import pandas as pd
importdf_source = "" # This is the XLSX file with raw data
exportdf_source = "" # This is the original CSV file with the organized data
exportdftest = "" # This is the new CSV with organized data with added grades
test = True
importdf = pd.read_excel(importdf_source, index_col = 'Student ID')
exportdf = pd.read_csv(exportdf_source, index_col = 'Username')
importdf_dict = dict(importdf)
exportdf_dict = dict(exportdf)
gradepair = importdf_dict['Grade']
itemname = '' # This is the item name (section) under which grades are added
newgrades = exportdf_dict[itemname]
idlist = list(gradepair.keys())
exportidlist = list(newgrades.keys())
for myid in idlist:
    mygrade = gradepair[myid]
    realid = myid + 1000000
    if realid in exportidlist:
        newgrades[realid] = mygrade
    else:
        print('Student ID ' + str(myid) + ' not found in export file.')
exportdf_dictkeylist = list(exportdf_dict.keys())
exportdf_dictkeylen = len(exportdf_dictkeylist)
exportdf_newdict = {}
for i in range(2):
    exportdf_dictkey = exportdf_dictkeylist[i]
    exportdf_newdict[exportdf_dictkey] = exportdf_dict[exportdf_dictkey]
exportdf_newdict['Username'] = exportdf_newdict[exportdf_dictkey]
for i in range(2, exportdf_dictkeylen):
    exportdf_dictkey = exportdf_dictkeylist[i]
    exportdf_newdict[exportdf_dictkey] = exportdf_dict[exportdf_dictkey]
exportdf_newdict[itemname] = newgrades
exportdf_new = pd.DataFrame(exportdf_newdict)
if test:
    exportdf_new.to_csv(exportdftest, index = False)
else:
    exportdf_new.to_csv(exportdf_source, index = False)
