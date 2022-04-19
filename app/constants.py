from enum import Enum


class Table(Enum):
    CANDIDATE_TBL = "Candidate_mapping"
    CANDIDATE_DTL_TBL = "Candidates"
    STATE_RESULTS_TBL = "Results"
    STATISTICS_TBL = "Statistics"
    LOCATION_TBL = "Region_location"


class CandidateTableColumn(Enum):
    CANDIDATE_ID = "Candidate ID"
    CANDIDATE_NAME = "Candidate name"
    DISPLAYED_NAME = "Displayed name"


class CandidateDtlTableColumn(Enum):
    CANDIDATE_ID = "Candidate ID"
    CANDIDATE_NAME = "Candidate name"
    GROUP = "Group"
    PARTY = "Party"
    STATUS = "Status"


class StateResultsTableColumn(Enum):
    CANDIDATE_NAME = "Candidate name"
    DEPARTMENT = "Department"
    RESULT_DATE = "Result date"
    REGION = "Region"
    VOTES = "Votes"


class StatisticsTableColumn(Enum):
    DEPARTMENT = "Department"
    RESULT_DATE = "Result date"
    REGION = "Region"
    ABSTENTIONS = "Abstentions"
    BLANK_VOTES = "Blank ballots"
    NULL_VOTES = "Null ballots"
    REGISTERED_VOTERS = "Registered voters"
    TURNOUT = "Turnout"
    VALID_VOTES = "Valid votes"


class LocationTableColumn(Enum):
    REGION = "Region"
    LATITUDE = "Latitude"
    LONGITUDE = "Longitude"


class Cube(Enum):
    ELECTION_CUBE = "Election"


class ElectionCubeHierarchy(Enum):
    RESULT_DATE = "Result date"
    REGION = "Region"
    DEPARTMENT = "Department"
    CANDIDATE_NAME = "Candidate name"


class ElectionCubeLevel(Enum):
    RESULT_DATE = ElectionCubeHierarchy.RESULT_DATE.value
    REGION = ElectionCubeHierarchy.REGION.value
    DEPARTMENT = ElectionCubeHierarchy.DEPARTMENT.value
    CANDIDATE_NAME = ElectionCubeHierarchy.CANDIDATE_NAME.value


class ElectionCubeMeasure(Enum):
    NUM_DEPARTMENTS = "Number of departments"
    NUM_REGIONS = "Number of regions"
    LONGITUDE = "Longitude"
    LATITUDE = "Latitude"

    VOTES = "Votes"
    TOTAL_VOTES_DEPARTMENTS = "Total votes across departments"
    TOTAL_REG_VOTERS = "Total registered voters"
    TOTAL_VALID_VOTES = "Total valid votes"
    TOTAL_BLANK_VOTES = "Total blank ballots"
    TOTAL_NULL_VOTES = "Total null ballots"
    TOTAL_ABSTENTIONS = "Total abstentions"
    TOTAL_INVALID_VOTES = "Total invalid votes"

    # Percentage
    PERCENT_REG_VOTES = "% votes against reg. votes"
    PERCENT_VALID_VOTES = "% valid vote"
    PERCENT_BLANK_VOTES = "% blank ballots"
    PERCENT_NULL_VOTES = "% null ballots"
    PERCENT_ABSTENTIONS = "% abstentions"
    PERCENT_INVALID = "% invalid votes"

    WINNING_CANDIDATE = "Winning candidates"
    WINNING_VOTES = "Winning votes"


# class ElectionCubeHierarchy(Enum):
#     BIKE_TYPE = StationStatusTableColumn.BIKE_TYPE.value
#     LOCATION = "Location"
#     STATION = "Station"


# class StationCubeBikeTypeLevel(Enum):
#     BIKE_TYPE = StationCubeHierarchy.BIKE_TYPE.value


# class StationCubeLocationLevel(Enum):
#     DEPARTMENT = StationDetailsTableColumn.DEPARTMENT.value
#     CITY = StationDetailsTableColumn.CITY.value
#     POSTCODE = StationDetailsTableColumn.POSTCODE.value
#     STREET = StationDetailsTableColumn.STREET.value
#     HOUSE_NUMBER = StationDetailsTableColumn.HOUSE_NUMBER.value


# class StationCubeStationLevel(Enum):
#     NAME = StationDetailsTableColumn.NAME.value
#     ID = StationDetailsTableColumn.ID.value


# class StationCubeMeasure(Enum):
#     CAPACITY = StationDetailsTableColumn.CAPACITY.value
#     BIKES = StationStatusTableColumn.BIKES.value
