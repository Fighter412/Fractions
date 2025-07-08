import tkinter, tkinter.ttk
from tkinter.font import Font
import math

window = tkinter.Tk()

# Properties
color = "white"
arrow = "lime green"
custom_font = Font(family='Cascadia Mono', size=34, weight='bold')

def change(a=None, b=None, c=None):
    global numerator, denominator, mf_whole, mf_numerator, mf_denominator, mf_line, de_label, pe_label
    n, d = numerator.get(), denominator.get()
    canvas.delete("all")
    for i in range(n):
        canvas.create_image(100+100*i, 150, image=pizza)
        draw_sector((100+100*i, 150), 0, (i%d)/d)
        draw_sector((100+100*i, 150), 1 if ((i+1)%d)/d==0 else ((i+1)%d)/d, 1)
    mf_whole["text"]=int(n/d)
    if n%d != 0:
        mf_numerator["text"]=n%d
        mf_denominator["text"]=d
        mf_line["bg"]="black"
    else:
        mf_numerator["text"]=""
        mf_denominator["text"]=""
        mf_line["bg"]=color
    de_label["text"] = f"{n/d:.2f}"
    pe_label["text"] = f"{n/d*100:.0f}%"
    # wholes
    for i in range(int(n/d)):
        canvas.create_image(50+50*(d+2*d*i), 450, image=pizza)
        polygon = [(50+100*i*d+15*d, 225), (50+100*(i+1)*d-15*d, 225),      # upper left, upper right
                   (50+100*(i+1)*d-15*d, 300), (50+100*(i+1)*d-5*d, 300),   # middle right, right right
                   (50+100*(i+0.5)*d, 375),                                 # point
                   (50+100*i*d+5*d, 300), (50+100*i*d+15*d, 300)]           # left left, middle left
        canvas.create_polygon([coord for point in polygon for coord in point], fill="lime green")
        # white lines
        for j in range(d):
            canvas.create_line(50+50*(d+2*d*i), 450, 50+50*(d+2*d*i)+50*math.sin(math.pi/180*360*j/d), 450-50*math.cos(math.pi/180*360*j/d), fill=color, width=5)
    # fraction
    if n%d != 0:
        canvas.create_image(50+50*(2*d*int(n/d))+50*(n%d), 450, image=pizza)
        draw_sector((50+50*(2*d*int(n/d))+50*(n%d), 450), (n%d)/d, 1)
        polygon = [(50+50*(2*d*int(n/d))+50*(n%d)-35*(n%d), 225), (50+50*(2*d*int(n/d))+50*(n%d)+35*(n%d), 225),      # upper left, upper right
                   (50+50*(2*d*int(n/d))+50*(n%d)+35*(n%d), 300), (50+50*(2*d*int(n/d))+50*(n%d)+45*(n%d), 300),   # middle right, right right
                   (50+50*(2*d*int(n/d))+50*(n%d), 375),                                 # point
                   (50+50*(2*d*int(n/d))+50*(n%d)-45*(n%d), 300), (50+50*(2*d*int(n/d))+50*(n%d)-35*(n%d), 300)]           # left left, middle left
        canvas.create_polygon([coord for point in polygon for coord in point], fill="lime green")
        # white lines
        for j in range(d):
            canvas.create_line(50+50*(2*d*int(n/d))+50*(n%d), 450, 50+50*(2*d*int(n/d))+50*(n%d)+50*math.sin(math.pi/180*360*j/d), 450-50*math.cos(math.pi/180*360*j/d), fill=color, width=5)
    
    

def draw_sector(centre, start, stop):
    global canvas
    x, y = centre[0], centre[1]
    polygon = [centre]

    if 0<=start<=0.125 or 0.875<=start<=1:
        polygon.append((x+50*math.tan(math.pi/180*(360*start)), y-50))
    elif 0.125<=start<=0.375:
        polygon.append((x+50, y-50*math.tan(math.pi/180*(90-360*start))))
    elif 0.375<=start<=0.625:
        polygon.append((x+50*math.tan(math.pi/180*(180-360*start)), y+50))
    elif 0.625<=start<=0.875:
        polygon.append((x-50, y+50*math.tan(math.pi/180*(270-360*start))))
    
    if start<=0.125 and stop>=0.125:
        polygon.append((x+50, y-50))
    if start<=0.375 and stop>=0.375:
        polygon.append((x+50, y+50))
    if start<=0.625 and stop>=0.625:
        polygon.append((x-50, y+50))
    if start<=0.875 and stop>=0.875:
        polygon.append((x-50, y-50))

    if 0<=stop<=0.125 or 0.875<=stop<=1:
        polygon.append((x+50*math.tan(math.pi/180*(360*stop)), y-50))
    elif 0.125<=stop<=0.375:
        polygon.append((x+50, y-50*math.tan(math.pi/180*(90-360*stop))))
    elif 0.375<=stop<=0.625:
        polygon.append((x+50*math.tan(math.pi/180*(180-360*stop)), y+50))
    elif 0.625<=stop<=0.875:
        polygon.append((x-50, y+50*math.tan(math.pi/180*(270-360*stop))))

    canvas.create_polygon([coord for point in polygon for coord in point], fill=color)


window["bg"] = color
window.geometry("1500x800")
canvas = tkinter.Canvas(window, width=1500, height=600, background=color, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=100)

pizza = tkinter.PhotoImage(file="python/fractions/pizza.png")

# input (proper/ improper fraction)
tkinter.Label(window, font=Font(family='Cascadia Mono', size=12, weight='bold'), text="Improper Fraction", bg=color, width=20).grid(row=5, column=1)
numerator, denominator = tkinter.IntVar(value=1), tkinter.IntVar(value=2)
tkinter.Label(window, width=40, bg=color).grid(row=2, column=0)
tkinter.ttk.Spinbox(window, font=custom_font, width=4, from_=0, to=14, textvariable=numerator).grid(row=2, column=1)
tkinter.ttk.Spinbox(window, font=custom_font, width=4, from_=1, to=10, textvariable=denominator).grid(row=4, column=1)
numerator.trace_add(mode="write", callback=change)
denominator.trace_add(mode="write", callback=change)
tkinter.Frame(window, height=5, bg="black").grid(row=3, column=1, sticky="ew")
tkinter.Label(window, font=custom_font, text="=", bg=color).grid(row=2, rowspan=3, column=2)

# output (mixed fraction)
tkinter.Label(window, font=Font(family='Cascadia Mono', size=12, weight='bold'), text="Mixed Fraction", bg=color, width=20).grid(row=5, column=3, columnspan=2)
mf_whole = tkinter.Label(window, font=custom_font, width=2, bg=color)
mf_whole.grid(row=2, rowspan=3, column=3)
mf_numerator = tkinter.Label(window, font=custom_font, width=2, bg=color)
mf_numerator.grid(row=2, column=4)
mf_denominator = tkinter.Label(window, font=custom_font, width=2, bg=color)
mf_denominator.grid(row=4, column=4)
mf_line=tkinter.Frame(window, height=5, bg="black")
mf_line.grid(row=3, column=4, sticky="ew")
tkinter.Label(window, font=custom_font, text="=", bg=color).grid(row=2, rowspan=3, column=5)

# output (decimal)
tkinter.Label(window, font=Font(family='Cascadia Mono', size=12, weight='bold'), text="Decimal", bg=color, width=20).grid(row=5, column=6)
de_label = tkinter.Label(window,  font=custom_font, bg=color, width=5)
de_label.grid(row=2, rowspan=3, column=6)
tkinter.Label(window, font=custom_font, text="=", bg=color).grid(row=2, rowspan=3, column=7)

# output (percentage)
tkinter.Label(window, font=Font(family='Cascadia Mono', size=12, weight='bold'), text="Percent", bg=color, width=20).grid(row=5, column=8)
pe_label = tkinter.Label(window,  font=custom_font, bg=color, width=8)
pe_label.grid(row=2, rowspan=3, column=8)



change()

window.mainloop()

