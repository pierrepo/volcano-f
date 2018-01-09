"""
Convert and download data through UniProt API
Initial source:
- http://www.uniprot.org/help/api
- http://www.uniprot.org/help/api_idmapping
Programmatic access - Retrieving entries via queries
http://www.uniprot.org/help/api_queries
"""
__author__ = "Pierre Poulain"
__version__ = "0.1"
__license__ = "MIT"

import urllib.parse
import urllib.request
from urllib.error import URLError, HTTPError
import pandas as pd
import math as m
import numpy as np
import os

def set_CSV(path):
    """
    Opening the CSV file
    """
    data_csv = pd.read_csv(path, sep = '\t',header=0,na_filter = True,index_col=False,na_values =" NaN")
    return data_csv

def convert(ids, format_from, format_to, format_output='tab'):
    """
    Convert ids from format_from to format_to with UniProt API
    Possible formats (for from and to): http://www.uniprot.org/help/api_idmapping
    Possible columns: http://www.uniprot.org/help/uniprotkb_column_names
    """
    url = 'http://www.uniprot.org/uploadlists/'
    params = {
        'from': format_from,
        'to': format_to,
        'format': format_output,
        'columns': 'id,entry name,reviewed,length',
        'query': ' '.join(ids)
    }
    # Add email address here to help UniProt to debug in case of problem
    contact = 'bob@mail.net'
    headers = {'User-Agent': 'Python bot / '.format(contact)}
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(url, data, headers)
    page = ""
    try:
        response = urllib.request.urlopen(req)
        page = response.read().decode('utf8')
    except HTTPError as e:
        print('Server could not answer.')
        print('Error code: ', e.code)
    except URLError as e:
        print('Fail to reach the server.')
        print('Reason: ', e.reason)
    finally:
        return page


def set_sub_table(path):
    data_csv = pd.read_csv(path, sep = '\t', header=0, na_filter = True,index_col=False,na_values =" NaN")
    del data_csv["Unnamed: 0"]
    serie = []
    dat =pd.DataFrame()
    for number in data_csv["access"]:
        access_nb = str(number).rstrip('.0')
        serie.append(access_nb)
        buff = convert(serie, 'P_GI', 'ACC', 'tab')
        file = open("data_table/buff.csv", "w")
        for line in buff:
            file.write(line)
        file.close()
        if (os.stat("data_table/buff.csv").st_size == 0) :
            break
    dat = set_CSV("data_table/buff.csv")
    new = dat.iloc[:,0:4]
    new["access"] = serie
    return new

if __name__ == '__main__':
    main()
