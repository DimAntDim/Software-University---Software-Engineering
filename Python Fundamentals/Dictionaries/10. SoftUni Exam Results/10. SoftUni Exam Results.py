students = {}
results = {}
language_submissions_counter = {}

while True:
    # ------------------data read------------------------------------
    data = input()
    if data == 'exam finished':
        break
    data = data.split('-')
    if data[1] != 'banned':
        user = data[0]
        language = data[1]
        points = int(data[2])
    # ---------Counter for Languages submission-----------------------
        if language not in language_submissions_counter:
            language_submissions_counter[language] = 0
        language_submissions_counter[language] += 1
    # ----------------------------------------------------------------
    # ----------Main body, add user and points to languages in dict---
        if language not in students:
            students[language] = {}
        if user not in students[language]:
            students[language][user] = points   # create nested dict for the users
        else:
            for k, v in students[language].items():
                current_points = v
                if k == user and current_points < points:
                    students[language][user] = points
    # ---------------------------------------------------------------
    # ----------If there is a student ban ---------------------------
    else:
        user = data[0]
        for s in students:
            for i in students[s].copy():
                if i == user:
                    students[s].pop(i)
    # ---------------------------------------------------------------
    # ------Separating only users with they results in new dict------
for k, v in students.items():
    for st, points in v.items():
        results[st] = points
    # ---------------------------------------------------------------
    # ---------------sorting result dict-----------------------------
order_results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
# -------------------------------------------------------------------
# ---------------print out user results -----------------------------
print('Results:')
for k, v in order_results.items():
    print(f"{k} | {v}")
    # ---------------print out submissions for different languages---
print('Submissions:')
language_submission_sort = dict(sorted(language_submissions_counter.items(), key=lambda x: (-x[1], x[0])))
for k, v in language_submission_sort.items():
    print(f"{k} - {v}")
    # ---------------------------------------------------------------
