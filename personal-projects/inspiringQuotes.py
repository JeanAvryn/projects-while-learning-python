# Inspiring Quotes


print("Instructions: Write your name in the first line, and then write your age in the second line. If you do not want to write your name, leave the first line blank.")

print()
print()

name = input()
age = int(input())

print("This is LIFE!")
print()
print("If your age is:", str(age))
print("Here's a message for you!")
print()

print("Hello there, " + name + "!")

print()

if age == 0:
 print("   Goodluck on your journey in life!")

elif age == 1:
 print("   Wow, hello there! You reached your first year!")

elif age <= 12:
 print("   Congratulations! Enjoy the fun and happy memories of childhood before entering adolescence. Remember to always respect your parents, have fun with friends and prioritize your studies! Enjoy it while it lasts!")

elif age <= 19:
 print("   This stage might be stressful. You might be facing acne, hormones and many more. You might be beginning to find your love of your life, or you're fighting with your parents. Remember, it's okay. It is a part of your life. Just always know that the exciting parts are coming! Teenage years will always be what you will remember later on.")

elif age <= 40:
 print("   Ah, exciting parts eh? Paying bills, facing midlife crisis, or even having debts. Having your first baby, or your wedding is upcoming? Parents getting older, siblings becoming much more of a burden? Wanna go back to your teenage years? Ah, there's no going back. You must face this. You already faced " + str(age) + " years of battle, you've already come this far. Why give up now?!")

elif age <= 99:
 print("   Congratulations, " + name + "! " + "You've made it this far! Reaching the age of "+ str(age) + " is really impressing, considering the fact that a lot don't really reach this age. You may have lived a beautiful life, or a not-so good one, but I am proud that I have the chance to talk to you in this way! I hope you are living well right now. Enjoy the remaining years of your life!")

else:
 print("   Wow, you are either so young, or so old!")

print()
print("   Life is worth living for. Go for it!")
