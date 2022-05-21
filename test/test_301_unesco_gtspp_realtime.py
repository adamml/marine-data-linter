import csv

def test_301_unesco_gtspp_realtime(inputfile,
                                   salinity,
                                   watertemperature):
    """Follows the UNESCO GTSPP Real-Time Quality Control manual (2010) to 
    check the range of the following parameters:
    
        - salinty (dimensionless: min: 0; max: 41)
        - water temperature (deg C.: min: -2, max: 40)
    """
    try:
        with open(inputfile) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for i, row in enumerate(csvreader):
                if i> 0:
                    if salinity:
                        param = "Salinity"
                        if float(row[int(salinity) -1]) < 0 or float(row[int(salinity) -1]) > 41:
                            raise ValueError
                    if watertemperature:
                        param = "WaterTemperature"
                        if float(row[int(watertemperature) -1]) < -2 or float(row[int(watertemperature) -1]) > 40:
                            raise ValueError
    except:
        assert False, "{} outside range on row {}...".format(param, i+1)