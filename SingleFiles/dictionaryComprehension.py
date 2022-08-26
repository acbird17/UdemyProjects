
# -------------------------------------------

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }

# convert = {day:((temp + 9/5) + 32) for (day, temp) in weather_c.items()}

# print(convert)


# ---------------------------------------

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# word_count = {word:len(word) for word in sentence.split()}

# print(word_count)

# ------------------------------------------
# import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# student_scores = {student:random.randint(1,100) for student in names}

# passed_student = {student:score for (student, score) in student_scores.items() if score >= 60}

# print(passed_student)