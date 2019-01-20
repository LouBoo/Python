score_list = []
i = 0

while i < 7:
    try:
        score = float(input("Please enter a test score between 0 and 100: "))
        if score >= 0 and score <= 100:
            score_list.append(score)
            i = i + 1
        else:
            print("Input Error! Please enter a nonnegative number between 0 and 100.")
    except ValueError:
        print("Input Error! Please enter a number between 0 and 100.")

score_list.sort()
score_list = score_list[1:]
avg_score = (sum(score_list) / len(score_list))

if avg_score < 60:
    print("%.2f%% is an F" %avg_score)
elif avg_score < 70:
    print("%.2f%% is a D" %avg_score)
elif avg_score < 80:
    print("%.2f%% is a C" %avg_score)
elif avg_score < 90:
    print("%.2f%% is a B" %avg_score)
else:
    print("%.2f%% is an A" %avg_score)
