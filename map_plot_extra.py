# name: Kevin Lin
# date: 03/11/21
# purpose: create working map of Dartmouth
# You can skip ahead to line 426 to skip all the key processing + variable declaring code

from cs1lib import *
from search_box import *
from sort_dartmouth_alpha import *
from load_graph_extra import *
from bfs import *
from vertex_extra import *

KEY1 = "1"
KEY2 = "2"
KEY3 = "3"
KEY4 = "4"
KEY5 = "5"
KEY6 = "6"
KEY7 = "7"
KEY8 = "8"
KEY9 = "9"
KEY0 = "0"
KEYA = "a"
KEYB = "b"
KEYC = "c"
KEYD = "d"
KEYE = "e"
KEYF = "f"
KEYG = "g"
KEYH = "h"
KEYI = "i"
KEYJ = "j"
KEYK = "k"
KEYL = "l"
KEYM = "m"
KEYN = "n"
KEYO = "o"
KEYP = "p"
KEYQ = "q"
KEYR = "r"
KEYS = "s"
KEYT = "t"
KEYU = "u"
KEYV = "v"
KEYW = "w"
KEYX = "x"
KEYY = "y"
KEYZ = "z"
KEY_SPACE = " "
KEY_EQUAL = "="
KEY_MINUS = "-"

pressed1 = False
pressed2 = False
pressed3 = False
pressed4 = False
pressed5 = False
pressed6 = False
pressed7 = False
pressed8 = False
pressed9 = False
pressed0 = False
presseda = False
pressedb = False
pressedc = False
pressedd = False
pressede = False
pressedf = False
pressedg = False
pressedh = False
pressedi = False
pressedj = False
pressedk = False
pressedl = False
pressedm = False
pressedn = False
pressedo = False
pressedp = False
pressedq = False
pressedr = False
presseds = False
pressedt = False
pressedu = False
pressedv = False
pressedw = False
pressedx = False
pressedy = False
pressedz = False
pressed_space = False
pressed_equal = False
pressed_minus = False

FRAMERATE = 40
WHEIGHT = 811
WWIDTH = 1012

R_VERTEX = 0              # colors for non selected
G_VERTEX = .5
B_VERTEX = 0
R_EDGE = 0
G_EDGE = .5
B_EDGE = 0

RS_VERTEX = 1             # Colors for selections
GS_VERTEX = 0
BS_VERTEX = 0
RS_EDGE = 1
GS_EDGE = 0
BS_EDGE = 0

r_pulse = 0
g_pulse = 0
b_pulse = 0
selected_vertex = 0
goal_vertex = 0
mouse = 0
mx = 0
my = 0
dict = load_graph("dartmouth_alpha.txt")
dart_list = load_list("dartmouth_alpha.txt")
image = load_image("dartmouth_map.png")
search_list = []
search_box = 0

start_search = False
active_search = False
start_program = False

# finds the mouse's coordinates
def m_move(x, y):
    global mx, my
    mx = x
    my = y

def key_up(key): # checks if a key is released
    global presseda, pressedb, pressedc, pressedd, pressede, pressedf, pressedg, pressedh, pressedi, pressedj, pressedk
    global pressedl, pressedm, pressedn, pressedo, pressedp, pressedq, pressedr, presseds, pressedt, pressedu, pressedv
    global pressedw, pressedx, pressedy, pressedz, pressed_space, pressed1, pressed2, pressed3, pressed4, pressed0
    global pressed_equal, pressed5, pressed6, pressed7, pressed8, pressed9, pressed_minus

    if key == KEY1:
        pressed1 = False
    if key == KEY2:
        pressed2 = False
    if key == KEY3:
        pressed3 = False
    if key == KEY4:
        pressed4 = False
    if key == KEY5:
        pressed5 = False
    if key == KEY6:
        pressed6 = False
    if key == KEY7:
        pressed7 = False
    if key == KEY8:
        pressed8 = False
    if key == KEY9:
        pressed9 = False
    if key == KEY0:
        pressed0 = False
    if key == KEYA:
        presseda = False
    if key == KEYB:
        pressedb = False
    if key == KEYC:
        pressedc = False
    if key == KEYD:
        pressedd = False
    if key == KEYE:
        pressede = False
    if key == KEYF:
        pressedf = False
    if key == KEYG:
        pressedg = False
    if key == KEYH:
        pressedh = False
    if key == KEYI:
        pressedi = False
    if key == KEYJ:
        pressedj = False
    if key == KEYK:
        pressedk = False
    if key == KEYL:
        pressedl = False
    if key == KEYM:
        pressedm = False
    if key == KEYN:
        pressedn = False
    if key == KEYO:
        pressedo = False
    if key == KEYP:
        pressedp = False
    if key == KEYQ:
        pressedq = False
    if key == KEYR:
        pressedr = False
    if key == KEYS:
        presseds = False
    if key == KEYT:
        pressedt = False
    if key == KEYU:
        pressedu = False
    if key == KEYV:
        pressedv = False
    if key == KEYW:
        pressedw = False
    if key == KEYX:
        pressedx = False
    if key == KEYY:
        pressedy = False
    if key == KEYZ:
        pressedz = False
    if key == KEY_SPACE:
        pressed_space = False
    if key == KEY_EQUAL:
        pressed_equal = False
    if key == KEY_MINUS:
        pressed_minus = False

def key_down(key): # checks if a key is pressed
    global presseda, pressedb, pressedc, pressedd, pressede, pressedf, pressedg, pressedh, pressedi, pressedj, pressedk
    global pressedl, pressedm, pressedn, pressedo, pressedp, pressedq, pressedr, presseds, pressedt, pressedu, pressedv
    global pressedw, pressedx, pressedy, pressedz, pressed_space, pressed1, pressed2, pressed3, pressed4, pressed0
    global pressed_equal, pressed5, pressed6, pressed7, pressed8, pressed9, pressed_minus

    if key == KEY1:
        pressed1 = True
    if key == KEY2:
        pressed2 = True
    if key == KEY3:
        pressed3 = True
    if key == KEY4:
        pressed4 = True
    if key == KEY5:
        pressed5 = True
    if key == KEY6:
        pressed6 = True
    if key == KEY7:
        pressed7 = True
    if key == KEY8:
        pressed8 = True
    if key == KEY9:
        pressed9 = True
    if key == KEY0:
        pressed0 = True
    if key == KEYA:
        presseda = True
    if key == KEYB:
        pressedb = True
    if key == KEYC:
        pressedc = True
    if key == KEYD:
        pressedd = True
    if key == KEYE:
        pressede = True
    if key == KEYF:
        pressedf = True
    if key == KEYG:
        pressedg = True
    if key == KEYH:
        pressedh = True
    if key == KEYI:
        pressedi = True
    if key == KEYJ:
        pressedj = True
    if key == KEYK:
        pressedk = True
    if key == KEYL:
        pressedl = True
    if key == KEYM:
        pressedm = True
    if key == KEYN:
        pressedn = True
    if key == KEYO:
        pressedo = True
    if key == KEYP:
        pressedp = True
    if key == KEYQ:
        pressedq = True
    if key == KEYR:
        pressedr = True
    if key == KEYS:
        presseds = True
    if key == KEYT:
        pressedt = True
    if key == KEYU:
        pressedu = True
    if key == KEYV:
        pressedv = True
    if key == KEYW:
        pressedw = True
    if key == KEYX:
        pressedx = True
    if key == KEYY:
        pressedy = True
    if key == KEYZ:
        pressedz = True
    if key == KEY_SPACE:
        pressed_space = True
    if key == KEY_EQUAL:
        pressed_equal = True
    if key == KEY_MINUS:
        pressed_minus = True

# appends the character to search_list when typed
def search_letter():
    global presseda, pressedb, pressedc, pressedd, pressede, pressedf, pressedg, pressedh, pressedi, pressedj, pressedk
    global pressedl, pressedm, pressedn, pressedo, pressedp, pressedq, pressedr, presseds, pressedt, pressedu, pressedv
    global pressedw, pressedx, pressedy, pressedz, pressed_space, pressed1, pressed2, pressed3, pressed4, pressed0
    global pressed_equal, start_search, pressed5, pressed6, pressed7, pressed8, pressed9, pressed_minus

    if pressed1:
        search_list.append("1")
        pressed1 = False
    if pressed2:
        search_list.append("2")
        pressed2 = False
    if pressed3:
        search_list.append("3")
        pressed3 = False
    if pressed4:
        search_list.append("4")
        pressed4 = False
    if pressed5:
        search_list.append("5")
        pressed5 = False
    if pressed6:
        search_list.append("6")
        pressed6 = False
    if pressed7:
        search_list.append("7")
        pressed7 = False
    if pressed8:
        search_list.append("8")
        pressed8 = False
    if pressed9:
        search_list.append("9")
        pressed9 = False
    if pressed0:
        search_list.append("0")
        pressed0 = False
    if presseda:
        search_list.append("a")
        presseda = False
    if pressedb:
        search_list.append("b")
        pressedb = False
    if pressedc:
        search_list.append("c")
        pressedc = False
    if pressedd:
        search_list.append("d")
        pressedd = False
    if pressede:
        search_list.append("e")
        pressede = False
    if pressedf:
        search_list.append("f")
        pressedf = False
    if pressedg:
        search_list.append("g")
        pressedg = False
    if pressedh:
        search_list.append("h")
        pressedh = False
    if pressedi:
        search_list.append("i")
        pressedi = False
    if pressedj:
        search_list.append("j")
        pressedj = False
    if pressedk:
        search_list.append("k")
        pressedk = False
    if pressedl:
        search_list.append("l")
        pressedl = False
    if pressedm:
        search_list.append("m")
        pressedm = False
    if pressedn:
        search_list.append("n")
        pressedn = False
    if pressedo:
        search_list.append("o")
        pressedo = False
    if pressedp:
        search_list.append("p")
        pressedp = False
    if pressedq:
        search_list.append("q")
        pressedq = False
    if pressedr:
        search_list.append("r")
        pressedr = False
    if presseds:
        search_list.append("s")
        presseds = False
    if pressedt:
        search_list.append("t")
        pressedt = False
    if pressedu:
        search_list.append("u")
        pressedu = False
    if pressedv:
        search_list.append("v")
        pressedv = False
    if pressedw:
        search_list.append("w")
        pressedw = False
    if pressedx:
        search_list.append("x")
        pressedx = False
    if pressedy:
        search_list.append("y")
        pressedy = False
    if pressedz:
        search_list.append("z")
        pressedz = False
    if pressed_space:
        search_list.append(" ")
        pressed_space = False
    if pressed_minus:
        if search_list:
            search_list.pop()
        pressed_minus = False
    if pressed_equal:
        start_search = True

# pulses the three 3 r g b variables to create the pulsing line in the search box
def pulse_color():
    global r_pulse, g_pulse, b_pulse
    r_pulse = r_pulse + 0.02
    g_pulse = g_pulse + 0.02
    b_pulse = b_pulse + 0.02
    if r_pulse > 1:
        r_pulse = 0
        g_pulse = 0
        b_pulse = 0

# Parameters: Vertex is a vertex object, mx and my are mouse coordinates
# returns true if a vertex gets selected by the mouse being pressed and released on that vertex
def select_vertex(vertex):
    global mouse

    if is_mouse_pressed():
        mouse = vertex

    if not is_mouse_pressed() and vertex == mouse:
        mouse = 0
        return True
    else:
        return False

# draws all the vertexes
def draw_all_vertex():
    for i in dict:
        dict[i].vertex_draw(R_VERTEX, G_VERTEX, B_VERTEX)
        dict[i].edges_draw_all(R_EDGE, G_EDGE, B_EDGE)

# obtains the selected vertex and goal vertex based off mouse inputs
def obtain_goal():
    global selected_vertex, goal_vertex
    for i in dict:
        if dict[i].on_vertex(mx, my) and select_vertex(dict[i]):
            selected_vertex = dict[i]
        if selected_vertex and dict[i].on_vertex(mx, my):
            goal_vertex = dict[i]

# colors the selected vertex and goal in selection color
def draw_selection_vertex():
    global selected_vertex, goal_vertex
    if selected_vertex:
        selected_vertex.vertex_draw(RS_VERTEX, GS_VERTEX, BS_VERTEX)

    if goal_vertex and goal_vertex.on_vertex(mx, my):
        goal_vertex.vertex_draw(RS_VERTEX, GS_VERTEX, BS_VERTEX)

# Parameters: path is a list of vertex objects
# draws the path in selection color
def draw_path(path):
    for i in range(0, len(path)-1):
        path[i].edges_draw_between(RS_EDGE, GS_EDGE, BS_EDGE, path[i+1])
        path[i].vertex_draw(RS_VERTEX, GS_VERTEX, BS_VERTEX)

# draws the names of the selection and goal vertex
def draw_name():
    global selected_vertex, goal_vertex
    enable_stroke()
    set_font_size(22)
    set_stroke_color(1, 0, 0)
    draw_text(selected_vertex.name, selected_vertex.x - 30, selected_vertex.y - 20)
    draw_text(goal_vertex.name, goal_vertex.x - 30, goal_vertex.y - 20)

# draws the search box and pulses a "search line" at the end of the search so you know where you are typing
def draw_search():
    global search_list, search_box
    search_box = Searchbox(search_list, 20, 50, 270, 35, 15)
    search_box.draw_box(r_pulse, b_pulse, g_pulse)


# draws the name of the vertex that is being searched for / displays the closest search to what is typed
def draw_option():
    global dart_list, search_list, search_box

    vertex = find_option()
    if vertex:
        enable_stroke()
        set_font_size(20)
        set_stroke_color(0, 0, 0)
        draw_text(vertex.name + "?", 20, 130)
        vertex.search_display()

# checks when the search box gets clicked or unclicked
def search_clicked():
    global mx, my, active_search, goal_vertex, selected_vertex
    if search_box.on_box(mx, my):
        if is_mouse_pressed():
            if not active_search:
                goal_vertex = 0
                selected_vertex = 0
            active_search = True


    if not search_box.on_box(mx, my) and not search_box.on_button_start(mx, my) and not search_box.on_button_goal(mx, my):
        if is_mouse_pressed():
            active_search = False
            goal_vertex = 0
            selected_vertex = 0

# draws the buttons in
def draw_buttons():
    search_box.draw_start()
    search_box.draw_goal()

# makes pressing the buttons select vertex 1 and vertex 2
def button_func():
    global mx, my, goal_vertex, selected_vertex
    vertex = find_option()
    if search_box.on_button_start(mx, my) and vertex:
        if is_mouse_pressed():
            selected_vertex = vertex
    if search_box.on_button_goal(mx, my) and vertex:
        if is_mouse_pressed():
            goal_vertex = vertex

# consolidated search functions
def search_main():
    draw_search()      # just draw the box and check if the search box is clicked
    search_clicked()
    if active_search:  # once the search box gets clicked
        draw_buttons()
        search_letter()
        draw_option()
        button_func()

# returns the vertex if search was successful and false if not successful
def find_option():
    global dart_list, search_list, search_box

    i = 0
    while search_box.str > dart_list[i].name.lower():
        i = i + 1
        if i == len(dart_list):   # prevent infinite loop
            return False

    if len(search_box.str) > len(dart_list[i].name):
        return False

    for x in range(0, len(search_box.str)):
        if search_box.str[x] != dart_list[i].name[x].lower():
            return False
    else:
        return dart_list[i]

# draws the main menu / instructions before entering program
def main_menu():
    global start_program

    set_clear_color(1, 1, 1)
    clear()
    enable_stroke()
    set_stroke_color(0, 0, 0)
    set_font_italic()
    set_font_bold()
    set_font_size(65)
    draw_text("Dartmouth Pathfinder", 80, 150)
    set_font_size(25)
    set_font_normal()
    draw_text("Figure out how to get from place to place at Dartmouth", 120, 250)
    set_font_size(18)
    draw_text("Select a location with the mouse or search using the search box", 155, 420)
    draw_text("Use ''-'' for backspace", 380, 460)
    set_stroke_color(r_pulse, g_pulse, b_pulse)
    set_font_italic()
    set_font_bold()
    set_font_size(32)
    draw_text("Press Space to Continue", 250, 770)
    if pressed_space:
        start_program = True


# main function to pass into start_graphics
def main():
    global active_search, start_program
    pulse_color()
    if not start_program:
        main_menu()
    if start_program:
        set_font_normal()
        draw_image(image, 0, 0)
        draw_all_vertex()
        draw_selection_vertex()
        if not active_search:
            obtain_goal()
        if selected_vertex and goal_vertex:      # only draw once a goal and path are set
            draw_name()
            draw_path(bfs(selected_vertex, goal_vertex))
        search_main()


start_graphics(main, framerate=FRAMERATE ,height=WHEIGHT, width=WWIDTH, mouse_move=m_move, key_release=key_up, key_press=key_down)
