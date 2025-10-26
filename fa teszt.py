import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=800, height=600, bg="white")
canvas.pack()
tree = tkinter.PhotoImage(file="tree.png")
global x
global y
x=250
y=250
tree_images = []

def makeTransparent(img, colorToMakeTransparentInHexFormat):
    newPhotoImage = tkinter.PhotoImage(width=img.width(), height=img.height())
    for x in range(img.width()):
        for y in range(img.height()):
            rgb = '#%02x%02x%02x' % img.get(x, y)
            if rgb != colorToMakeTransparentInHexFormat:
                newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

# obstacles

def fa(x1,y1):
    global x, y, tree
    newTreeImage = makeTransparent(tree, "#ffffff")
    tree_images.append(newTreeImage)  
    canvas.create_image(x1, y1, image=newTreeImage, tag="3")
    
    half_size = 32

   
    dx = x - x1
    dy = y - y1

    
    overlap_x = half_size * 2 - abs(dx)
    overlap_y = half_size * 2 - abs(dy)

    if overlap_x > 0 and overlap_y > 0:
        
        if overlap_x < overlap_y:
            
            if dx > 0:
                x += overlap_x  
            else:
                x -= overlap_x  
        else:
            
            if dy > 0:
                y += overlap_y  
            else:
                y -= overlap_y
fa(100,100)
root.mainloop()