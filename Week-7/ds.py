
# Python3 program for reverse geocoding. 
  
# importing necessary libraries 
import geocoder as g
import pprint 
  
def reverseGeocode(coordinates): 
    result = g.google(coordinates) 
      
    # result is a list containing ordered dictionary. 
    pprint.pprint(result)  
  
# Driver function 
if __name__=="__main__": 
      
    # Coorinates tuple.Can contain more than one pair. 
    coordinates =('293 Surrey St, San Francisco, CA 94131, USA') 
      
    reverseGeocode(coordinates)  