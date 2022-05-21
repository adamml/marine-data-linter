import csv

def test_102_latitude_longitude_is_earth_valid(inputfile, latitude, longitude):
    """Test if each latitude is between -90 and 90 and each longitude is
    between -180 and 180"""
    try:
        if latitude and longitude:
            with open(inputfile) as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for i, row in enumerate(csvreader):
                    if i> 0:
                        if float(row[int(latitude)-1]) < -90 or \
                                float(row[int(latitude)-1]) > 90 or \
                                float(row[int(longitude)-1]) < -180 or \
                                float(row[int(longitude)-1]) > 180:
                            raise ValueError
    except ValueError:
        assert False, ("ValueError: Latitude or Longitude are not Earth" +
                       "coordinates on row {}".format(i+1))