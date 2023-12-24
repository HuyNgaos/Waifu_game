import string

class Interface():
    def cleanup(teststr):
       cleaningtable1 = str.maketrans('','',string.punctuation) #remove puctuation
       cleanpuc = teststr.translate(cleaningtable1)
       cleaningtable2 = str.maketrans('','',' ') #remove space
       cleanspc = cleanpuc.translate(cleaningtable2)
       cleanstr = cleanspc.lower() #convert to lowercase
       return cleanstr
    
