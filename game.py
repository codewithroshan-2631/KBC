questions = [
    ["which language was used to created Facebook ?", "Pyton", "Javascript", "French", "php", "None", 4],
    ["Parnadatta was appointed the Provincial Governor of Saurashtra by __?", "Chandragupta Maurya", "Rudradaman", "Chandragupta II", "Skandagupta", "None", 4],
    ["The title “Paramasaugata” was adopted by ___ ?", "Bhaskar Varman", "Shashanka", "Rajya Vardhana", "Harsha", "None", 4],
    ["What is the sum of 130+125+191?", "335", "456", "446", "426", "None", 4],
    ["The title “Paramasaugata” was adopted by ___ ?", "Bhaskar Varman", "Shashanka", "Rajya Vardhana", "Harsha", "None", 4],
    ["What is the sum of 130+125+191?", "335", "456", "446", "426", "None", 4],
    ["which language was used to created Facebook ?", "Pyton", "Javascript", "French", "php", "None", 4],
    ["Parnadatta was appointed the Provincial Governor of Saurashtra by __?", "Chandragupta Maurya", "Rudradaman", "Chandragupta II", "Skandagupta", "None", 4],
    ["which language was used to created Facebook ?", "Pyton", "Javascript", "French", "php", "None", 4],
    ["Parnadatta was appointed the Provincial Governor of Saurashtra by __?", "Chandragupta Maurya", "Rudradaman", "Chandragupta II", "Skandagupta", "None", 4],
    ["The title “Paramasaugata” was adopted by ___ ?", "Bhaskar Varman", "Shashanka", "Rajya Vardhana", "Harsha", "None", 4],
    ["What is the sum of 130+125+191?", "335", "456", "446", "426", "None", 4],
    ["The title “Paramasaugata” was adopted by ___ ?", "Bhaskar Varman", "Shashanka", "Rajya Vardhana", "Harsha", "None", 4],
    ["What is the sum of 130+125+191?", "335", "456", "446", "426", "None", 4],
    ["which language was used to created Facebook ?", "Pyton", "Javascript", "French", "php", "None", 4],
    ["Parnadatta was appointed the Provincial Governor of Saurashtra by __?", "Chandragupta Maurya", "Rudradaman", "Chandragupta II", "Skandagupta", "None", 4]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 7000000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"{question[0]}")  # <-- This line shows the question
    print(f"A. {question[1]}   B. {question[2]}")
    print(f"C. {question[3]}   D. {question[4]}")
    
    try:
        reply = int(input("Enter your answer (1-4): "))
    except ValueError:
        print("Invalid input! Exiting game.")
        break

    if reply == question[-1]:
        print(f"Correct answer, you have won Rs.{levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is Rs.{money}")
