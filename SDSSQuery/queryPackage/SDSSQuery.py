'''
Created on Oct 23, 2018

@author: Matthew Peek
@change: 9 November 2018
'''
import sys
import warnings
from astroquery.sdss import SDSS
from astropy.units import arcmin
from astropy import coordinates as coords

class SDSSQuery:
    """
    SDSS Query constructor. Sets up search area by user defined 
    latitude and longitute in decimal degree format, and search cone size.
    Order of arguments latitude, longitude, and radiusMultiplier. 
    
    Queries data and stores in variable named 'result'. Loop goes through
    result appending ra's and dec's to lists for spectro query.
    
    @param param: latitude in decimal degree format.
    @param param: longitude in decimal degree format.
    @param param: int to multiply with arcminutes. Expands search area size.   
    """
    def __init__(self, latitude, longitude, radiusMultiplier):
        warnings.filterwarnings('ignore')
        self.rad = radiusMultiplier * arcmin
        self.position = coords.SkyCoord(latitude, longitude, frame='icrs', unit='deg')        
        self.result = SDSS.query_region(self.position, radius=self.rad, spectro=True)
        
        self.ra = []
        self.dec = []
        for i in range(0, len(self.result)):
            self.ra.append(self.result[i]['ra'])
            self.dec.append(self.result[i]['dec'])   
    #End SDSSQuery constructor
    
    """
    QuerySpectra function starts loop appending sky coordinates from ra's and dec's.
    Gets the spectra for objects found with coordinates module.
    @return: query spectra.
    """
    def querySpectra(self):
        co = []
        for i in range(0, len(self.ra)):
            co.append(coords.SkyCoord(self.ra[i], self.dec[i], frame='icrs', unit='deg'))
        self.spectra = SDSS.query_crossid(co, photoobj_fields=['modelMag_g', 'modelMag_r'])
        
        print(self.spectra)
        sys.stdout.flush()
        return self.spectra
    #End querySpectra function
        
    """
    Query Result function gets the query result from the constructor and returns it.  
    @return: query result.
    """
    def queryResult(self):
        print(self.result,'\n')
        sys.stdout.flush()
        return self.result
    #End queryResult function    
    
"""
Test SDSSQuery Class Implementation
"""
#target1 = SDSSQuery(143.50993, 55.239775, 4)
#target1.queryResult()
#target1.querySpectra()

