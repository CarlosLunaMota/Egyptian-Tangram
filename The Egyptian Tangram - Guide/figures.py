#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#
# Figure generator for: "The Egyptian Tangram Guide"
#
# By: Carlos Luna Mota
#
################################################################################

# LIBRARIES
from pyx import *
from math import *

# CONSTANTS
BETA = 180*atan2(1,2)/pi
R2  = sqrt(2.0)
R3  = sqrt(3.0)
R5  = sqrt(5.0)
R10 = sqrt(10.0)

# COLOR PALETTE
WHITE    = color.grey.white
BLACK    = color.grey(0.10)
GREY     = color.grey(0.50)
CHALK    = color.grey(0.90)

RED      = color.cmyk.Mahogany
BLUE     = color.cmyk.NavyBlue
GREEN    = color.cmyk.ForestGreen
ORANGE   = color.cmyk.Orange
YELLOW   = color.cmyk.Dandelion

L_RED    = color.cmyk.Red
L_BLUE   = color.cmyk.SkyBlue
L_GREEN  = color.cmyk.LimeGreen
L_ORANGE = color.cmyk.YellowOrange
L_YELLOW = color.cmyk.Goldenrod

PLUM     = color.cmyk.Orchid
PINK     = color.cmyk.Lavender
BROWN    = color.cmyk.RawSienna

# LINE STYLES
BASE       = [style.linewidth.THick, style.linestyle.solid, style.linecap.round, style.linejoin.round, WHITE]
ULTRATHICK = [style.linewidth.THICK]
VERYTHICK  = [style.linewidth.THICk]
THICK      = [style.linewidth.THIck]
NORMAL     = [style.linewidth.THick]
THIN       = [style.linewidth.Thick]
VERYTHIN   = [style.linewidth.normal]
ULTRATHIN  = [style.linewidth.thin]
SOLID      = [style.linestyle.solid]
DASHED     = [style.linestyle.dashed]
DOTTED     = [style.linestyle.dotted]
DASHDOTTED = [style.linestyle.dashdotted]

def FILLED(color):
    return [deco.filled([color])]
def COLOR(color):
    return [color]

# AUXILIARY FUNCTIONS
def w_point((x1,x2), (y1,y2), Wx, Wy): return ((Wx*x1+Wy*y1)/(Wx+Wy), (Wx*x2+Wy*y2)/(Wx+Wy))
def s_point((x1,x2), (y1,y2), W): return ((W*(y1-x1))+y1 , (W*(y2-x2))+y2)

################################################################################

# FIGURES
def figure000a():
    '''Tangram dels Cinc Triangles'''

    name = "figures/figure000a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(B, C, 1,1)
    F = w_point(A, C, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure000b():
    '''Tangram de la Creu'''

    name = "figures/figure000b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, E, 3,2)
    H = w_point(C, E, 1,4)
    I = w_point(A, F, 3,2)
    J = w_point(A, F, 1,4)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.lineto(*B),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure000c():
    '''Tangram de la Creu - Retícula'''

    name = "figures/figure000c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, D, 1,1)
    H = w_point(D, A, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.moveto(*H),
                              path.lineto(*C),
                              path.moveto(*B),
                              path.lineto(*G),
                              path.moveto(*E),
                              path.lineto(*D)), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure000d():
    '''Tangram dels cinc triangles - Retícula'''

    name = "figures/figure000d"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*G),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D)), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*B),
                              path.moveto(*D),
                              path.lineto(*G),
                              path.moveto(*A),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*C)), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C),
                              path.moveto(*B),
                              path.lineto(*D)), BASE+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*G),
                              path.moveto(*F),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure000e():
    '''El Puzzle Egipci'''

    name = "figures/figure000e"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, E, 3,2)
    H = w_point(C, E, 1,4)
    I = w_point(A, F, 3,2)
    J = w_point(A, F, 1,4)
    K = w_point(A, B, 1,1)
    L = w_point(D, C, 1,1)
    M = w_point(J, B, 1,1)
    N = w_point(G, C, 1,1)
    O = w_point(I, J, 1,1)
    P = w_point(G, H, 1,1)
    Q = w_point(A, I, 1,1)
    R = w_point(H, D, 1,1)


    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*I),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*H),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*J),
                              path.lineto(*I),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*H),
                              path.lineto(*G),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*L),
                              path.moveto(*K),
                              path.lineto(*D),
                              path.moveto(*A),
                              path.lineto(*F),
                              path.moveto(*E),
                              path.lineto(*C),
                              path.moveto(*O),
                              path.lineto(*G)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001a():
    '''The Egyptian Tangram'''

    name = "figures/figure001a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []


    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C)), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E)), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F)), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D)), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I)), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001b():
    '''Egyptian Tangram outline'''

    name = "figures/figure001b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001c():
    '''Egyptian Tangram outline minus one line'''

    name = "figures/figure001c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001d():
    '''Egyptian Tangram outline minus two lines'''

    name = "figures/figure001d"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001e():
    '''Egyptian Tangram outline minus three lines'''

    name = "figures/figure001e"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001f():
    '''Egyptian Tangram outline plus 5x5 grid'''

    name = "figures/figure001f"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*w_point(A, D, 1,4)),
                              path.lineto(*w_point(B, C, 1,4)),
                              path.moveto(*w_point(A, D, 2,3)),
                              path.lineto(*w_point(B, C, 2,3)),
                              path.moveto(*w_point(A, D, 3,2)),
                              path.lineto(*w_point(B, C, 3,2)),
                              path.moveto(*w_point(A, D, 4,1)),
                              path.lineto(*w_point(B, C, 4,1)),
                              path.moveto(*w_point(A, B, 1,4)),
                              path.lineto(*w_point(D, C, 1,4)),
                              path.moveto(*w_point(A, B, 2,3)),
                              path.lineto(*w_point(D, C, 2,3)),
                              path.moveto(*w_point(A, B, 3,2)),
                              path.lineto(*w_point(D, C, 3,2)),
                              path.moveto(*w_point(A, B, 4,1)),
                              path.lineto(*w_point(D, C, 4,1))), BASE+DOTTED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001g():
    '''The Egyptian Tangram'''

    name = "figures/figure001g"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []


    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E)), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*I),
                              path.lineto(*C)), BASE+THICK+FILLED(color.cmyk.SpringGreen)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure001h():
    '''The Egyptian Tangram'''

    name = "figures/figure001h"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    drawing = []


    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E)), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F)), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*I),
                              path.lineto(*C)), BASE+THICK+FILLED(color.cmyk.SpringGreen)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002a():
    '''Egyptian Tangram grid'''

    name = "figures/figure002a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK+COLOR(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002b():
    '''Egyptian Tangram grid outline'''

    name = "figures/figure002b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002c():
    '''Egyptian Tangram grid outline'''

    name = "figures/figure002c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    I = w_point(E, B, 2,3)
    J = w_point(G, D, 1,1)
    K = w_point(F, D, 2,3)

    L = w_point(A, G, 1,4)
    M = w_point(B, H, 1,1)
    N = w_point(B, D, 2,1)


    drawing = []

    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C)), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*K),
                              path.lineto(*D)), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*L),
                              path.lineto(*M),
                              path.lineto(*N)), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002d():
    '''Egyptian Tangram grid outline'''

    name = "figures/figure002d"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    I = w_point(B, E, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E)), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*C)), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F)), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002e():
    '''Egyptian Tangram grid outline plus 2x2 grid'''

    name = "figures/figure002e"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*w_point(A, D, 1,1)),
                              path.lineto(*w_point(B, C, 1,1)),
                              path.moveto(*w_point(A, B, 1,1)),
                              path.lineto(*w_point(D, C, 1,1))), BASE+DOTTED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002f():
    '''Egyptian Tangram grid outline plus 3x3 grid'''

    name = "figures/figure002f"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*w_point(A, D, 1,2)),
                              path.lineto(*w_point(B, C, 1,2)),
                              path.moveto(*w_point(A, D, 2,1)),
                              path.lineto(*w_point(B, C, 2,1)),
                              path.moveto(*w_point(A, B, 1,2)),
                              path.lineto(*w_point(D, C, 1,2)),
                              path.moveto(*w_point(A, B, 2,1)),
                              path.lineto(*w_point(D, C, 2,1))), BASE+DOTTED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002g():
    '''Egyptian Tangram grid outline plus 4x4 grid'''

    name = "figures/figure002g"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*w_point(A, D, 1,3)),
                              path.lineto(*w_point(B, C, 1,3)),
                              path.moveto(*w_point(A, D, 2,2)),
                              path.lineto(*w_point(B, C, 2,2)),
                              path.moveto(*w_point(A, D, 3,1)),
                              path.lineto(*w_point(B, C, 3,1)),
                              path.moveto(*w_point(A, B, 1,3)),
                              path.lineto(*w_point(D, C, 1,3)),
                              path.moveto(*w_point(A, B, 2,2)),
                              path.lineto(*w_point(D, C, 2,2)),
                              path.moveto(*w_point(A, B, 3,1)),
                              path.lineto(*w_point(D, C, 3,1))), BASE+DOTTED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002h():
    '''Egyptian Tangram grid outline plus 5x5 grid'''

    name = "figures/figure002h"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)

    drawing = []

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*w_point(A, D, 1,4)),
                              path.lineto(*w_point(B, C, 1,4)),
                              path.moveto(*w_point(A, D, 2,3)),
                              path.lineto(*w_point(B, C, 2,3)),
                              path.moveto(*w_point(A, D, 3,2)),
                              path.lineto(*w_point(B, C, 3,2)),
                              path.moveto(*w_point(A, D, 4,1)),
                              path.lineto(*w_point(B, C, 4,1)),
                              path.moveto(*w_point(A, B, 1,4)),
                              path.lineto(*w_point(D, C, 1,4)),
                              path.moveto(*w_point(A, B, 2,3)),
                              path.lineto(*w_point(D, C, 2,3)),
                              path.moveto(*w_point(A, B, 3,2)),
                              path.lineto(*w_point(D, C, 3,2)),
                              path.moveto(*w_point(A, B, 4,1)),
                              path.lineto(*w_point(D, C, 4,1))), BASE+DOTTED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure002i():
    '''Egyptian Tangram grid colored'''

    name = "figures/figure002i"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(D, A, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(H, A, 1,1)
    J = w_point(E, B, 1,1)
    K = w_point(F, C, 1,1)
    L = w_point(G, D, 1,1)
    M = w_point(D, B, 2,1)
    N = w_point(A, C, 2,1)
    O = w_point(B, D, 2,1)
    P = w_point(C, A, 2,1)

    Q = w_point(C, E, 3,2)
    R = w_point(D, G, 3,2)
    S = w_point(D, F, 3,2)
    T = w_point(A, H, 3,2)
    U = w_point(A, G, 3,2)
    V = w_point(B, E, 3,2)
    W = w_point(B, H, 3,2)
    Y = w_point(C, F, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*N),
                              path.lineto(*J),
                              path.lineto(*O),
                              path.lineto(*K),
                              path.lineto(*P),
                              path.lineto(*L),
                              path.lineto(*M),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*P),
                              path.lineto(*Q),
                              path.lineto(*L),
                              path.closepath(),
                              path.moveto(*L),
                              path.lineto(*R),
                              path.lineto(*M),
                              path.closepath(),
                              path.moveto(*M),
                              path.lineto(*S),
                              path.lineto(*I),
                              path.closepath(),
                              path.moveto(*I),
                              path.lineto(*T),
                              path.lineto(*N),
                              path.closepath(),
                              path.moveto(*N),
                              path.lineto(*U),
                              path.lineto(*J),
                              path.closepath(),
                              path.moveto(*J),
                              path.lineto(*V),
                              path.lineto(*O),
                              path.closepath(),
                              path.moveto(*O),
                              path.lineto(*W),
                              path.lineto(*K),
                              path.closepath(),
                              path.moveto(*K),
                              path.lineto(*Y),
                              path.lineto(*P),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*U),
                              path.lineto(*F),
                              path.closepath(),
                              path.moveto(*B),
                              path.lineto(*V),
                              path.lineto(*F),
                              path.closepath(),
                              path.moveto(*B),
                              path.lineto(*W),
                              path.lineto(*G),
                              path.closepath(),
                              path.moveto(*C),
                              path.lineto(*Y),
                              path.lineto(*G),
                              path.closepath(),
                              path.moveto(*C),
                              path.lineto(*Q),
                              path.lineto(*H),
                              path.closepath(),
                              path.moveto(*D),
                              path.lineto(*R),
                              path.lineto(*H),
                              path.closepath(),
                              path.moveto(*D),
                              path.lineto(*S),
                              path.lineto(*E),
                              path.closepath(),
                              path.moveto(*A),
                              path.lineto(*T),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*U),
                              path.lineto(*N),
                              path.lineto(*T),
                              path.closepath(),
                              path.moveto(*B),
                              path.lineto(*W),
                              path.lineto(*O),
                              path.lineto(*V),
                              path.closepath(),
                              path.moveto(*C),
                              path.lineto(*Q),
                              path.lineto(*P),
                              path.lineto(*Y),
                              path.closepath(),
                              path.moveto(*D),
                              path.lineto(*S),
                              path.lineto(*M),
                              path.lineto(*R),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*T),
                              path.lineto(*I),
                              path.lineto(*S),
                              path.closepath(),
                              path.moveto(*F),
                              path.lineto(*U),
                              path.lineto(*J),
                              path.lineto(*V),
                              path.closepath(),
                              path.moveto(*G),
                              path.lineto(*Y),
                              path.lineto(*K),
                              path.lineto(*W),
                              path.closepath(),
                              path.moveto(*H),
                              path.lineto(*R),
                              path.lineto(*L),
                              path.lineto(*Q),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*D),
                              path.moveto(*G),
                              path.lineto(*A),
                              path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*H),
                              path.moveto(*F),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.moveto(*A),
                              path.lineto(*H)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure003a():
    '''El Tangram Egípci - Decomposat'''

    name = "figures/figure003a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(I, B, 1,1)
    K = w_point(I, C, 1,1)
    L = w_point(C, E, 3,2)
    M = w_point(B, E, 1,4)
    N = w_point(C, E, 1,4)
    O = w_point(A, M, 1,1)
    P = w_point(N, D, 1,1)
    drawing = []


    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C)), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E)), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F)), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D)), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I)), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*G),
                              path.lineto(*K),
                              path.lineto(*J),
                              path.moveto(*N),
                              path.lineto(*D),
                              path.moveto(*P),
                              path.lineto(*L),
                              path.lineto(*H),
                              path.lineto(*P),
                              path.moveto(*A),
                              path.lineto(*M),
                              path.moveto(*F),
                              path.lineto(*O),
                              path.lineto(*I)), BASE+THIN+DASHED))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure003b():
    '''Tangram de la Creu - Decomposat'''

    name = "figures/figure003b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, E, 3,2)
    H = w_point(C, E, 1,4)
    I = w_point(A, F, 3,2)
    J = w_point(A, F, 1,4)
    K = w_point(A, B, 1,1)
    L = w_point(D, C, 1,1)
    M = w_point(J, B, 1,1)
    N = w_point(G, C, 1,1)
    O = w_point(I, J, 1,1)
    P = w_point(G, H, 1,1)
    Q = w_point(A, I, 1,1)
    R = w_point(H, D, 1,1)


    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*N),
                              path.lineto(*J),
                              path.moveto(*G),
                              path.lineto(*O),
                              path.lineto(*P),
                              path.lineto(*I),
                              path.lineto(*A),
                              path.moveto(*D),
                              path.lineto(*H),
                              path.lineto(*Q),
                              path.lineto(*E),
                              path.moveto(*G),
                              path.lineto(*L),
                              path.lineto(*R),
                              path.lineto(*G),
                              path.moveto(*K),
                              path.lineto(*I),
                              path.lineto(*M),
                              path.lineto(*K)), BASE+THIN+DASHED))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.moveto(*G),
                              path.lineto(*B)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure003c():
    '''Tangram Xinés - Decomposat'''

    name = "figures/figure003c"

    X = 3*R2
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(E, F, 1,1)
    H = w_point(A, C, 3,1)
    I = w_point(A, C, 1,1)
    J = w_point(A, C, 1,3)
    K = w_point(C, D, 1,1)
    L = w_point(D, A, 1,1)
    M = w_point(I, D, 1,1)

    drawing = []
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*C),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*I),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(PINK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*I),
                              path.closepath()), BASE+FILLED(PLUM)))
    drawing.append((path.path(path.moveto(*G),
                              path.lineto(*I),
                              path.lineto(*H),
                              path.closepath()), BASE+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*H),
                              path.lineto(*G),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*G),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*M),
                              path.lineto(*J),
                              path.moveto(*E),
                              path.lineto(*L),
                              path.lineto(*K),
                              path.lineto(*J),
                              path.lineto(*G),
                              path.lineto(*B)), BASE+THIN+DASHED))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004a():
    '''T1+T4+T5 - Figura a'''

    name = "figures/figure004a"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,1*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004b():
    '''T1+T4+T5 - Figura b'''

    name = "figures/figure004b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (5*X,2*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004c():
    '''T1+T4+T5 - Figura c'''

    name = "figures/figure004c"

    X = 1 # Scale #
    A = (     0,     0)
    B = (1*X*R5,2*X*R5)
    C = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004d():
    '''T1+T4+T5 - Figura d'''

    name = "figures/figure004d"

    X = 1 # Scale #
    A = (     0,     0)
    B = (2*X*R5,1*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004e():
    '''T1+T4+T5 - Figura e'''

    name = "figures/figure004e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (1*X,2*X)
    C = (5*X,2*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004f():
    '''T1+T4+T5 - Figura f'''

    name = "figures/figure004f"

    X = 1 # Scale #
    A = (  0,  0)
    B = (4*X,2*X)
    C = (5*X,2*X)
    D = (9*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004g():
    '''T1+T4+T5 - Figura g'''

    name = "figures/figure004g"

    X = 1 # Scale #
    A = (   0,  0)
    B = (   0,4*X)
    C = (-1*X,4*X)
    D = (-4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004h():
    '''T1+T4+T5 - Figura h'''

    name = "figures/figure004h"

    X = 1 # Scale #
    A = (  0,  0)
    B = (1*X,2*X)
    C = (6*X,2*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004i():
    '''T1+T4+T5 - Figura i'''

    name = "figures/figure004i"

    X = 1 # Scale #
    A = (  0,  0)
    B = (4*X,2*X)
    C = (9*X,2*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004j():
    '''T1+T4+T5 - Figura j'''

    name = "figures/figure004j"

    X = 1 # Scale #
    A = (  0,4*X)
    B = (2*X,5*X)
    C = (4*X,4*X)
    D = (2*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure004k():
    '''T1+T4+T5 - Figura k'''

    name = "figures/figure004k"

    X = 1.0 # Scale #
    A = (   0,  0)
    B = (-2*X,  0)
    C = (-2*X,4*X)
    D = (   0,5*X)

    E = w_point(C,D, 1,4)
    F = s_point((0,4*X),E, 1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure005a():
    '''T1+T4+T5 - Pythagoras of T5'''

    name = "figures/figure005a"

    X = 1.0 # Scale #
    A = (      0,      0)
    B = (-1*X*R5,      0)
    C = (      0, 2*X*R5)

    D = (-1*X*R5, 2*X*R5)
    E = ( 4*X/R5, 2*X/R5)
    F = s_point(E, A, 1)

    drawing = []
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure005b():
    '''T1+T4+T5 - Pythagoras of T4'''

    name = "figures/figure005b"

    X = 1.0 # Scale #
    A = (   0,   0)
    B = (-2*X,   0)
    C = (   0, 4*X)

    E = ( 2*X,  4*X)
    F = (   0, -1*X)
    D = s_point(F,B, 1.0)

    drawing = []
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure005c():
    '''T1+T4+T5 - Pythagoras of T1'''

    name = "figures/figure005c"

    X = 1.0 # Scale #
    A = (   0,   0)
    B = (-1*X,   0)
    C = (   0, 2*X)

    D = (-5*X,  2*X)
    E = ( 4*X,  2*X)
    F = (   0, -2*X)

    drawing = []
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006a():
    '''1:2:sqrt(5) inradius'''

    name = "figures/figure006a"

    X   = 1.0 # Scale #
    PHI = (1.0+R5)/2.0
    A   = (             0,             0)
    B   = (             0, 1*(PHI+1.0)*X)
    C   = ( 2*(PHI+1.0)*X,             0)
    D   = w_point(B,C, PHI+1,1.0)

    drawing = []

    drawing.append((path.circle(X, X, X), BASE))
    drawing.append((path.path(path.moveto(X,X),
                              path.lineto(X,0),
                              path.moveto(X,X),
                              path.lineto(0,X),
                              path.moveto(X,X),
                              path.lineto(*D)), BASE+DASHED+VERYTHIN))

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006b():
    '''3:4:5 inradius'''

    name = "figures/figure006b"

    X   = 1.0 # Scale #
    A   = (  0,   0)
    B   = (  0, 3*X)
    C   = (4*X,   0)
    D   = w_point(B,C, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.circle(X, X, X), BASE))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(X,X),
                              path.lineto(0,X),
                              path.closepath()), BASE+FILLED(RED)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006c():
    '''3:4:5 dissection'''

    name = "figures/figure006c"

    X   = 1.0 # Scale #
    A   = (  0,   0)
    B   = (  0, 3*X)
    C   = (4*X,   0)
    D   = w_point(B,C, 3,2)

    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))
    drawing.append((path.circle(X, X, X), BASE+DASHED+VERYTHIN))
    drawing.append((path.path(path.moveto(X,X),
                              path.lineto(X,0),
                              path.moveto(X,X),
                              path.lineto(0,X),
                              path.moveto(X,X),
                              path.lineto(*D),
                              path.moveto(X,X),
                              path.lineto(*C),
                              path.moveto(X,X),
                              path.lineto(*B),
                              path.moveto(X,X),
                              path.lineto(*A)), BASE+THIN))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006d():
    '''3:4:5 dissection'''

    name = "figures/figure006d"

    X   = 1.0 # Scale #
    A   = (  0,   0)
    B   = (  0, 3*X)
    C   = (4*X,   0)
    D   = w_point(B,C, 2,3)
    E   = w_point(A,C, 2.5,1.5)

    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*D)), BASE+THIN+DASHED))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006e():
    '''1:2:sqrt(5) dissection'''

    name = "figures/figure006e"

    X   = 1.0 # Scale #
    A   = (  0,   0)
    B   = (  0, 4*X)
    C   = (8*X,   0)
    D   = w_point(B,C, 1,1)
    E   = w_point(A,C, 5,3)

    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*D)), BASE+THIN+DASHED))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006f():
    '''1:2:sqrt(5) dissection'''

    name = "figures/figure006f"

    X = 1.0 # Scale #
    A = (  0,   0)
    B = (  0, 4*X)
    C = (8*X,   0)
    D = w_point(B,C, 1,1)
    E = w_point(A,C, 5,3)
    F = w_point(B,E, 1,4)

    drawing = []

    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*D),
                              path.closepath()), BASE+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006g():
    '''Pinwheel tiling'''

    name = "figures/figure006g"

    def pinwheel(A, B, C, depth):
        output = [(A, B, C, depth)]
        if depth > 0:
            D = w_point(B,C, 4,1)
            E = w_point(D,C, 1,1)
            F = w_point(A,C, 1,1)
            G = w_point(A,D, 1,1)
            output.extend(pinwheel(D,B,A,depth-1))
            output.extend(pinwheel(E,F,D,depth-1))
            output.extend(pinwheel(G,D,F,depth-1))
            output.extend(pinwheel(G,A,F,depth-1))
            output.extend(pinwheel(E,F,C,depth-1))
        return output


    X = 1.0 # Scale #
    A = (  0,   0)
    B = (  0, 4*X)
    C = (8*X,   0)
    S = [ULTRATHIN, VERYTHIN, VERYTHICK, VERYTHICK]

    drawing = []
    for P,Q,R,s in pinwheel(A, B, C, 3):
        drawing.append((path.path(path.moveto(*P),
                                  path.lineto(*Q),
                                  path.lineto(*R),
                                  path.closepath()), BASE+S[s]))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure006h():
    '''Pinwheel Franctal'''

    name = "figures/figure006h"

    def pinwheel(A, B, C, depth):
        output = [(A, B, C, depth)]
        if depth > 0:
            D = w_point(B,C, 4,1)
            E = w_point(D,C, 1,1)
            F = w_point(A,C, 1,1)
            G = w_point(A,D, 1,1)
            output.extend(pinwheel(D,B,A,depth-1))
            output.extend(pinwheel(E,F,D,depth-1))
            output.extend(pinwheel(G,A,F,depth-1))
            output.extend(pinwheel(E,F,C,depth-1))
        return output


    X = 1.0 # Scale #
    A = (  0,   0)
    B = (  0, 4*X)
    C = (8*X,   0)
    S = [ULTRATHIN+DOTTED, ULTRATHIN, VERYTHIN, THIN, NORMAL, THICK]

    drawing = []
    for P,Q,R,s in pinwheel(A, B, C, 5):
        drawing.append((path.path(path.moveto(*P),
                                  path.lineto(*Q),
                                  path.lineto(*R),
                                  path.closepath()), BASE+S[s]))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure007a():
    '''Q4 with angles'''

    name = "figures/figure007a"

    X = 1.0 # Scale #
    A = ( 0, 0)
    B = ( 0, R5*X)
    C = w_point(B, (R5*X*2,R5*X*2), 4,1)
    D = ( R5*X,0)
    E = ( 0, R5*X*2)

    drawing = []

    #drawing.append((path.path(path.moveto(*C), path.arc(C[0],C[1], X/2.0, 180, 360)), BASE+COLOR(BLUE)))

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D)), BASE+DASHED+THIN))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*A),
                              path.lineto(*D),
                              path.closepath()), BASE+DASHED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure007b():
    '''Golden Rombus with angles'''

    name = "figures/figure007b"

    X = 1.0 # Scale #
    Y = (1.0+R5)/2.0
    A = (-X, 0)
    B = ( 0, Y)
    C = ( X, 0)
    D = ( 0,-Y)

    drawing = []

    #drawing.append((path.path(path.moveto(*C), path.arc(C[0],C[1], X/2.0, 180, 360)), BASE+COLOR(BLUE)))

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D)), BASE+DASHED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C)), BASE+DASHED+THIN))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019():
    '''El Tangram Egípci - 5 cercles notables'''

    name = "figures/figure019"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(F, B, 1,1)

    C1 = w_point(C, E, 1,1)
    C2 = w_point(F, E, 1,1)
    C3 = G
    C4 = D

    drawing = []
    #drawing.append((path.path(path.moveto(*F), path.arc(J[0], J[1], X/4.0, 270, 90)), BASE+THICK+COLOR(PLUM)))
    drawing.append((path.circle(J[0], J[1], X/4), BASE+THICK+COLOR(PLUM)))

    #drawing.append((path.circle(X, 0, X), BASE+THICK+COLOR(color.rgb.blue)))
    drawing.append((path.path(path.moveto(*C), path.arc(X,0, X, 90, 180)), BASE+THICK+COLOR(color.rgb.blue)))

    #drawing.append((path.circle(X/2.0,X,X/2.0), BASE+THICK+COLOR(color.rgb.green)))
    drawing.append((path.path(path.moveto(*B), path.arc(X/2.0,X, X/2.0, 180, 360)), BASE+THICK+COLOR(color.rgb.green)))

    drawing.append((path.circle(C2[0], C2[1], X/(2*R2)), BASE+THICK+COLOR(ORANGE)))

    drawing.append((path.circle(C1[0], C1[1], X*R5/4.0), BASE+THICK+COLOR(color.rgb.red)))

    #drawing.append((path.path(path.moveto(X/2.0, X/2.0),path.lineto(X/2.0, X/2.0)), BASE+THICK))
    #drawing.append((path.path(path.moveto(X/2.0, X/2.0),path.lineto(X/2.0, X/2.0)), BASE+THICK))
    #drawing.append((path.path(path.moveto(X/2.0, X/2.0),path.lineto(X/2.0, X/2.0)), BASE+THICK))
    #drawing.append((path.path(path.moveto(X/2.0, X/2.0),path.lineto(X/2.0, X/2.0)), BASE+THICK))

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019b():
    '''El Tangram Egípci - El quadrilater es ciclic'''

    name = "figures/figure019b"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(F, B, 1,1)

    C1 = w_point(C, E, 1,1)
    C2 = w_point(F, E, 1,1)
    C3 = G
    C4 = D

    drawing = []
    drawing.append((path.circle(C2[0], C2[1], X/(2*R2)), BASE+COLOR(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019c():
    '''El Tangram Egípci - 4 circumcircles'''

    name = "figures/figure019c"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(F, B, 1,1)

    C1 = w_point(C, E, 1,1)
    C2 = w_point(F, E, 1,1)
    C3 = G
    C4 = D

    drawing = []
    drawing.append((path.circle(J[0], J[1], X/4), BASE+COLOR(RED)))

    drawing.append((path.path(path.moveto(*B), path.arc(X/2.0,X, X/2.0, 180, 360)), BASE+COLOR(BLUE)))

    drawing.append((path.circle(C2[0], C2[1], X/(2*R2)), BASE+COLOR(ORANGE)))

    drawing.append((path.circle(C1[0], C1[1], X*R5/4.0), BASE+COLOR(color.cmyk.SpringGreen)))

    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019d():
    '''El Tangram Egípci - 2 tangent circles'''

    name = "figures/figure019d"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(F, B, 1,1)

    C1 = w_point(C, E, 1,1)
    C2 = w_point(F, E, 1,1)
    C3 = G
    C4 = D

    drawing = []
    drawing.append((path.circle(J[0], J[1], X/4), BASE+COLOR(RED)))
    drawing.append((path.path(path.moveto(*C), path.arc(X,0, X, 90, 180)), BASE+COLOR(PLUM)))

    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*J)), BASE+THIN+DASHED))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure019e():
    '''El Tangram Egípci - 1 tangent circle'''

    name = "figures/figure019e"

    X = 2.0*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(F, B, 1,1)

    C1 = w_point(C, E, 1,1)
    C2 = w_point(F, E, 1,1)
    C3 = G
    C4 = D

    drawing = []
    drawing.append((path.path(path.moveto(*B), path.arc(X/2.0,X, X/2.0, 180, 360)), BASE+COLOR(BLUE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*J),
                              path.lineto(*A),
                              path.closepath()), BASE+ULTRATHIN+[deco.filled([YELLOW, color.transparency(0.75)])]+[YELLOW, color.transparency(0.75)]))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*J)), BASE+THIN+DASHED))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020a():
    '''T1+Q4'''

    name = "figures/figure020a"

    X = 2*R5
    A = (0,0)
    B = (X/2.0,0)
    C = (0,X)
    D = w_point(A, C, 1,1)
    E = w_point(B, C, 2,3)
    F = w_point(B, C, 4,1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020b():
    '''T5'''

    name = "figures/figure020b"

    X = 2*R5
    A = (0,0)
    B = (X/2.0,0)
    C = (0,X)
    D = w_point(A, C, 1,1)
    E = w_point(B, C, 2,3)
    F = w_point(B, C, 4,1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020c():
    '''T1+T4'''

    name = "figures/figure020c"

    X = 2*R5
    A = (0,0)
    B = (X/2.0,0)
    C = (0,X)
    D = w_point(A, C, 1,1)
    E = w_point(B, C, 2,3)
    F = w_point(B, C, 4,1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020d():
    '''T1+Q4+T5'''

    name = "figures/figure020d"

    X = 2*R5
    A = (0,0)
    B = (X,0)
    C = (X/2.0,X)
    D = w_point(A, B, 1,1)
    E = w_point(C, D, 1,1)
    F = w_point(B, C, 2,3)
    G = w_point(A, C, 3,2)

    drawing = []
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020e():
    '''T4+T6'''

    name = "figures/figure020e"

    X = 2*R5
    A = (0,0)
    B = (X,0)
    C = (X/2.0,X)
    D = w_point(A, B, 1,1)
    E = w_point(C, D, 1,1)
    F = w_point(B, C, 2,3)
    G = w_point(A, C, 3,2)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020f():
    '''T1+Q4+T5'''

    name = "figures/figure020f"

    X = 2*R5
    A = (X,0)
    B = (0,0)
    C = (X/2.0,X)
    D = w_point(A, B, 1,1)
    E = w_point(C, D, 1,1)
    F = w_point(B, C, 2,3)
    G = w_point(A, C, 3,2)

    drawing = []
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020g():
    '''T4+T6'''

    name = "figures/figure020g"

    X = 2*R5
    A = (X,0)
    B = (0,0)
    C = (X/2.0,X)
    D = w_point(A, B, 1,1)
    E = w_point(C, D, 1,1)
    F = w_point(B, C, 2,3)
    G = w_point(A, C, 3,2)

    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*G),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020h():
    '''T6+Q4'''

    name = "figures/figure020h"

    X = 2*R5
    A = (0,0)
    B = (X/2.0,0)
    C = (X,X)
    D = (0,X/2.0)
    E = w_point(C, D, 1,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020i():
    '''T6+Q4'''

    name = "figures/figure020i"

    X = 2*R5
    A = (0,0)
    B = (0,X/2.0)
    C = (X,X)
    D = (X/2.0,0)
    E = w_point(C, D, 1,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020j():
    '''T1+T4+T5+Q4'''

    name = "figures/figure020j"

    X = 1.0 # Scale!
    A = (0  ,X*2)
    B = (0  ,X*0)
    C = (X*7,X*0)
    D = (X*7,X*2)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 5,2)
    G = w_point(D, A, 3,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020k():
    '''T1+T4+T5+Q4'''

    name = "figures/figure020k"

    X = 1.0 # Scale!
    A = (X*7,X*2)
    B = (X*7,X*0)
    C = (X*0,X*0)
    D = (X*0,X*2)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 5,2)
    G = w_point(D, A, 3,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020l():
    '''T1+T4+T5+Q4'''

    name = "figures/figure020l"

    X = 1.0 # Scale!
    A = (0  ,X*0)
    B = (0  ,X*2)
    C = (X*7,X*2)
    D = (X*7,X*0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 5,2)
    G = w_point(D, A, 3,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure020m():
    '''T1+T4+T5+Q4'''

    name = "figures/figure020m"

    X = 1.0 # Scale!
    A = (X*7,X*0)
    B = (X*7,X*2)
    C = (X*0,X*2)
    D = (X*0,X*0)
    E = w_point(A, B, 1,1)
    F = w_point(B, C, 5,2)
    G = w_point(D, A, 3,4)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*G),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*E),
                              path.lineto(*B),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure021a():
    '''El Tangram Egípci - Quadrat 1'''

    name = "figures/figure021a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(C, E, 3,2)
    K = w_point(C, E, 1,4)
    drawing = []


    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure021b():
    '''El Tangram Egípci - Quadrat 2'''

    name = "figures/figure021b"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(C, E, 3,2)
    K = w_point(C, E, 1,4)
    drawing = []


    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*J),
                              path.lineto(*H),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*H),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*J),
                              path.lineto(*H),
                              path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure021c():
    '''El Tangram Egípci - Quadrat 3'''

    name = "figures/figure021c"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(C, E, 3,2)
    K = w_point(C, E, 1,4)
    drawing = []


    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*D),
                              path.moveto(*F),
                              path.lineto(*C),
                              path.lineto(*I)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022a():
    '''El Tangram Egípci - Figura 1'''

    name = "figures/figure022a"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022b():
    '''El Tangram Egípci - Figura 2'''

    name = "figures/figure022b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (5*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022c():
    '''El Tangram Egípci - Figura 3'''

    name = "figures/figure022c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (4*X,4*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022d():
    '''El Tangram Egípci - Figura 4'''

    name = "figures/figure022d"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (2*X,4*X)
    D = (6*X,2*X)
    E = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022e():
    '''El Tangram Egípci - Figura 5'''

    name = "figures/figure022e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (4*X,4*X)
    D = (4*X,2*X)
    E = (6*X,2*X)
    F = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022f():
    '''El Tangram Egípci - Figura 6'''

    name = "figures/figure022f"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (3*X,4*X)
    D = (3*X,5*X)
    E = (5*X,5*X)
    F = (5*X,2*X)
    G = (4*X,2*X)
    H = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022g():
    '''El Tangram Egípci - Figura 7'''

    name = "figures/figure022g"

    X = 1 # Scale #
    A = (  0,  0)
    B = (3*X,4*X)
    C = (5*X,4*X)
    D = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022h():
    '''El Tangram Egípci - Figura 8'''

    name = "figures/figure022h"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (5*X,4*X)
    D = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022i():
    '''El Tangram Egípci - Figura 9'''

    name = "figures/figure022i"

    X = 1 # Scale #
    A = (     0,     0)
    B = (1*X*R5,2*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (3*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022j():
    '''El Tangram Egípci - Figura 10'''

    name = "figures/figure022j"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (7*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022k():
    '''El Tangram Egípci - Figura 11'''

    name = "figures/figure022k"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,1*X*R5)
    C = (-2*X*R5,2*X*R5)
    D = (-3*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022l():
    '''El Tangram Egípci - Figura 12'''

    name = "figures/figure022l"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022m():
    '''El Tangram Egípci - Figura 13'''

    name = "figures/figure022m"

    X = 1 # Scale #
    A = (      0,-1*X*R5)
    B = (-2*X*R5,      0)
    C = (      0, 1*X*R5)
    D = ( 2*X*R5,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022n():
    '''El Tangram Egípci - Figura 14'''

    name = "figures/figure022n"

    X = 1 # Scale #
    A = (   0,-3*X)
    B = (-4*X,   0)
    C = (   0, 2*X)
    D = ( 4*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022o():
    '''El Tangram Egípci - Figura 15'''

    name = "figures/figure022o"

    X = 1 # Scale #
    A = (      0,      0)
    C = (-1*X*R5, 2*X*R5)
    D = ( 1*X*R5, 2*X*R5)

    I = w_point(A,C, 1,4)
    J = w_point(A,D, 1,4)
    K = w_point(C,D, 1,1)
    B = s_point(K,I, 1)
    E = s_point(K,J, 1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022p():
    '''El Tangram Egípci - Figura 16'''

    name = "figures/figure022p"

    X = 1 # Scale #
    A = (      0,      0)
    B = (1*X*R10,1*X*R10)
    C = (      0,2*X*R10)
    D = (3*X*R10,1*X*R10)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022q():
    '''El Tangram Egípci - Figura 17'''

    name = "figures/figure022q"

    X = 1 # Scale #
    A = (     0,     0)
    B = (2*X*R5,1*X*R5)
    C = (     0,2*X*R5)
    D = (2*X*R5,2*X*R5)
    E = (4*X*R5,1*X*R5)
    F = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022r():
    '''El Tangram Egípci - Figura 18'''

    name = "figures/figure022r"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (1*X*R5,2*X*R5)
    D = (3*X*R5,1*X*R5)
    E = (1*X*R5,0*X*R5)

    #A = (     0,     0)
    #B = (     0,2*X*R5)
    #C = (2*X*R5,1*X*R5)
    #D = (2*X*R5,2*X*R5)
    #E = (3*X*R5,2*X*R5)
    #F = (3*X*R5,     0)
    #G = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              #path.lineto(*F),
                              #path.lineto(*G),
                              #path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022s():
    '''El Tangram Egípci - Figura 19'''

    name = "figures/figure022s"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (2*X*R5,2*X*R5)
    E = (4*X*R5,1*X*R5)
    F = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022t():
    '''El Tangram Egípci - Figura 20'''

    name = "figures/figure022t"

    X = 1 # Scale #
    A = (     0/2.0,1*X*R5/2.0)
    B = (     0/2.0,3*X*R5/2.0)
    C = (4*X*R5/2.0,3*X*R5/2.0)
    D = (4*X*R5/2.0,4*X*R5/2.0)
    E = (8*X*R5/2.0,2*X*R5/2.0)
    F = (4*X*R5/2.0,     0/2.0)
    G = (4*X*R5/2.0,1*X*R5/2.0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022u():
    '''El Tangram Egípci - Figura 21'''

    name = "figures/figure022u"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (2*X,6*X)
    D = (4*X,6*X)
    E = (4*X,4*X)
    F = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022v():
    '''El Tangram Egípci - Figura 22'''

    name = "figures/figure022v"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,5*X)
    C = (4*X,2*X)
    D = (7*X,2*X)
    E = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022w():
    '''El Tangram Egípci - Figura 23'''

    name = "figures/figure022w"

    X = 1 # Scale #
    A = (         0,  0)
    B = (         0,2*X*R5)
    C = (1*X*R5    ,2*X*R5)
    D = (2*X*R5-1*X,2*X)
    E = (2*X*R5+2*X,2*X)
    F = (2*X*R5+2*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure022x():
    '''El Tangram Egípci - Figura 24'''

    name = "figures/figure022x"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (3*X,4*X)
    D = (4*X,2*X)
    E = (6*X,2*X)
    F = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023a():
    '''El Subtangram Egípci - Figura 1'''

    name = "figures/figure023a"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (4*X,4*X)
    D = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023b():
    '''El Subtangram Egípci - Figura 2'''

    name = "figures/figure023b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (3*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023c():
    '''El Subtangram Egípci - Figura 3'''

    name = "figures/figure023c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023d():
    '''El Subtangram Egípci - Figura 4'''

    name = "figures/figure023d"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (4*X,4*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023e():
    '''El Subtangram Egípci - Figura 5'''

    name = "figures/figure023e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (3*X,4*X)
    C = (4*X,4*X)
    D = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023f():
    '''El Subtangram Egípci - Figura 6'''

    name = "figures/figure023f"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (6*X,4*X)
    D = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023g():
    '''El Subtangram Egípci - Figura 7'''

    name = "figures/figure023g"

    X = 1 # Scale #
    A = (  0,  0)
    B = (3*X,4*X)
    C = (7*X,4*X)
    D = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023h():
    '''El Subtangram Egípci - Figura 8'''

    name = "figures/figure023h"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (4*X,4*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure023i():
    '''El Subtangram Egípci - Figura 9'''

    name = "figures/figure023i"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,1*X)
    C = (4*X,4*X)
    D = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure024a():
    '''El Tangram Egípci - Triangle 1:2'''

    name = "figures/figure024a"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (1*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure024b():
    '''El Tangram Egípci - Triangle 2:4'''

    name = "figures/figure024b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (2*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure024c():
    '''El Tangram Egípci - Triangle sqrt(5):2*sqrt(5)'''

    name = "figures/figure024c"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (1*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure024d():
    '''El Tangram Egípci - Triangle 3:6'''

    name = "figures/figure024d"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,6*X)
    C = (3*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure024e():
    '''El Tangram Egípci - Triangle 4:8'''

    name = "figures/figure024e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,8*X)
    C = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure024f():
    '''El Tangram Egípci - Triangle 2*sqrt(5):4*sqrt(5)'''

    name = "figures/figure024f"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,4*X*R5)
    C = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure024g():
    '''El Tangram Egípci - Triangle 5:10:3*sqrt(5)'''

    name = "figures/figure024g"

    X = 1 # Scale #
    A = ( 0*X, 0*X)
    B = ( 4*X, 3*X)
    C = (10*X, 0*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure024h():
    '''El Tangram Egípci - Triangle 5:4*sqrt(5):5'''

    name = "figures/figure024h"

    X = 1 # Scale #
    A = (     0,     0)
    B = (2*X*R5,1*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure024i():
    '''El Tangram Egípci - Triangle 5:2*sqrt(5):5'''

    name = "figures/figure024i"

    X = 1 # Scale #
    A = (     0,     0)
    B = (1*X*R5,2*X*R5)
    C = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure024j():
    '''El Tangram Egípci - Triangle 3:4:5'''

    name = "figures/figure024j"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (3*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure025a():
    '''El Tangram Egípci - Suma de figures semblants 1'''

    name = "figures/figure025a"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure025b():
    '''El Tangram Egípci - Suma de figures semblants 2'''

    name = "figures/figure025b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure025c():
    '''El Tangram Egípci - Suma de figures semblants 3'''

    name = "figures/figure025c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (4*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure025d():
    '''El Tangram Egípci - Suma de figures semblants 4'''

    name = "figures/figure025d"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,1*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (3*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure025e():
    '''El Tangram Egípci - Suma de figures semblants 5'''

    name = "figures/figure025e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,2*X)
    C = (4*X,4*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure025f():
    '''El Tangram Egípci - Suma de figures semblants 6'''

    name = "figures/figure025f"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,1*X)
    C = (2*X,2*X)
    D = (3*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026a():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026a"

    X = 1.0 # Scale #
    A = (     0,      0)
    B = (1*X*R5, 2*X*R5)
    C = (2*X*R5,      0)

    D = w_point(A,B, 5.0-X*R5,X*R5)
    E = (       - 3*X, 4*X)

    F = w_point(C,B, 5.0-X*R5,X*R5)
    G = (2*X*R5 + 3*X, 4*X)
    H = w_point(F,G, 1,1)
    I = w_point(C,G, 2,3)
    J = w_point(H,G, 1,1)
    K = s_point(I,J, 1)


    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*D),
                              path.lineto(*B),
                              path.lineto(*F),
                              path.lineto(*H),
                              path.lineto(*K),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026b():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026b"

    X = 1.0 # Scale #
    A = (  0,   0)
    B = (  0, 2*X)
    C = (2*X, 2*X)
    D = (2*X + 9*X/5.0, 2*X + 12*X/5.0)
    E = (7*X, 2*X)
    F = (7*X, 1*X)
    G = (5*X,   0)

    H = (6.5*X,   0)
    I = (H[0] + X*R5/5.0, 2*X/R5)
    J = (H[0] + X*R5,   0)



    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026c():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026c"

    X = 1.0 # Scale #
    A = (  0, 1*X)
    B = (  0, 2*X)
    C = (7*X, 2*X)
    D = (3*X, 0)
    E = (2*X, 0)


    F = (  0, 2.25*X)
    G = (3*X, 2.25*X)
    H = (3*X, 6.25*X)
    I = (3.25*X, 2.25*X)
    J = (3.25*X + R5*X, 2.25*X)
    K = (3.25*X, 2.25*X + 2*R5*X)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*I),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026d():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026d"

    X = 1.0 # Scale #
    A = (     0,          0)
    B = (1*X*R5,     2*X*R5)
    C = (2*X*R5,          0)
    D = (1*X*R5-5*X, 2*X*R5)
    E = (1*X*R5+5*X, 2*X*R5)
    F = w_point(A,B, X*R5, 5-X*R5)
    G = w_point(C,B, X*R5, 5-X*R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*G),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026e():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026e"

    X = 1.0 # Scale #
    A = (     0,      0)
    B = (     0, 1*X*R5)
    C = (1*X*R5, 3*X*R5)
    D = (2*X*R5, 1*X*R5)
    E = (2*X*R5,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026f():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026f"

    X = 1.0 # Scale #
    A = (      0,      0)
    C = (-1*X*R5, 2*X*R5)
    D = ( 1*X*R5, 2*X*R5)

    I = w_point(A,C, 1,4)
    J = w_point(A,D, 1,4)
    K = w_point(C,D, 1,1)
    B = s_point(K,I, 1)
    E = s_point(K,J, 1)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026g():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026g"

    X = 1.0 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (2*X,6*X)
    D = (4*X,6*X)
    E = (4*X,4*X)
    F = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026h():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026h"

    X = 1.0 # Scale #


    A  = (         0,       0)
    B  = (1*X*R5,       2*X*R5)
    A1 = (2*X*R5-4*X,       0)
    A2 = (2*X*R5-4*X,     2*X)
    A3 = w_point(A,B, 3,2)
    C  = (2*X*R5-3*X,   2*X*R5)
    D  = (2*X*R5-3*X,   2*X*R5+1*X)
    E  = (2*X*R5-1*X,   2*X*R5+2*X)
    F  = (2*X*R5-1.25*X,   2*X*R5+2.5*X)
    G  = (2*X*R5-0.25*X,   2*X*R5+2.5*X)
    H  = (2*X*R5-0.25*X,   2*X*R5+0.5*X)
    I  = (2*X*R5,       2*X*R5)
    J  = (2*X*R5,       0)

    drawing = []
    drawing.append((path.path(path.moveto(*A1),
                              path.lineto(*A2),
                              path.lineto(*A3),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.lineto(*J),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026i():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026i"

    X = 1.0 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (-2*X*R5,1*X*R5)
    D = (-2*X*R5,2*X*R5)
    E = (-4*X*R5,1*X*R5)
    F = (-2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026j():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026j"

    X = 1.0 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)

    D = (    0-X*R3,      0)
    E = (    0-X*R3, 2*X*R5)
    F = (-X*R5-X*R3, 2*X*R5)
    G = (-X*R5-X*R3,      0)
    
    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026k():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026k"

    X = 1.0 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (2*X*R5,2*X*R5)
    E = (4*X*R5,1*X*R5)
    F = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026l():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026l"

    X = 1.0 # Scale #
    A = (      0,     0)
    B = (      0,2*X*R5)
    C = (-4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026m():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026m"

    X = 1.0 # Scale #
    A = (      0,      0)
    B = (      0, 2*X*R5)
    C = ( 2*X*R5, 2*X*R5)
    D = ( 2*X*R5,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026n():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026n"

    X = 1.0 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (2*X*R5,2*X*R5)
    E = (3*X*R5,2*X*R5)
    F = (3*X*R5,     0)
    G = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure026o():
    '''El Tangram Egípci - Figura realista'''

    name = "figures/figure026o"

    X = 1.0 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (-2*X*R5,1*X*R5)
    D = (-2*X*R5,2*X*R5)
    E = (-3*X*R5,2*X*R5)
    F = (-3*X*R5,     0)
    G = (-2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*F),
                              path.lineto(*G),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure028a():
    '''El Puzzle Egipci'''

    name = "figures/figure028a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(B, C, 1,1)
    G = w_point(C, E, 3,2)
    H = w_point(C, E, 1,4)
    I = w_point(A, F, 3,2)
    J = w_point(A, F, 1,4)
    K = w_point(A, B, 1,1)
    L = w_point(D, C, 1,1)
    M = w_point(J, B, 1,1)
    N = w_point(G, C, 1,1)
    O = w_point(I, J, 1,1)
    P = w_point(G, H, 1,1)
    Q = w_point(A, I, 1,1)
    R = w_point(H, D, 1,1)


    drawing = []
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*F),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*K),
                              path.lineto(*I),
                              path.lineto(*A),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*H),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*C),
                              path.lineto(*G),
                              path.lineto(*J),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*O),
                              path.lineto(*G),
                              path.lineto(*H),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*J),
                              path.lineto(*I),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*D),
                              path.lineto(*H),
                              path.lineto(*G),
                              path.lineto(*L),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*L),
                              path.moveto(*K),
                              path.lineto(*D),
                              path.moveto(*A),
                              path.lineto(*F),
                              path.moveto(*E),
                              path.lineto(*C),
                              path.moveto(*O),
                              path.lineto(*G)), BASE+THICK))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+THICK))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029a():
    '''Quadrilaters del Tangram Egípci - Figura 1'''

    name = "figures/figure029a"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (2*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029b():
    '''Quadrilaters del Tangram Egípci - Figura 2'''

    name = "figures/figure029b"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (5*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029c():
    '''Quadrilaters del Tangram Egípci - Figura 3'''

    name = "figures/figure029c"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,4*X)
    C = (4*X,4*X)
    D = (6*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029d():
    '''Quadrilaters del Tangram Egípci - Figura 4'''

    name = "figures/figure029d"

    X = 1 # Scale #
    A = (  0,4*X)
    B = (2*X,4*X)
    C = (10*X,0)
    D = (2*X,0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029e():
    '''Quadrilaters del Tangram Egípci - Figura 5'''

    name = "figures/figure029e"

    X = 1 # Scale #
    A = (  0,  0)
    B = (0.89*X,4.92*X)
    C = (2*X*R5, 1*X*R5)
    D = (4*X*R5, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*C)), BASE+DASHED+THICK+COLOR(WHITE)))
    #drawing.append((path.path(path.moveto(*B),
    #                          path.lineto(*D)), BASE+DASHED+THICK+COLOR(BLACK)))


    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029f():
    '''Quadrilaters del Tangram Egípci - Figura 6'''

    name = "figures/figure029f"

    X = 1 # Scale #
    A = (  0,  0)
    B = (-0.4*X,2.2*X)
    C = (4*X,3*X)
    D = (10*X, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*C)), BASE+DASHED+THICK+COLOR(WHITE)))
    #drawing.append((path.path(path.moveto(*B),
    #                          path.lineto(*D)), BASE+DASHED+THICK+COLOR(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029g():
    '''Quadrilaters del Tangram Egípci - Figura 7'''

    name = "figures/figure029g"

    X = 1 # Scale #
    A = (  0,  0)
    B = (3*X,4*X)
    C = (5*X,4*X)
    D = (8*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.circle(4*X, 2*X, 2*X), BASE+DASHED+THICK+COLOR(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029h():
    '''Quadrilaters del Tangram Egípci - Figura 8'''

    name = "figures/figure029h"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (5*X,4*X)
    D = (7*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029i():
    '''Quadrilaters del Tangram Egípci - Figura 9'''

    name = "figures/figure029i"

    X = 1 # Scale #
    A = (     0,     0)
    B = (1*X*R5,2*X*R5)
    C = (2*X*R5,2*X*R5)
    D = (3*X*R5,     0)
    E = (1.5*X*R5,0.5*X*R5)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    #drawing.append((path.circle(1.5*X*R5, 0.5*X*R5, X*5/R2), BASE+DASHED+THICK+COLOR(RED)))
    drawing.append((path.path(path.moveto(*D),
                              path.arc(E[0],E[1], X*5/R2, -18.43, 198.43)), BASE+DASHED+THICK+COLOR(BLACK)))


    print BETA

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029j():
    '''Quadrilaters del Tangram Egípci - Figura 10'''

    name = "figures/figure029j"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (7*X,4*X)
    D = (5*X,  0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029k():
    '''Quadrilaters del Tangram Egípci - Figura 11'''

    name = "figures/figure029k"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,1*X*R5)
    C = (-2*X*R5,2*X*R5)
    D = (-3*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029l():
    '''Quadrilaters del Tangram Egípci - Figura 12'''

    name = "figures/figure029l"

    X = 1 # Scale #
    A = (  0,  0)
    B = (2*X,4*X)
    C = (4*X,3*X)
    D = (10*X, 0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*C)), BASE+DASHED+THICK+COLOR(WHITE)))
    #drawing.append((path.path(path.moveto(*B),
    #                          path.lineto(*D)), BASE+DASHED+THICK+COLOR(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029m():
    '''Quadrilaters del Tangram Egípci - Figura 13'''

    name = "figures/figure029m"

    X = 1 # Scale #
    A = (      0,-1*X*R5)
    B = (-2*X*R5,      0)
    C = (      0, 1*X*R5)
    D = ( 2*X*R5,      0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029n():
    '''Quadrilaters del Tangram Egípci - Figura 14'''

    name = "figures/figure029n"

    X = 1 # Scale #
    A = (   0,-3*X)
    B = (-4*X,   0)
    C = (   0, 2*X)
    D = ( 4*X,   0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C),
                              path.moveto(*B),
                              path.lineto(*D)), BASE+DASHED+THICK+COLOR(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029o():
    '''Quadrilaters del Tangram Egípci - Figura 15'''

    name = "figures/figure029o"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,5*X)
    C = (4*X,3*X)
    D = s_point(A, C, 2*R5/5.0)
    E = s_point(B, C, 5/(2*R5))

    drawing = []
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*E),
    #                          path.moveto(*B),
    #                          path.lineto(*D)), BASE+DASHED+THICK+COLOR(BLACK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s+[trafo.rotate(-(90-3*BETA)/2.0)])

    mycanvas.writePDFfile(name)


def figure029p():
    '''Quadrilaters del Tangram Egípci - Figura 16'''

    name = "figures/figure029p"

    X = 1 # Scale #
    A = (      0,      0)
    B = (1*X*R10,1*X*R10)
    C = (      0,2*X*R10)
    D = (3*X*R10,1*X*R10)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*C)), BASE+DASHED+THICK+COLOR(BLACK)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*D)), BASE+DASHED+THICK+COLOR(WHITE)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029q():
    '''Quadrilaters del Tangram Egípci - Figura 17'''

    name = "figures/figure029q"

    X = 1 # Scale #
    A = (  0,  0)
    B = (  0,5*X)
    C = (4*X,3*X)
    D = (8*X,6*X)
    E = (8*X,1*X)

    drawing = []
    #drawing.append((path.path(path.moveto(*A),
    #                          path.lineto(*E),
    #                          path.moveto(*B),
    #                          path.lineto(*D)), BASE+DASHED+THICK+COLOR(BLACK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure029r():
    '''Quadrilaters del Tangram Egípci - Figura 18'''

    name = "figures/figure029r"

    X = 1 # Scale #
    A = (     0,     0)
    B = (     0,2*X*R5)
    C = (2*X*R5,1*X*R5)
    D = (4*X*R5,2*X*R5)
    E = (4*X*R5,     0)

    drawing = []
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*E),
                              path.moveto(*B),
                              path.lineto(*D)), BASE+DASHED+THICK+COLOR(BLACK)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*C),
                              path.lineto(*D),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.closepath()), BASE+COLOR(CHALK)+FILLED(CHALK)))

    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


def figure030a():
    '''Golden Rectangle'''

    name = "figures/figure030a"

    X = 2*R5
    A = (0,0)
    B = (0,X)
    C = (X,X)
    D = (X,0)
    E = w_point(A, D, 1,1)
    F = w_point(A, B, 1,1)
    G = w_point(B, C, 1,1)
    H = w_point(C, D, 1,1)
    I = w_point(B, E, 3,2)
    J = w_point(E,C, 5-R5, R5)
    K = ((X*(1.0+R5))/2., 0)
    L = ((X*(1.0+R5))/2., X)
    drawing = []


    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*B),
                              path.lineto(*L),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+DASHED))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*I),
                              path.lineto(*C),
                              path.closepath()), BASE+THICK+FILLED(YELLOW)))
    drawing.append((path.path(path.moveto(*A),
                              path.lineto(*F),
                              path.lineto(*I),
                              path.lineto(*E),
                              path.closepath()), BASE+THICK+FILLED(ORANGE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*I),
                              path.lineto(*F),
                              path.closepath()), BASE+THICK+FILLED(RED)))
    drawing.append((path.path(path.moveto(*E),
                              path.lineto(*J),
                              path.lineto(*K),
                              path.closepath()), BASE+THICK+FILLED(GREEN)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*C),
                              path.lineto(*I),
                              path.closepath()), BASE+THICK+FILLED(BLUE)))
    drawing.append((path.path(path.moveto(*B),
                              path.lineto(*E),
                              path.lineto(*C),
                              path.lineto(*F)), BASE+THICK))
    
    mycanvas = canvas.canvas()
    for (p, s) in drawing: mycanvas.stroke(p, s)
    mycanvas.writePDFfile(name)


################################################################################

if __name__ == "__main__":

    figure000a()
    figure000b()
    figure000c()
    figure000d()
    figure000e()
    figure001a()
    figure001b()
    figure001c()
    figure001d()
    figure001e()
    figure001f()
    figure001g()
    figure001h()
    figure002a()
    figure002b()
    figure002c()
    figure002d()
    figure002e()
    figure002f()
    figure002g()
    figure002h()
    figure002i()
    figure003a()
    figure003b()
    figure003c()
    figure004a()
    figure004b()
    figure004c()
    figure004d()
    figure004e()
    figure004f()
    figure004g()
    figure004h()
    figure004i()
    figure004j()
    figure004k()
    figure005a()
    figure005b()
    figure005c()
    figure006a()
    figure006b()
    figure006c()
    figure006d()
    figure006e()
    figure006f()
    figure006g()
    figure006h()
    figure007a()
    figure007b()

    figure019()
    figure019b()
    figure019c()
    figure019d()
    figure019e()
    figure020a()
    figure020b()
    figure020c()
    figure020d()
    figure020e()
    figure020f()
    figure020g()
    figure020h()
    figure020i()
    figure020j()
    figure020k()
    figure020l()
    figure020m()
    figure021a()
    figure021b()
    figure021c()
    figure022a()
    figure022b()
    figure022c()
    figure022d()
    figure022e()
    figure022f()
    figure022g()
    figure022h()
    figure022i()
    figure022j()
    figure022k()
    figure022l()
    figure022m()
    figure022n()
    figure022o()
    figure022p()
    figure022q()
    figure022r()
    figure022s()
    figure022t()
    figure022u()
    figure022v()
    figure022w()
    figure022x()
    figure023a()
    figure023b()
    figure023c()
    figure023d()
    figure023e()
    figure023f()
    figure023g()
    figure023h()
    figure023i()
    figure024a()
    figure024b()
    figure024c()
    figure024d()
    figure024e()
    figure024f()
    figure024g()
    figure024h()
    figure024i()
    figure024j()
    figure025a()
    figure025b()
    figure025c()
    figure025d()
    figure025e()
    figure025f()
    figure026a()
    figure026b()
    figure026c()
    figure026d()
    figure026e()
    figure026f()
    figure026g()
    figure026h()
    figure026i()
    figure026j()
    figure026k()
    figure026l()
    figure026m()
    figure026n()
    figure026o()
    figure028a()
    figure030a()