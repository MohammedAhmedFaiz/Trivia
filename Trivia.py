print('Hello, welcome to trivia')

ans = input('Are you ready to play? (yes/no): ')
score = 0 
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. Whats the best programming language?')
    if ans.lower() == 'python':
        score += 1 
        print('Correct')
    else:
        print('Incorrect')


    ans = input('2. What is 2 + 3 - 2?')
    if ans == '3':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


print('Thank you for playing! You got', score, "questions correct")
mark = (score/total_q) * 100

print("Mark: ", mark)
print('Goodbye')