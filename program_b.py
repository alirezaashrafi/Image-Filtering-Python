import turtle
import imagesize

screen_width, screen_height = 1000, 800


altered_images = open('outputs.txt', 'r')
images = altered_images.readlines()[-4:]
 
screen = turtle.Screen()
screen.setup(screen_width, screen_height)
screen.bgcolor('white')


position_width = screen_width // 2
position_height = screen_height // -2


for line in images:
    image = line.replace("\n", "")
    image_width, image_height = imagesize.get(image)
    screen.addshape(image)
    

    print(position_width - image_width // 2,position_height + image_height // 2)
    shape = turtle.Turtle()
    shape.shape(image)
    shape.penup()
    shape.setpos(position_width - image_width // 2 , position_height + image_height // 2)
    
    position_width -= image_width
    
    if position_width < 0 :
        position_height += image_height
        position_width = screen_width // 2


    shape.pendown()