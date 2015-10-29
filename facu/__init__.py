# -*- coding: utf-8 -*-
import matplotlib
import numpy as np
import pandas as pd
import os
import json
from dateutil.parser import parse
import datetime
import multiprocessing
from pylab import *
import re
import scipy.stats
import random 
import pymongo
from collections import Counter , defaultdict
import json
from gensim.matutils import unitvec
from scipy.stats import ttest_ind , kruskal , pearsonr



def clean_txt(txt, lang='en'):			
	txt = re.sub("[^\w ]+"," ",txt.lower().strip())
	return txt


def map_multi( f, l, cpu_n= multiprocessing.cpu_count()):
	pool = multiprocessing.Pool(cpu_n)
	res = pool.map( f, l)
	pool.close()
	pool.join()
	return res
	


