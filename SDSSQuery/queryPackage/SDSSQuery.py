'''
Created on Oct 23, 2018

@author: Matthew Peek
@change: 26 November 2018
'''
import warnings
from astroquery.sdss import SDSS
from astropy.units import arcmin
from astropy import coordinates as coords

class SDSSQuery:
    """
    SDSS Query constructor. Sets up search area by user defined 
    latitude and longitute in decimal degree format, and search cone size.
    Order of arguments latitude, longitude, and radiusMultiplier. 
    
    @param param: latitude in decimal degree format.
    @param param: longitude in decimal degree format.
    @param param: int to multiply with arcminutes. Expands search area size.   
    """
    def __init__(self, longitude, latitude, radiusMultiplier):
        warnings.filterwarnings('ignore')
        self.rad = radiusMultiplier * arcmin
        self.position = coords.SkyCoord(longitude, latitude, frame='icrs', unit='deg')             
        self.ra = []
        self.dec = []    
    #End SDSSQuery constructor
    
    """
    StandardQuery function gets search position from constructor and performs
    actual query. Goes through ra and dec columns and appends to lists for
    use by querySpectra function.
    @return: standard query result.
    """
    def standardQuery(self):
        self.result = SDSS.query_region(self.position, radius=self.rad, spectro=True)
        try:
            for i in range(0, len(self.result)):
                self.ra.append(self.result[i]['ra'])
                self.dec.append(self.result[i]['dec'])
            return self.result
        except:
            return ValueError("No Results found"'\n'"Try a different search area.")
    #End standardQuery function
    
    """
    QuerySpectra function starts loop appending sky coordinates from ra's and dec's.
    Gets the spectra for objects found with coordinates module.
    @return: query spectra.
    """
    def querySpectra(self):
        try:
            self.standardQuery()
            coord = []
            for i in range(0, len(self.ra)):
                coord.append(coords.SkyCoord(self.ra[i], self.dec[i], frame='icrs', unit='deg'))
            self.spectra = SDSS.query_crossid(coord, photoobj_fields=['modelMag_g', 'modelMag_r'])       
            return self.spectra
        except:
            return ValueError("No Results found"'\n'"Try a different search area.")
    #End querySpectra function
    
    """
    ShowSpectraQuery function prints out querySpectra result for viewing.
    """    
    def showSpectraQuery(self):
        #print(self.querySpectra())
        return self
    #End showSpectraQuery
    
    """
    ShowStandardQuery function prints out standardQuery result for viewing.
    """    
    def showStandardQuery(self):
        #print(self.standardQuery())
        return self
    
"""
Test SDSSQuery Class Implementation

target1 = SDSSQuery(143.50993, 55.239775, 4)
target1.showStandardQuery()
target1.showSpectraQuery()
"""
