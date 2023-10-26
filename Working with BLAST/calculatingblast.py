def determine(querypath, queryresults, strainbarcodepath):
 from readingblast import readresults
 from nameIDdict import idname
 from querylengthname import getlength
 import pandas as pd
 import os
 results = readresults(strainbarcodepath, queryresults)
 names = idname(strainbarcodepath)
 querygene, sequencelength = getlength(querypath)
 Presencedict = {name: f"{querygene} is not present" for name in names.keys()}
 for file in os.listdir(queryresults):
    filepath = os.path.join(queryresults, file)
    for name, barcode in names.items():
        if name in file:
            data = results.get(name)
            if data:
                percidentity, percoverlap = float(data[2]), (float(data[3]) / sequencelength) * 100
                if percidentity > 95 and percoverlap > 95:
                    Presencedict[name] = f"{querygene} is present"
                else:
                    Presencedict[name] = f"{querygene} presence is not definitive"
 df = pd.DataFrame(list(Presencedict.items()), columns=['Strain name ', ' Presence'])
 presencefile = "presence.csv"
 df.to_csv(presencefile, index=False, sep= ":")
 return Presencedict





 
       




