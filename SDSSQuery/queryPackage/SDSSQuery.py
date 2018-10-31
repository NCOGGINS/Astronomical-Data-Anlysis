'''
Created on Oct 23, 2018

@author: Matthew Peek
@change: 26 October 2018
'''
import warnings
from astroquery.sdss import SDSS
from astropy import coordinates as coords
from astropy.units import arcmin

class SDSSQuery:
    """
    SDSS Query constructor.
    """
    def __init__(self):
        warnings.filterwarnings('ignore')
        
    """
    Query Object function queries CAS and returns results according to search area.
    @param param: search area in hour, minute, seconds format
    @param param: int expands search area by multiplying with arcminutes
    @return: query result in tabular format  
    """
    def queryObject(self, searchArea, radiusMultiplier):
        position = coords.SkyCoord(str(searchArea), frame='icrs')        
        self.result = SDSS.query_region(position, radius=radiusMultiplier*arcmin, spectro=True)
        print(self.result)
        return self.result
    
"""
Test SDSSQuery Class Implementation
"""
#target1 = SDSSQuery()
#target1.queryObject('0h8m05.63s +14d50m23.3s', 4)
