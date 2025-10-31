import time

print("🤖 Welcome to SmartTalk AI!")
time.sleep(1)

name = input("✨ What's your name? ")
print(f"Hello {name}! Nice to meet you 💖")
time.sleep(1)

mood = input("How are you feeling today (happy/sad/angry/okay)? ").lower()

if mood == "happy":
    print("That's wonderful! Keep shining 😍")
elif mood == "sad":
    print("Oh no! Don’t worry, {name}. Everything will be fine 💪")
elif mood == "angry":
    print("Take a deep breath... calm mind = strong soul 🌿")
else:
    print("Got it! Always stay positive ✨")

time.sleep(1)
print()
print("Let's chat a bit more! 💬")
time.sleep(1)

interest = input("What do you want to learn today (Python/AI/Web)? ").lower()

if interest == "python":
    print("Python is amazing! You can build AI, apps, and automation scripts 🐍")
elif interest == "ai":
    print("AI is the future! Smart choice 🤖✨")
elif interest == "web":
    print("Web development is super fun! You can design cool websites 🌐")
else:
    print("Nice! Learning something new is always great 🚀")

time.sleep(1)
print()
print(f"It was awesome chatting with you, {name}! Have a great day 💫")
