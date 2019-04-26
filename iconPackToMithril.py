import glob
import errno

print('Executing Script')
print('Opening File')
#Path to write the mithrilfile
fileWrite_Path = './scripts/drawModule/mithrilIcons.js'
#Path to the iconpack
image_path = './images/iconpack/*.png'
files = glob.glob(image_path)
spacer = '     '
quadSpacer = spacer + spacer + spacer + spacer
nameList = ''
#manual counter, Count \n to figure out number of lines.
lineCounter = 0

#writes the header
nameList += '//Autogenerated Mithril Mount for icons.' + '\n'
nameList += '//This code was generated with iconPackToMithril.py' + '\n'
nameList += 'const iconTools =' + '\n'
nameList += '{' + '\n'
nameList += spacer + 'view: function()' + '\n' 
nameList += spacer + '{' + '\n'
nameList += spacer + spacer + 'return m("div",' + '\n'
nameList += spacer + spacer + '{"id":"icontools"},'+ '\n'
nameList += spacer + spacer + '['+ '\n'
nameList += spacer + spacer + spacer + 'm("div",' + '\n' 
nameList += spacer + spacer + spacer + '{"id":"iconContainer"}, ' + '\n'
nameList += spacer + spacer + spacer + '[' + '\n'

#manual header count, change if header changes.
lineCounter += 12
fileCounter = 0

#runs through all the images in iconpack and writes them to a mithrilformated JS file.
for name in files:
    try:
        nameOutput = ""
        fileCounter += 1
        currentName = name.split('\\',1)[1]
        nameOutput += quadSpacer + '//Icon Number:' + str(fileCounter) + ' Name:' + currentName + '\n' 
        currentName = currentName.split('.png', 1)[0]
        nameOutput += quadSpacer + 'm("img",' + '\n'
        nameOutput += quadSpacer + '{' + '\n'
        nameOutput += quadSpacer + spacer + '"src":"images/iconpack/' + currentName + '.png",' + '\n'
        nameOutput += quadSpacer + spacer + '"class":"drawIcons",' + '\n'
        nameOutput += quadSpacer + spacer + '"id":"markerIcon-' + currentName + '",' + '\n'
        nameOutput += quadSpacer + spacer + '"title":"' + currentName + '",' + '\n'
        nameOutput += quadSpacer + spacer + 'onclick: (e) =>' + '\n' 
        nameOutput += quadSpacer + spacer + '{markerIcons_click(e)}' + '\n'
        nameOutput += quadSpacer +'}),' + '\n'
        nameList += nameOutput

        #Manually counted lines added per icon, Change with changes made.
        lineCounter += 10
    except IOError as exc:
        print(exc)
#Adds bracket and spaceing.
nameList += spacer + spacer + spacer + '])' + '\n'
nameList += spacer + spacer + '])' + '\n'
nameList += spacer + '}' + '\n'
nameList += '}' 

#Counting the ending brackets
lineCounter +=4

#Writes the icons to File
writeToFile = open(fileWrite_Path,'w')
writeToFile.write(nameList)
print('Done writing to file. ' + str(lineCounter) + ' lines written. ' + str(fileCounter) + ' Icons Added.')
print('File Closing')
writeToFile.close()
print('Script Closing.')