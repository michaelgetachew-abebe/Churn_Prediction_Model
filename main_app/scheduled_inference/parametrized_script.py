#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import random

import seaborn as sns
from matplotlib import pyplot as pyplot

import mlflow
# SOME AIRFLOW REALTED THINGS

import pickle
from sklearn.feature_extraction import DictVectorizer

def generate_msisdn(n):
    msisdn = []
    for i in range(n):
        msisdn.append('2517' + str(random.randint(100000000, 999999999)))

    return msisdn

def read_dataframe(filename: str):
    df = pd.read_csv(filename)
    return df

def preprocessor(df: pd.DataFrame):

    df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')
    df['totalcharges'] = df['totalcharges'].fillna(0)
    df['seniorcitizen'] = df['seniorcitizen'].replace({0: 'no', 1: 'yes'})

    df.columns = df.columns.str.lower().str.replace(' ','_')
    string_columns = list(df.dtypes[df.dtypes == 'object'].index)

    for col in string_columns:
        df[col] = df[col].str.lower().str.replace(' ','_')

    return df

def prepareDictionaries(df: pd.DataFrame):
    categorical = ['gender', 'seniorcitizen', 'partner', 'dependents',
               'phoneservice', 'multiplelines', 'internetservice',
               'onlinesecurity', 'onlinebackup', 'deviceprotection',
               'techsupport', 'streamingtv', 'streamingmovies',
               'contract', 'paperlessbilling', 'paymentmethod']
    numerical = ['tenure', 'monthlycharges', 'totalcharges']

    dicts = df[categorical + numerical].to_dict(orient='records')
    return dicts