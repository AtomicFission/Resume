

def digit_check(integer):
    return f"00{integer}" if integer < 10 else f"0{integer}" if integer < 100 else integer 

def generator(inputed_name, inputed_num):
    gui_foile = open("jif.gui", "w+", encoding="utf-8")
    gui_foile.write(
f"""icon = {{
    name = "frame1"
    texture = "gfx/resume/gifs/{inputed_name}/{inputed_name} 001.jpg"
    visible = "[Not(GetVariableSystem.Exists('{inputed_name}'))]"
    size = {{ @frameWidth @frameHeight }}
}}
state = {{
    name = {inputed_name}_frame1
    next = {inputed_name}_frame2
    duration = @frameDuration
    on_start = "[GetVariableSystem.Clear('{inputed_name}')]"
}}
""")
    for i in range(2, inputed_num):
        integer_as_string = digit_check(i)
        gui_foile.write(
f"""icon = {{
    name = "frame{i}"
    texture = "gfx/resume/gifs/{inputed_name}/{inputed_name} {integer_as_string}.jpg"
    visible = "[GetVariableSystem.HasValue('{inputed_name}', 'frame{i}')]"
    size = {{ @frameWidth @frameHeight }}
}}
state = {{
    name = {inputed_name}_frame{i}
    next = {inputed_name}_frame{i+1}
    duration = @frameDuration
    on_start = "[GetVariableSystem.Set('{inputed_name}', 'frame{i}')]"
}}
""")
    integer_as_string = digit_check(inputed_num)
    gui_foile.write(
f"""icon = {{
    name = "frame{inputed_num}"
    texture = "gfx/resume/gifs/{inputed_name}/{inputed_name} {integer_as_string}.jpg"
    visible = "[GetVariableSystem.HasValue('{inputed_name}', 'frame{inputed_num}')]"
    size = {{ @frameWidth @frameHeight }}
}}
state = {{
    name = {inputed_name}_frame{inputed_num}
    next = {inputed_name}_frame1
    duration = @frameDuration
    on_start = "[GetVariableSystem.Set('{inputed_name}', 'frame{inputed_num}')]"
}}""")

inputed_name = input("What is the name of this gif?\n")
inputed_num = input("How many frames does this gif have?\n")
generator(inputed_name, int(inputed_num))