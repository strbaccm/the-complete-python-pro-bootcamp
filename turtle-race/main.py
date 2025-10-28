from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)



#now in order to start listening for events we have to get hold of the screen object and then tell it ot start listening
#and once it starts listening we have to bind a function that will be triggered when
# particular key is presses on the keyboard
screen.listen()

#when we use a function as an argument, so something that is going to be passed into another function
#we don't add parentheses as the end
# The parentheses triggers the function to happen there and then.

# only when the key space happens to trigger the function
screen.onkey(key="space", fun = move_forwards)
screen.exitonclick()