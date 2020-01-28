import urllib
import xml.etree.ElementTree as ET

#The Below Documentation has been very handy. Go through it each time you open this program.
#https://docs.python.org/2/library/xml.etree.elementtree.html


def mov():
                
        movie = raw_input("\nEnter Movie name\n")

        movie.replace(' ', '+')

        url = 'http://www.omdbapi.com/?t=' + movie + '&y=&plot=short&r=xml'

        tree = ET.parse(urllib.urlopen(url))
        root = tree.getroot()


        movie_dict = {}
        

        for child in root:
                movie_dict[child.tag] = child.attrib
		#print (child.tag)
                

        #for k,v in movie_dict.items():
         #      print k


        arg = raw_input("Enter property\n").lower()

        print movie_dict['movie'][arg]





#Press ctrl+c to exit
while True:
        mov()
