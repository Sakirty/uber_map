import gmplot 
import sys
latitude_list = []
longitude_list = []

tracefile = open(sys.argv[1],'r+')

for line in tracefile:
    sp = line.split(',')
    #sp[2] is latitute
    #sp[3] is longitute
    latitude_list.append(float(sp[2]))
    longitude_list.append(float(sp[3]))

#print(latitude_list)
#print(longitude_list)

  
gmap3 = gmplot.GoogleMapPlotter(40.513222980282265, 
                                -79.80447000453813, 13) 
gmap3.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8" 
# scatter method of map object  
# scatter points on the google map 
gmap3.scatter( latitude_list, longitude_list, '# FF0000', 
                              size = 40, marker = False ) 
  
# Plot method Draw a line in 
# between given coordinates 
gmap3.plot(latitude_list, longitude_list,  
           'cornflowerblue', edge_width = 2.5) 
  
gmap3.draw(sys.argv[2])

'''



'''

