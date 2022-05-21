import csv

import datetime

def test_101_date_is_iso(inputfile, date, dattim, time):
    """Test that the date, datetime and time columns as supplied are 
    formatted as ISO8601 strings"""

    try:
        if date is not None:
            with open(inputfile) as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for i, row in enumerate(csvreader):
                    if i> 0:
                        datetime.datetime.strptime(row[int(date) - 1], '%Y-%m-%d')
            
        if dattim is not None:
            with open(inputfile) as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for i, row in enumerate(csvreader):
                    if i> 0:
                        datetime.datetime.strptime(row[int(dattim) - 1], '%Y-%m-%dT%H:%M:%S%z')
        
        if time is not None:
            with open(inputfile) as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for i, row in enumerate(csvreader):
                    if i> 0:
                        datetime.datetime.strptime(row[int(time) - 1], '%Y-%m-%dT%H:%M:%S%z')
    
    except ValueError as e:
        assert False,\
               "ValueError in testing date/ datetimetime / time at row {}".format(i+1)
