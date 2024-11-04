import re
import pytest

def convert(s):
    if x := re.search(r"^([0-9]{1,2}|[0-9]{1,2}:[0-5][0-9]) (AM|PM) to ([0-9]{1,2}|[0-9]{1,2}:[0-5][0-9]) (AM|PM)$", s):
        # Loop to check values > 12
        for i in (1, 3):
            if len(x.group(i)) <= 2:
                if int(x.group(i)) > 12:
                    raise ValueError  # X is > 12 when using H
            else:
                if int(x.group(i).split(":")[0]) > 12:
                    raise ValueError  # X is > 12 when using HH:MM
    # if regex format not met raise error
    else:
        raise ValueError

    # default start/end time values, mm to be set below conditionally on format
    start_time = int(x.group(1).split(":")[0])
    end_time = int(x.group(3).split(":")[0])
    start_time_mm = "00"
    end_time_mm = "00"

    # conversion of AM to 24H value except if 12PM
    if x.group(2) == "PM" and start_time != 12:
        start_time += 12
    if x.group(4) == "PM" and end_time != 12:
        end_time += 12

    # preservation of midnight as 12AM
    if x.group(2) == "AM" and start_time == 12:
        start_time -= 12
    if x.group(4) == "AM" and end_time == 12:
        end_time -= 12

    # string prefix of 0 for start/end times <10
    if len(str(start_time)) == 1:
        start_time = "0" + str(start_time)
    if len(str(end_time)) == 1:
        end_time = "0" + str(end_time)

    # minute value handling conditional on length of group
    if len(x.group(1)) > 2:
        start_time_mm = x.group(1).split(":")[1]
        end_time_mm = x.group(3).split(":")[1]

    # final values for start/end time ready for returning
    start_time = str(start_time) + ":" + str(start_time_mm)
    end_time = str(end_time) + ":" + str(end_time_mm)

    return f"{start_time} to {end_time}"


# Test cases
def test_valid_input_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_input_2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_valid_input_3():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_valid_input_4():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_invalid_input_1():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_invalid_input_2():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_input_3():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
