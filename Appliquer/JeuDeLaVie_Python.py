import curses
# Fonction à modifier 

def next_state (state,stdscr):
    new_state = state
    count_neighbours = 0
    for i in range(len(state)):
           for j in range(len(state[i])):
                if state[i][j] == "O":
                    if state[i-1][j] == "O":
                    count_neighbours += 1                
                    if state[i-1][j+1] == "O":
                        count_neighbours += 1             
                    if state[i][j+1] == "O":
                        count_neighbours += 1
                    if state[i+1][j+1] == "O":
                        count_neighbours += 1             
                    if state[i+1][j] == "O":
                        count_neighbours += 1  
                    if state[i+1][j-1] == "O":
                        count_neighbours += 1                        
                    if state[i][j-1] == "O":
                        count_neighbours += 1             
                    if state[i-1][j-1] == "O":
                        count_neighbours += 1           
                                    
                             
                        
    # stdscr.addstr(30, 30, "salut")
    return new_state

#def cell_neighbours(state):
    


# Fonction principale, que vous n'avez pas à modifier ;
# stdscr est l'objet qui représente l'écran dans curses
def main (stdscr):
    # On désactive le curseur de texte dans la fenêtre de curses
    curses.curs_set(False) 
    
    # On lit la grille initiale, modifiable dans cells.txt
    text_file = open("cells.txt", "r")
    state = text_file.read().splitlines()

    # Boucle de jeu :
    # Tant que l'input utilisateur est différent de "q", on reste dans le jeu
    key = " "
    while key != "q":
        # On vide l'écran
        stdscr.clear()

        # Préparation de l'affichage ligne par ligne
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == "O":
                    stdscr.addstr(i, j, "O") # attention, curses met y avant x

        # Fonction qui affiche ce qu'on a préparé
        stdscr.refresh()
        
        # La fonction next_state() retourne le prochain état du jeu de la vie
        state = next_state(state,stdscr)

        # Fonction qui attend un input utilisateur
        key = stdscr.getkey()

# Curses s'exécute au sein d'un wrapper, afin de ne pas perturber l'affichage du
# shell lorsqu'on ferme le programme
curses.wrapper(main)