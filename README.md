# Marine Data Linter

A Python based linter for marine science data files.

## Introduction

## Expected file format

An ISO 8859-1 Comma Separated Value (CSV) file. with one header line

## Dependencies

- `pytest`

## Usage

The linter is run by pytest.

```console
cd marine-data-linter
pytest
```

e.g.

```console
pytest --inputfile ./resources/pass_very_basic.csv --date 1 --latitude 2 --longitude 3 --depth 4

pytest --inputfile ./resources/IMI_CTD_7834_50bf_4641.csv --datetime 24 --depth 25 --latitude 26 --longitude 27 --depthmonotonic
```

## Flags

A number of flags are used to configure the linter. Where a column number is specified, columns are indexed starting with `1` (as in Excel or OpenOffice Calc).

### File to check

* `--input-file` Points to the data file to be linted, e.g. `--inputfile ./resources/pass_very_basic.csv`

### Date/Datetime/Time

* `--date` Specifies the column of the input file in which an observation or measurement date is specified, e.g. `--date 1`
* `--datetime` Specifies the column of the input file in which an observation or measurement date/time is specified, e.g. `--datetime 1`
* `--time` Specifies the column of the input file in which an observation or measurement time is specified, e.g. `--time 1`

### Positional - Latitude, Longitude and Depth

* `--latitude` Specifies the column of the input file in which an observation or measurement latitude in a global Coordinate Reference System (e.g. WGS84) is specified, e.g. `--latitude 2`
* `--longitude` Specifies the column of the input file in which an observation or measurement latitude in a global Coordinate Reference System (e.g. WGS84) is specified, e.g. `--longitude 3`
* `--depth` Specifies the column of the input file in which an observation or measurement depth in metres is specified (positive values are deeper in the ocean) e.g. `--depth 4`
* `--depthmargin` Specifies a margin of error to use in validation of each depth record, either in absolute or metres or as a percentage of the depth, e.g. `--depth-marign 10` for 10 metres or `--depth-margin 10%` for 10% of the water column depth. Depths are checked against the EMODnet Bathymetry web service
* `--depthmonotonic` Specifies that the depths in a data file should increase through the datafile, for example for a processed CTD cast e.g. `--depthmonotonic True`

### Other paramters

* `--watertemperature` Specifies the column of water temperature measurements made in degrees C, e.g. `--watertemperature 5`
* `--salinity` Specifies the column of salinity measurements (dimensionless), e.g. `--salinity 6`

## Tests run

1. A Date column is identified by a `--date` or a `--datetime`flag
    1. Date - If a `--date`, `--datetime`, or a `--time` flag is set, all dates/datetime/times in the specified column must be strings conforming to ISO8601
1. A Latitude column is identified by a `--latitude` flag
1. A Longitude column is identified by a `--longitude` flag
1. A Depth column is identified by a `--depth` flag
    1. Depth is checked against the EMODnet Bathymetry web service to ensure it is realistic
    1. Depth can have a margin of error against the EMODnet Bathymethry web service specified by `--depthmargin` 
    1. Depth can be tested to be continuously increasing, specified by `--depthmonotonic`
1. Location - If both `--latitude` and `--longitude` flags are specified, the location must be Earth valid coordinates (latitude between -90 and 90, longitude between -180 and 180)
1. UNESCO GTSPP Real-Time Quality Control Checks for:
    1. Water Temperature
    1. Salinity