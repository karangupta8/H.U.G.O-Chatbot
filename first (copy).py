import aiml
import os


import urllib
import xml.etree.ElementTree as ET



# Create the kernel and learn AIML files
kernel = aiml.Kernel()


#kernel.learn("std-startup.xml")
#kernel.respond("load aiml b")

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")


def mov(movie,arg):
    movie.replace(' ', '+')

    url = 'http://www.omdbapi.com/?t=' + movie + '&apikey=4f618851&r=xml'

    tree = ET.parse(urllib.urlopen(url))
    root = tree.getroot()


    movie_dict = {}


    for child in root:
            movie_dict[child.tag] = child.attrib
            #print (child.tag)
            

    #for k,v in movie_dict.items():
     #      print k


    #arg = raw_input("Enter property\n").lower()
    arg = arg.lower()
    
    result = movie_dict['movie'][arg]
    print (result)
    
        
def att_check(query):
    attributes = set(["year", "rating", "release", "runtime", "genre", "director", "writer", "actors", "plot", "language", "country", "awards", "type"])
    querySet = set( query.lower().split() )

    result = (attributes & querySet)
    
    if result:
        return list(result)
    else:
        return -1


def title(query):

    wor = query.split()
    wor1 = wor[::-1]

    ind=-1
    
    for i in wor1:    

        if i=="movie":
            ind=wor1.index(i)
            break

    if ind!=-1:
        title = (wor[len(wor)-ind:len(wor)])
        title_name = " ".join(title)
        return title_name



# Press CTRL-C to break this loop
while True:
    user = raw_input("Enter your message >> ")
    attribs = att_check(user)


    if attribs != -1:
            title_name = title(user)
            #print ("%s of %s" %(attribs[0],title_name))
            mov(title_name, attribs[0])
            continue

    print (kernel.respond(user))
