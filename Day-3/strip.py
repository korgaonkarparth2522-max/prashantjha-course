# 1. rstrip() - removes whitespace from the right end of a string
# 2. lstrip() - removes whitespace from the left end of a string
# 3. strip() - removes whitespace from both ends of a string

# programming = input("Enter a programming language: ")
# p_name = programming.strip()
# if p_name == "python":
#     print(p_name)
# elif p_name == "java":
#     print(p_name)
# elif p_name == "c++":
#     print(p_name)
# else:
#     print("Invalid programming language")
    
# convert a 12-hour time string to 24-hour time format
time_12hr = input("Enter time in 12-hour format (e.g., 02:30 PM): ")
time_24hr = time_12hr.strip().upper()
if time_24hr.endswith("AM"):
    time_24hr = time_24hr[:-2]
    if time_24hr.startswith("12"):
        time_24hr = "00" + time_24hr[2:]
elif time_24hr.endswith("PM"):
    time_24hr = time_24hr[:-2]
    if not time_24hr.startswith("12"):
        time_24hr = str(int(time_24hr[:2]) + 12) + time_24hr[2:]
print("Time in 24-hour format:", time_24hr)
 