
def RGBtoHEX(color):        # Expects and returns a color string: either "0,120,255" or "#0078ff"
    # Check format
    if color == None:
        return(color)
    
    elif color[0] == "#" and len(color) == 7:     # Hex to RGB
        color = color.lstrip("#")
        
        rh = int(color[0:2],16)
        gh = int(color[2:4],16)
        bh = int(color[4:6],16)

        rgb = str(rh) + "," + str(gh) +","+ str(bh)

        return(rgb)
        
        # int(color[0:i],16) for i in range(0,6,2)
        
    elif "," in color:      # RGB to hex
        rgblist = color.split(",")
        
        for x in rgblist:
            if not x.isnumeric():
                return(color)
               
        r = int(rgblist[0])
        g = int(rgblist[1])
        b = int(rgblist[2])
        return('#{:02x}{:02x}{:02x}'.format(r,g,b))

    else:                   # Other format or total nonsense
        return(color)
    

def writeLabel(fname='AMBCCFv2022.label', labels=[], split=False):

    if labels:

        header = '''################################################
# ITK-SnAP Label Description File
# File format: 
# IDX   -R-  -G-  -B-  -A--  VIS MSH  LABEL
# Fields: 
#    IDX:   Zero-based index 
#    -R-:   Red color component (0..255)
#    -G-:   Green color component (0..255)
#    -B-:   Blue color component (0..255)
#    -A-:   Label transparency (0.00 .. 1.00)
#    VIS:   Label visibility (0 or 1)
#    IDX:   Label mesh visibility (0 or 1)
#  LABEL:   Label description 
################################################
'''

        lines = []  
        if split:

            for label in labels:
                color = '#' + str(label[1]).rjust(6,'0')                 
                rgb = RGBtoHEX(color).split(",")

                # Left
                label_id = str(int(label[0]) + 50000)
                line = "{:>5}{:>6}{:>5}{:>5}{:>9}{:>3}{:>3}{}".format(label_id, rgb[0], rgb[1], rgb[2], "1", "1", "0", '    "' + label[2] + ' L"')
                lines.append(line)

                # Right
                label_id = str(int(label[0]) + 10000)
                line = "{:>5}{:>6}{:>5}{:>5}{:>9}{:>3}{:>3}{}".format(label_id, rgb[0], rgb[1], rgb[2], "1", "1", "0", '    "' + label[2] + ' R"')
                lines.append(line)

            lines.sort()

        else:
            for label in labels:
                color = '#' + str(label[1]).rjust(6,'0')                 
                rgb = RGBtoHEX(color).split(",")
                line = "{:>5}{:>6}{:>5}{:>5}{:>9}{:>3}{:>3}{}".format(label[0], rgb[0], rgb[1], rgb[2], "1", "1", "0", '    "' + label[2] + '"')
                lines.append(line)

        with open(fname, 'w') as out:
            out.write(header)
            for line in lines:
                out.write(line + "\n")


if __name__ == '__main__':

    labels = []
    with open('AMBCCFv2022_splitAtlas_metadata.csv', 'r') as lf:
        for line in lf:
            labels.append(line.strip().split(';'))

    labels = labels[1:]

    writeLabel(fname='AMBCCFv2022.label', labels=labels, split=False)
    writeLabel(fname='AMBCCFv2022-split.label', labels=labels, split=True)