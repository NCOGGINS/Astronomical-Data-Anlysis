'''
Created on Oct 23, 2018

@author: Matthew Peek
@change: 4 November 2018
'''
import sys
import warnings
from astroquery.sdss import SDSS
from astropy import coordinates as coords
from astropy.units import arcmin

class SDSSQuery:
    """
    SDSS Query constructor. Sets up search area by user defined search area in 
    hour, minute, second format and search cone size. 
    
    Queries data and stores in variable named 'result'.
    """
    def __init__(self, searchArea, radiusMultiplier):
        warnings.filterwarnings('ignore')
        position = coords.SkyCoord(str(searchArea), frame='icrs')        
        self.result = SDSS.query_region(position, radius=radiusMultiplier*arcmin, spectro=True)
    #End SDSSQuery constructor
    
    """
    Query Result function gets the query result from the constructor and returns it.
    
    @return: query result
    """
    def queryResult(self):
        print(self.result)
        sys.stdout.flush()
        return self.result
    #End queryResult function    
    
"""
Test SDSSQuery Class Implementation
"""
target1 = SDSSQuery('0h8m05.63s +14d50m23.3s', 4)
target1.queryResult()
