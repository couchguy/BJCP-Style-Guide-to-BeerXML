import xml.etree.ElementTree as ET


# lets read the xml file
tree = ET.parse('styleguide.xml')
root = tree.getroot()

styles = []
styleDict = {"VERSION": "1", "STYLE_GUIDE": "BJCP 2015", "TYPE": "UNKNOWN"}

catname = ""
catnum = ""
name = ""
styleletter = ""
profile = ""
ingredients = ""
examples = ""
notes = ""
oghigh = ""
oglow = ""
fghigh = ""
fglow = ""
ibuhigh = ""
ibulow = ""
srmhigh = ""
srmlow = ""
abvlow = ""
abvhigh = ""

for category in root.iter('category'):
    catnum = category.attrib["id"]
    for catChild in  category.getchildren():
        if catChild.tag == "name":
            catname = catChild.text
        if catChild.tag == "subcategory":
            styleDict["CATEGORY"] = catname
            styleDict["CATEGORY_NUMBER"] = catnum
            styleletter = catChild.attrib["id"].split(catnum)[1]
            styleDict["STYLE_LETTER"] = styleletter
            profile = ""
            for beer in catChild.getchildren():
                if(beer.tag == "name"):
                    styleDict["name"] = beer.text
                    name = beer.text

                if(beer.tag == "aroma"):
                    profile = profile + "\nAroma: " + beer.text
                    styleDict["PROFILE"] = profile
                if(beer.tag == "flavor"):
                    profile = profile + "\nFlavor: " + beer.text
                    styleDict["PROFILE"] = profile
                if(beer.tag == "mouthfeel"):
                    profile = profile + "\nMouthfeel: " + beer.text
                    styleDict["PROFILE"] = profile
                if(beer.tag == "appearance"):
                    profile = profile + "\nAppearance: " + beer.text
                    styleDict["PROFILE"] = profile

                if(beer.tag == "impression"):
                    notes = beer.text
                    styleDict["NOTES"] = notes

                if(beer.tag == "ingredients"):
                    ingredients = beer.text
                    styleDict["INGREDIENTS"] = ingredients

                if(beer.tag == "examples"):
                    examples = beer.text
                    styleDict["EXAMPLES"] = examples

                if(beer.tag == "stats"):
                    for stat in beer.getchildren():
                        if(stat.tag == "og"):
                            for og in stat.getchildren():
                                if(og.tag == "high"):
                                    oghigh = og.text
                                    styleDict["OG_MAX"] = oghigh
                                if(og.tag == "low"):
                                    oglow = og.text
                                    styleDict["OG_MIN"] = oglow
                        if(stat.tag == "fg"):
                            for fg in stat.getchildren():
                                if(fg.tag == "high"):
                                    fghigh = fg.text
                                    styleDict["FG_MAX"] = fghigh
                                if(fg.tag == "low"):
                                    fglow = fg.text
                                    styleDict["FG_MIN"] = fglow
                        if(stat.tag == "ibu"):
                            for ibu in stat.getchildren():
                                if(ibu.tag == "high"):
                                    ibuhigh = ibu.text
                                    styleDict["IBU_MAX"] = ibuhigh
                                if(ibu.tag == "low"):
                                    ibulow = ibu.text
                                    styleDict["IBU_MIN"] = ibulow
                        if(stat.tag == "srm"):
                            for srm in stat.getchildren():
                                if(srm.tag == "high"):
                                    srmhigh = srm.text
                                    styleDict["COLOR_MAX"] = srmhigh
                                if(srm.tag == "low"):
                                    srmlow = srm.text
                                    styleDict["COLOR_MIN"] = srmlow
                        if(stat.tag == "abv"):
                            for abv in stat.getchildren():
                                if(abv.tag == "high"):
                                    abvhigh = abv.text
                                    styleDict["ABV_MAX"] = abvhigh
                                if(abv.tag == "low"):
                                    abvlow = srm.text
                                    styleDict["ABV_MIN"] = abvlow

#            print(name)                             # NAME
#            print("1")                              # VERSION
#            print(catname)                          # CATEGORY
#            print(catnum)                           # CATEGORY_NUMBER
#            print(styleletter)                      # STYLE_LETTER
#            print("BJCP 2015")                      # STYLE_GUIDE
#            print("Ale Lager")                      # TYPE
#            print(oglow)                            # OG_MIN
#            print(oghigh)                           # OG_MAX
#            print(fglow)                            # FG_MIN
#            print(fghigh)                           # FG_MAX
#            print(ibulow)                           # IBU_MIN
#            print(ibuhigh)                          # IBU_MAX
#            print(srmlow)                           # COLOR_MIN
#            print(srmhigh)                          # COLOR_MAX
#            print(abvhigh)                          # ABV_MAX
#            print(abvlow)                           # ABV_MIN
#            print(notes)                            # NOTES
#            print(profile[1:])                      # PROFILE - Aroma, Flavor, Mouthfeel, Appearance, Impression
            styleDict["profile"] = profile[1:]
#            print(ingredients)                      # INGREDIENTS
#            print(examples)                         # EXAMPLES
#            print(oglow + " SG")                    # DISPLAY_OG_MIN
            styleDict["DISPLAY_OG_MIN"] = oglow + " SG"
#            print(oghigh + " SG")                   # DISPLAY_OG_MAX
            styleDict["DISPLAY_OG_MAX"] = oghigh + " SG"
#            print(fglow + " SG")                    # DISPLAY_FG_MIN
            styleDict["DISPLAY_FG_MIN"] = fglow + " SG"
#            print(fghigh + " SG")                   # DISPLAY_FG_MAX
            styleDict["DISPLAY_FG_MAX"] = fghigh + " SG"
#            print(srmlow + " SRM")                  # DISPLAY_COLOR_MIN
            styleDict["DISPLAY_COLOR_MIN"] = srmlow + " SRM"
#            print(srmhigh + " SRM")                 # DISPLAY_COLOR_MAX
            styleDict["DISPLAY_COLOR_MAX"] = srmhigh + " SRM"
#            print(oglow + "-" + oghigh + " SG")     # OG_RANGE
            styleDict["OG_RANGE"] = oglow + "-" + oghigh + " SG"
#            print(fglow + "-" + fghigh + " SG")     # FG_RANGE
            styleDict["FG_RANGE"] = fglow + "-" + fghigh + " SG"
#            print(ibulow + "-" + ibuhigh + " IBUs") # IBU_RANGE
            styleDict["IBU_RANGE"] = ibulow + "-" + ibuhigh + " IBUs"
#            print(srmlow + "-" + srmhigh + " SRM")  # COLOR_RANGE
            styleDict["COLOR_RANGE"] = srmlow + "-" + srmhigh + " SRM"
#            print(abvlow + "-" + abvhigh + " %")    # ABV_RANGE
            styleDict["ABV_RANGE"] = abvlow + "-" + abvhigh + " %"
#            print("---------------------------")

            if("Ale" in name or "Stout" in name or "IPA" in name or "Porter" in name):
                styleDict["TYPE"] = "Ale"
            elif("Lager" in name or "Bock" in name or "bock" in name or "Helles" in name or "Pils" in name):
                styleDict["TYPE"] = "Lager"
            elif("Mead" in name or "Mead" in catname):
                styleDict["TYPE"] = "Mead"
            elif("Cider" in name or "Cider" in catname):
                styleDict["TYPE"] = "Cider"

            else:
                styleDict["TYPE"] = "UNKNOWN"
            styles.append(styleDict.copy())

#print(len(styles))
f = open("2018styles.xml", "w+")
f.write('<?xml version="1.0" encoding="iso-8859-1"?>\n<STYLES>\n')
for style in styles:
    f.write("     <STYLE>\n")
    f.write("          <NAME>%s</NAME>\n" % (style["name"]))
    f.write("          <VERSION>%s</VERSION>\n" % (style["VERSION"]))
    f.write("          <CATEGORY>%s</CATEGORY>\n" % (style["CATEGORY"]))
    f.write("          <CATEGORY_NUMBER>%s</CATEGORY_NUMBER>\n" % (style["CATEGORY_NUMBER"]))
    f.write("          <STYLE_LETTER>%s</STYLE_LETTER>\n" % (style["STYLE_LETTER"]))
    f.write("          <STYLE_GUIDE>%s</STYLE_GUIDE>\n" % (style["STYLE_GUIDE"]))
    f.write("          <TYPE>%s</TYPE>\n" % (style["TYPE"]))
    f.write("          <OG_MIN>%s</OG_MIN>\n" % (style["OG_MIN"]))
    f.write("          <OG_MAX>%s</OG_MAX>\n" % (style["OG_MAX"]))
    f.write("          <FG_MIN>%s</FG_MIN>\n" % (style["FG_MIN"]))
    f.write("          <FG_MAX>%s</FG_MAX>\n" % (style["FG_MAX"]))
    f.write("          <IBU_MIN>%s</IBU_MIN>\n" % (style["IBU_MIN"]))
    f.write("          <IBU_MAX>%s</IBU_MAX>\n" % (style["IBU_MAX"]))
    f.write("          <COLOR_MIN>%s</COLOR_MIN>\n" % (style["COLOR_MIN"]))
    f.write("          <COLOR_MAX>%s</COLOR_MAX>\n" % (style["COLOR_MAX"]))
    f.write("          <ABV_MAX>%s</ABV_MAX>\n" % (style["ABV_MAX"]))
    f.write("          <ABV_MIN>%s</ABV_MIN>\n" % (style["ABV_MIN"]))
    f.write("          <CARB_MIN>1.500</CARB_MIN>\n")
    f.write("          <CARB_MAX>3.000</CARB_MAX>\n")
    f.write("          <NOTES>%s</NOTES>\n" % (style["NOTES"]))
    f.write("          <PROFILE>%s</PROFILE>\n" % (style["PROFILE"][1:]))
    f.write("          <INGREDIENTS>%s</INGREDIENTS>\n" % (style["INGREDIENTS"]))
    f.write("          <EXAMPLES>%s</EXAMPLES>\n" % (style["EXAMPLES"]))
    f.write("          <DISPLAY_OG_MIN>%s</DISPLAY_OG_MIN>\n" % (style["DISPLAY_OG_MIN"]))
    f.write("          <DISPLAY_OG_MAX>%s</DISPLAY_OG_MAX>\n" % (style["DISPLAY_OG_MAX"]))
    f.write("          <DISPLAY_FG_MIN>%s</DISPLAY_FG_MIN>\n" % (style["DISPLAY_FG_MIN"]))
    f.write("          <DISPLAY_FG_MAX>%s</DISPLAY_FG_MAX>\n" % (style["DISPLAY_FG_MAX"]))
    f.write("          <DISPLAY_COLOR_MIN>%s</DISPLAY_COLOR_MIN>\n" % (style["DISPLAY_COLOR_MIN"]))
    f.write("          <DISPLAY_COLOR_MAX>%s</DISPLAY_COLOR_MAX>\n" % (style["DISPLAY_COLOR_MAX"]))
    f.write("          <OG_RANGE>%s</OG_RANGE>\n" % (style["OG_RANGE"]))
    f.write("          <FG_RANGE>%s</FG_RANGE>\n" % (style["FG_RANGE"]))
    f.write("          <IBU_RANGE>%s</IBU_RANGE>\n" % (style["IBU_RANGE"]))
    f.write("          <COLOR_RANGE>%s</COLOR_RANGE>\n" % (style["COLOR_RANGE"]))
    f.write("          <ABV_RANGE>%s</ABV_RANGE>\n" % (style["ABV_RANGE"]))
    f.write("          <CARB_RANGE>1.50-3.0 Vols</CARB_RANGE>\n")
    f.write("     </STYLE>\n")
f.write("</STYLES>")
f.close()
