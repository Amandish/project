
from tkinter import *

root = Tk()

#the title of the program
root.title("Simple Keyboard")

e = Entry(root, width=45, borderwidth=7)
e.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

def button_click(letter):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(letter))
    #button to use when clearing whats in the "keyboard string"
def button_clear():
    e.delete(0, END)


    # define buttons
    #this is where I have defined the buttons and how big they should be
    #the button_click is what will show up when you press the key named in text

button_A = Button (root, text="A", padx=40, pady=20, command=lambda:button_click(A))
button_B = Button (root, text="B", padx=40, pady=20, command=lambda:button_click(B))
button_C = Button (root, text="C", padx=40, pady=20, command=lambda:button_click(C))
button_D = Button (root, text="D", padx=40, pady=20, command=lambda:button_click(D))
button_E = Button (root, text="E", padx=40, pady=20, command=lambda:button_click(E))
button_F = Button (root, text="F", padx=40, pady=20, command=lambda:button_click(F))
button_G = Button (root, text="G", padx=40, pady=20, command=lambda:button_click(G))
button_H = Button (root, text="H", padx=40, pady=20, command=lambda:button_click(H))
button_I = Button (root, text="I", padx=40, pady=20, command=lambda:button_click(I))
button_J = Button (root, text="J", padx=40, pady=20, command=lambda:button_click(J))
button_K = Button (root, text="K", padx=40, pady=20, command=lambda:button_click(K))
button_L = Button (root, text="L", padx=40, pady=20, command=lambda:button_click(L))
button_M = Button (root, text="M", padx=40, pady=20, command=lambda:button_click(M))
button_N = Button (root, text="N", padx=40, pady=20, command=lambda:button_click(N))
button_O = Button (root, text="O", padx=40, pady=20, command=lambda:button_click(O))
button_P = Button (root, text="P", padx=40, pady=20, command=lambda:button_click(P))
button_Q = Button (root, text="Q", padx=40, pady=20, command=lambda:button_click(Q))
button_R = Button (root, text="R", padx=40, pady=20, command=lambda:button_click(R))
button_S = Button (root, text="S", padx=40, pady=20, command=lambda:button_click(S))
button_T = Button (root, text="T", padx=40, pady=20, command=lambda:button_click(T))
button_U = Button (root, text="U", padx=40, pady=20, command=lambda:button_click(U))
button_V = Button (root, text="V", padx=40, pady=20, command=lambda:button_click(V))
button_W = Button (root, text="W", padx=40, pady=20, command=lambda:button_click(W))
button_X = Button (root, text="X", padx=40, pady=20, command=lambda:button_click(X))
button_Y = Button (root, text="Y", padx=40, pady=20, command=lambda:button_click(Y))
button_Z = Button (root, text="Z", padx=40, pady=20, command=lambda:button_click(Z))

button_clear = Button (root, text="Clear", padx=180, pady=20, command=button_clear)


# put the buttons on the screen
# this is where the keys are placed on the screen

button_A.grid(row=3, column=1)
button_B.grid(row=3, column=2)
button_C.grid(row=3, column=3)

button_D.grid(row=2, column=1)
button_E.grid(row=2, column=2)
button_F.grid(row=2, column=3)

button_G.grid(row=1, column=1)
button_H.grid(row=1, column=2)
button_I.grid(row=1, column=3)

button_J.grid(row=3, column=4)
button_K.grid(row=3, column=5)
button_L.grid(row=3, column=6)

button_M.grid(row=2, column=4)
button_N.grid(row=2, column=5)
button_O.grid(row=2, column=6)

button_P.grid(row=1, column=4)
button_Q.grid(row=1, column=5)
button_R.grid(row=1, column=6)

button_S.grid(row=3, column=7)
button_T.grid(row=3, column=8)
button_U.grid(row=3, column=9)

button_V.grid(row=2, column=7)
button_W.grid(row=2, column=8)
button_X.grid(row=2, column=9)

button_Y.grid(row=1, column=7)
button_Z.grid(row=1, column=8)

button_clear.grid(row=4, column=4, columnspan=3)

    
root.mainloop()
