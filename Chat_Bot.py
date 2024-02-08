print('''Hello User!
      I am a chat bot. My name is Jarvis.''')

name = input("May I know your name? ")  # You should use the input function correctly

print("OK, " + name + "!")  # Make sure to call the input function to get the user's name

print('''My creater's name is Noor ul Husnain.
      He is a programmer who rcently learn some python basics.
      Using these basic skills he creted me.
      I ask you smoe simple questions.''')

questions = [
    "How old are you, " + name + "?\n",
    "In which class do you study, " + name + "?\n",
    "Do you know Python, " + name + "?\n",
    "Do you know HTML, " + name + "?\n"
]

for q in questions:
    user_response = input(q)
    
    if user_response.lower() == "yes":
        print("Oh! that's great")
    elif user_response.lower() == "no":
        print("Oh! that's OK")
    else:
        print("Oh! that's " + user_response)


print("Which shape would you like me to create?")
shapeName = input("Choose one: Square, Circle, Rectangle, Pentagon or Special:\n ")

import turtle

mouse = turtle.Turtle()

if shapeName.capitalize() == "Square":
    print("OK " + shapeName)
    for _ in range(4):
        mouse.forward(50)
        mouse.left(90)
elif shapeName.capitalize() == "Circle":
    print("OK " + shapeName)
    for _ in range(400):
        mouse.forward(2)
        mouse.left(1)
elif shapeName.capitalize() == "Rectangle":
    print("OK " + shapeName)
    for _ in range(2):
        mouse.forward(100)
        mouse.left(90)
        mouse.forward(50)
        mouse.left(90)
elif shapeName.capitalize() == "Pentagon":
    print("OK " + shapeName)
    for _ in range(5):
        mouse.forward(50)
        mouse.left(72)
elif shapeName.capitalize() == "Special":
    s=turtle.Screen()
    s.bgcolor('black')
    mouse.width(3)
    mouse.speed(70)
    col=("blue","yellow","green")
    for i in range(200):
        mouse.pencolor(col[i%3])
        mouse.forward(i*4)
        mouse.right(121)
else:
    print("Invalid shape selected.")

turtle.done()
