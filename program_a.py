import cImage as image



def grayscale(filename):
    __convert("grayscale",filename)
    
def sepia_tone(filename):
    __convert("sepia_tone",filename)
    
def negative(filename):
    __convert("negative",filename)
    
def black_and_white(filename):
    __convert("black_and_white",filename)
    
def __convert(convert_type , filename):
    old_image = image.Image(filename)
    width,height = old_image.getWidth(),old_image.getHeight()

    new_image = image.EmptyImage(width, height)
        
    old_image.setPosition(0,0)



    for row in range(height):
        for col in range(width):
            old_pixel = old_image.getPixel(col,row)
            R,G,B = old_pixel.getRed() , old_pixel.getGreen() , old_pixel.getBlue()
            
            if convert_type == "grayscale":
                # Add the three colors together and then divide by 3 to get the average color
                R = G = B = (R + G + B) // 3
                
            elif convert_type == "sepia_tone":
                R = int(R * 0.393 + G * 0.769 + B * 0.189)
                G = int(R * 0.349 + G * 0.686 + B * 0.168)
                B = int(R * 0.272 + G * 0.534 + B * 0.131)
                
            elif convert_type == "negative":
                R = 255 - R
                G = 255 - G
                B = 255 - B
             
            elif convert_type == "black_and_white":
                # if total of 3 colors are bigger than (128*3) or 384 set 255 otherwise 0
                # it means that pixel is bright or dark
                # when it's bigger than average then convert it to the maximum and conversely
                R = G = B = 255 if ((R + G + B) >= 128 * 3) else 0

            
            new_pixel = image.Pixel(R,G,B)    
            new_image.setPixel( col , row , new_pixel )
            
            
    show_images(old_image,new_image)
    new_file_name = convert_type + "@" + filename;
    save_image_as_gif(new_image, new_file_name)
    
def show_images(old_image,new_image):
    width,height = old_image.getWidth(),old_image.getHeight()
    win = image.ImageWin("Image",width * 2, height)
    old_image.draw(win)
    new_image.setPosition(width + 1,0)
    new_image.draw(win)
    win.exitonclick()
    
def save_image_as_gif(image_object,name):
    name = "outputs/"+ name + ".gif"
    image_object.save(name)
    write_in_file(name)
    
def write_in_file(altered_file_name):
    output = open("outputs.txt","a")
    output.write(altered_file_name + "\n")
    output.close()

black_and_white("airplain.jpg")




