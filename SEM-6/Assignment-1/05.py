import re
class Time:
    def __init__(self, time_str):
        self.time_str = time_str

    def is_valid_time(self):
        pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$"
        return bool(re.match(pattern, self.time_str))

    def convert_to_12_hour(self):
        if not self.is_valid_time():
            return "Invalid time format. Please use HH:MM:SS (24-hour format)."

        hours, minutes, seconds = map(int, self.time_str.split(":"))
        period = "AM" if hours < 12 else "PM"
        hours = hours % 12 or 12
        return f"{hours:02}:{minutes:02}:{seconds:02} {period}"
    
time_input = input("Enter time in 24-hour format (HH:MM:SS): ")
time_obj = Time(time_input)

if time_obj.is_valid_time():
    print("Converted Time:", time_obj.convert_to_12_hour())
else:
    print("Invalid time format. Please enter HH:MM:SS in 24-hour format.")
