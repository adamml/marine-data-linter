import csv
import json
import urllib.request

def test_103_depth(inputfile, depth, depthmargin, depthmonotonic, latitude, longitude):
    """Test if the depth for a row is, within a given margin, less than the
    depth reported for the location by the EMODnet Bathymetry Web Service"""
    
    if depthmonotonic == "True":
        depthmonotonic = True
    else:
        depthmonotonic = False
    try:
        with open(inputfile) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for i, row in enumerate(csvreader):
                if i> 0:
                    with urllib.request.urlopen("https://rest." +
                                                "emodnet-bathymetry.eu/" +
                                                "depth_sample?" +
                                                "geom=POINT({}%20{})".format(longitude,
                                                                             latitude)) as emodnet_depth:
                        web_depth = json.loads(emodnet_depth.read().decode("utf-8"))
                    if depthmargin.find("%") > -1:
                        if float(row[int(depth)-1]) > web_depth['avg'] * (1 + (int(int(depthmargin[:-1])) / 100)):
                            raise ValueError
                    else:
                        if float(row[int(depth)-1]) > web_depth['avg'] + float(depthmargin):
                            raise ValueError
                    if depthmonotonic:
                        if i > 1:
                            if float(row[int(depth)-1]) < last_depth:
                                raise TypeError
                    last_depth = float(row[int(depth)-1])

    except ValueError:
        assert False, ("Depth for row {} is deeper than EMODnet depth, " +
                       "taking into account a margin of {}").format(i+1, 
                                                                    depthmargin)
    except TypeError:
        assert False, "Depth not monotonic at row {})".format(i+1)