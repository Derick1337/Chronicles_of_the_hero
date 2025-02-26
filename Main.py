import pyxel as px
import time
from music import play_song

play_song()

class LaunchScreen: # Classe para a tela inicial do jogo
    def __init__(self):
        px.init(250, 250, title="Chronicles of the Hero", fps=30) 
        px.image(0).load(0, 0, "launch_screen.png") # Carrega a imagem da tela inicial
        self.show_initial_menu = False  #Variável de controle para mostrar o menu inicial
        self.initial_menu = Initial_Menu()  # Instancia a classe Initial_Menu
        px.run(self.update, self.draw) 


    def update(self):
        if px.btnp(px.KEY_SPACE): # Se a tecla SPACE for pressionada, atualiza a variável de controle
            self.show_initial_menu = True
            

    def draw(self):
        if self.show_initial_menu: # Se a variável de controle for True, mostra o menu inicial
            px.cls(0)
            self.initial_menu.update()  # Atualiza a classe Initial_Menu
            self.initial_menu.draw()    # Desenha a classe Initial_Menu
        else:
            px.cls(0) # Limpa a tela inicial
            px.blt(0, 0, 0, 0, 0, 250, 250) # Desenha a tela inicial
            px.text(80, 200, "Press SPACE to start", px.COLOR_WHITE) # Mostra a mensagem para iniciar o jogo


class Initial_Menu: # Classe para o menu inicial
    def __init__(self):
        px.image(1).load(0, 0, "menu.png")  # Carrega a imagem do menu inicial
        self.selected_option = 0 # Opção selecionada no menu
        self.menu_options = ["Start Game", "Story", "Exit"] # Opções do menu
       

    def update(self): 
        if px.btnp(px.KEY_DOWN): # Se a tecla DOWN for pressionada, atualiza a opção selecionada
            self.selected_option = (self.selected_option + 1) % len(self.menu_options)

        elif px.btnp(px.KEY_UP): # Se a tecla UP for pressionada, atualiza a opção selecionada
            self.selected_option = (self.selected_option - 1) % len(self.menu_options)

        if px.btnp(px.KEY_Q): # Se a tecla Q for pressionada, executa a ação da opção selecionada
            selected_action = self.menu_options[self.selected_option]
            if selected_action == "Start Game": # Se a opção selecionada for "Start Game", inicia o jogo
                game = Game()
                px.run(game.update, game.draw)
                
            elif selected_action == "Story": # Se a opção selecionada for "Story", mostra a tela de história
                story_screen = StoryScreen()
                px.run(story_screen.update, story_screen.draw)

            elif selected_action == "Exit": # Se a opção selecionada for "Exit", fecha o jogo
                px.quit()

    def draw(self):
        px.blt(0, 0, 1, 0, 0, 250, 250, 0)  # Desenha a imagem do menu inicial na tela
        px.text(160,240,"Press Q to select", px.COLOR_WHITE) # Mostra a mensagem para selecionar uma opção

        for i, option in enumerate(self.menu_options): # Desenha as opções do menu
            if i == self.selected_option:
                px.text(100, 85 + 40 * i + 45, option, 8)
            else:
                px.text(100, 85 + 40 * i + 45, option,14)



class StoryScreen: # Classe para a tela de história
    def __init__(self):
        px.image(0).load(0, 0, 'story.png') # Carrega a imagem da tela de história


    def update(self):
        if px.btnp(px.KEY_B): # Se a tecla B for pressionada, volta para o menu inicial
            self.back_to_menu()


    def draw(self): 
        px.cls(0)
        px.blt(0, 0, 0, 0, 0, 250, 250) # Desenha a imagem da tela de história
        px.text(160, 240, "Press B to turn back", px.COLOR_WHITE) # Mostra a mensagem para voltar para o menu inicial


    def back_to_menu(self): # Função para voltar para o menu inicial
        initial_menu = Initial_Menu()
        px.run(initial_menu.update, initial_menu.draw)


class PauseMenu: # Classe para o menu de pausa
    def __init__(self):
        self.is_paused = False # Variável de controle para pausar o jogo

        self.selected_option = 0 # Opção selecionada no menu
        self.options = ["Resume Game", "Restart", "Back to Menu"] # Opções do menu

        self.arrow_y = 0 # Posição y da seta
        self.arrow_x = 65 # Posição x da seta

        self.menu_x = 50 # Posição x do menu
        self.menu_y = 80 # Posição y do menu
        self.menu_width = 150 # Largura do menu
        self.menu_height = 80 # Altura do menu

        self.return_to_menu = False # Variável de controle para voltar para o menu inicial



    def update(self):
        if px.btnp(px.KEY_M):
            self.is_paused = not self.is_paused  # Alterna entre pausado e não pausado

        if self.is_paused: # Se o jogo estiver pausado, atualiza o menu de pausa
            if self.return_to_menu == True: # Se a variável de controle for True, volta para o menu inicial
                initial_menu = Initial_Menu()
                px.run(initial_menu.update, initial_menu.draw)

            if px.btnp(px.KEY_DOWN): # Se a tecla DOWN for pressionada, atualiza a opção selecionada
                self.selected_option = (self.selected_option + 1) % len(self.options)

            elif px.btnp(px.KEY_UP): # Se a tecla UP for pressionada, atualiza a opção selecionada
                self.selected_option = (self.selected_option - 1) % len(self.options)

            if px.btnp(px.KEY_Q): # Se a tecla Q for pressionada, executa a ação da opção selecionada
                if self.selected_option == 0: # Se a opção selecionada for "Resume Game", despausa o jogo
                    self.is_paused = False

                elif self.selected_option == 1: # Se a opção selecionada for "Restart", reinicia o jogo
                    self.is_paused = False
                    self.restart_game()  

                elif self.selected_option == 2: # Se a opção selecionada for "Back to Menu", volta para o menu inicial
                    self.return_to_menu = True  


    def draw(self): # Função para desenhar o menu de pausa
        if self.is_paused: # Se o jogo estiver pausado, desenha o menu de pausa
            px.rect(self.menu_x, self.menu_y, self.menu_width, self.menu_height, 10) # Desenha o menu de pausa
            px.rectb(self.menu_x, self.menu_y, self.menu_width, self.menu_height, 9) # Desenha a borda do menu de pausa 

            px.text(100, 85, "Pause Menu", 9)  # Desenha o título do menu de pausa
            px.text(130, 150, "Press Q to select", px.COLOR_WHITE) # Mostra a mensagem para selecionar uma opção

            self.arrow_y = 100 + self.selected_option * 20  # Atualiza a posição y da seta
            px.rect(self.arrow_x, self.arrow_y,5,5,9) # Desenha a seta
              
            for i, option in enumerate(self.options): # Desenha as opções do menu
                px.text(80, self.menu_y + 20 * i + 20, option, 9)


    def restart_game(self): # Função para reiniciar o jogo
        self.is_paused = False # Atualiza a variável de controle para despausar o jogo
        game = Game()
        px.run(game.update, game.draw)



class GameOver: # Classe para a tela de game over
    def __init__(self, winning_player): # Recebe o jogador vencedor como parâmetro
        self.winning_player = winning_player
        self.show_game_over = True # Variável de controle para mostrar a tela de game over
        self.current_image = 0 # Imagem atual
        self.previous_time = time.time() 
        self.toggle_time = 0.1 # Define o tempo de alternância em segundos entre as imagens


    def update(self):
        if self.winning_player == 1: # Se o jogador 1 vencer, carrega a imagem correspondente
            self.load_images("player1_win.png")

        elif self.winning_player == 2: # Se o jogador 2 vencer, carrega a imagem correspondente
            self.load_images("player2_win.png")

        self.current_time = time.time() 

        if self.current_time - self.previous_time >= self.toggle_time:
            self.toggle_images()
            self.previous_time = self.current_time

        self.quit()
        self.restart()

    def draw(self): # Função para desenhar a tela de game over, de acordo com o jogador vencedor e realizando uma animação de piscar entre as imagens, inspirado nos jogos de luta antigos
        px.cls(0)
        px.blt(0, 0, self.current_image, 0, 0, 250, 250) # Desenha a imagem atual na tela
        
        px.text(85, 240, "Press R to restart", px.COLOR_WHITE) # Mostra a mensagem para reiniciar o jogo

    def load_images(self, image1): # Função para carregar as imagens da tela de game over
        px.image(0).load(0, 0, image1)
        px.image(1).load(0, 0, "blink.png")

    def toggle_images(self): # Função para alternar entre as imagens
        self.current_image = 1 - self.current_image

    def quit(self): # Função para fechar o jogo
        if px.btn(px.KEY_ESCAPE):
            px.quit()

    def restart(self): # Função para reiniciar o jogo
        if px.btn(px.KEY_R):
            game = Game()
            px.run(game.update, game.draw)


class Character1:  # Classe para o personagem 1
    def __init__(self, x, y, image, u, v, w, h): # Construtor da classe que recebe as coordenadas x e y, a imagem de origem, a posição u e v, a largura e altura
        self.x = x
        self.y = y
        self.new_x = x
        self.new_y = y
        self.image = image
        self.u = u
        self.v = v
        self.w = w
        self.h = h

        self.right = [0, 14, 28, 42] # Posições das sprites do personagem para a direita
        self.left = [0, 14, 28, 42]  # Posições das sprites do personagem para a esquerda
        self.up = [0, 14, 28, 42]   # Posições das sprites do personagem para cima
        self.down = [0, 14, 28, 42] # Posições das sprites do personagem para baixo

        self.weapon_right = [110, 125] # Posições das sprites da espada para a direita
        self.effect_right = [135,200, 120] # Posições das sprites do efeito da espada para a direita
        self.weapon_left = [130, 115] # Posições das sprites da espada para a esquerda
        self.effect_left = [125,200,109] # Posições das sprites do efeito da espada para a esquerda
        self.weapon_down = [88, 101] # Posições das sprites da espada para baixo
        self.effect_down = [94,200,101] # Posições das sprites do efeito da espada para baixo
        self.weapon_up = [61, 75] # Posições das sprites da espada para cima
        self.effect_up = [59,200,69] # Posições das sprites do efeito da espada para cima

        self.animation_frame = 0  # Frame da animação do personagem
        self.direction = 'right' # Inicializa o personagem virado para a direita
        self.weapon_animation_frame = 0 # Frame da animação da espada
        self.effect_animation_frame = 0 # Frame da animação do efeito da espada

        self.health = 60 # Vida do personagem

        self.load_assets() # Carrega os assets do personagem


    def draw(self): # Funcao para desenhar o personagem e suas animacoes na tela
        self.draw_character()
        self.direction_animation()
        self.weapon_animation()

    def update(self):  # Funcao para atualizar o personagem
        self.move()
        self.attack()

        if not self.check_collision(self.new_x, self.new_y): # Se não houver colisão, atualiza as coordenadas do personagem
            self.x = self.new_x
            self.y = self.new_y

        self.out_map_saver() # Função para manter o personagem dentro do mapa


    def load_assets(self):  # Funcao para carregar os assets do personagem
        px.image(0).load(0, 0, "assets.png")


    def draw_character(self):  # Funcao para desenhar o personagem
        if self.direction == 'down': # Se o personagem estiver virado para baixo, desenha a sprite correspondente
            px.blt(self.x, self.y, 0,
                   self.down[self.animation_frame], 0, 14, 18, 6)
            
        elif self.direction == 'up': # Se o personagem estiver virado para cima, desenha a sprite correspondente
            px.blt(self.x, self.y, 0,
                   self.up[self.animation_frame], 18, 14, 18, 6)
            
        elif self.direction == 'left': # Se o personagem estiver virado para a esquerda, desenha a sprite correspondente
            px.blt(self.x, self.y, 0,
                   self.left[self.animation_frame], 36, 14, 18, 6)
            
        elif self.direction == 'right': # Se o personagem estiver virado para a direita, desenha a sprite correspondente
            px.blt(self.x, self.y, 0,
                   self.right[self.animation_frame], 54, 14, 18, 6)


    def move(self):  # Funcao para mover o personagem
        self.new_x = self.x 
        self.new_y = self.y


        if px.btn(px.KEY_W): # Se a tecla UP for pressionada, atualiza a posição do personagem
            self.new_y = self.y - 2
            self.direction = 'up'
            self.animation_frame = (self.animation_frame + 1) % 4

        elif px.btn(px.KEY_S): # Se a tecla DOWN for pressionada, atualiza a posição do personagem
            self.new_y = self.y + 2
            self.direction = 'down'
            self.animation_frame = (self.animation_frame + 1) % 4

        elif px.btn(px.KEY_A): # Se a tecla LEFT for pressionada, atualiza a posição do personagem
            self.new_x = self.x - 2
            self.direction = 'left'
            self.animation_frame = (self.animation_frame + 1) % 4

        elif px.btn(px.KEY_D): # Se a tecla RIGHT for pressionada, atualiza a posição do personagem
            self.new_x = self.x + 2
            self.direction = 'right'
            self.animation_frame = (self.animation_frame + 1) % 4 


    def direction_animation(self):  # Funcao para animar o movimento do personagem
        if self.direction == 'down': # Se o personagem estiver virado para baixo, desenha as sprites de movimento correspondentes
            px.blt(self.x, self.y, 0,
                   self.down[self.animation_frame], 0, 14, 18, 6)
            
        elif self.direction == 'up': # Se o personagem estiver virado para cima, desenha as sprites de movimento correspondentes
            px.blt(self.x, self.y, 0,
                   self.up[self.animation_frame], 18, 14, 18, 6)
            
        elif self.direction == 'left': # Se o personagem estiver virado para esquerda, desenha as sprites de movimento correspondentes
            px.blt(self.x, self.y, 0,
                   self.left[self.animation_frame], 36, 14, 18, 6)
            
        elif self.direction == 'right': # Se o personagem estiver virado para direita, desenha as sprites de movimento correspondentes
            px.blt(self.x, self.y, 0,
                   self.right[self.animation_frame], 54, 14, 18, 6)
    

    def weapon_animation(self):  # Funcao para animar o movimento do personagem
        if self.direction == 'down': # Se o personagem estiver virado para baixo, desenha as sprites de movimento da espada correspondentes
            px.blt(self.x, self.y+12, 0, # Desenha a sprite da espada
                   self.weapon_down[self.weapon_animation_frame], 80, 8, 9, 6)
            
            px.blt(self.x, self.y+21, 0, # Desenha a sprite do efeito da espada
            self.effect_down[self.effect_animation_frame], 89, 9, 8, 6)

        elif self.direction == 'up':  # Se o personagem estiver virado para cima, desenha as sprites de movimento da espada correspondentes
            px.blt(self.x+9, self.y, 0, # Desenha a sprite da espada
                   self.weapon_up[self.weapon_animation_frame], 109, 9, 11, 6)
            
            px.blt(self.x+10, self.y-9, 0, # Desenha a sprite do efeito da espada
            self.effect_up[self.effect_animation_frame], 100, 9, 15, 6)

        elif self.direction == 'left':  # Se o personagem estiver virado para esquerda, desenha as sprites de movimento da espada correspondentes
            px.blt(self.x-5, self.y+4, 0, # Desenha a sprite da espada
                   self.weapon_left[self.weapon_animation_frame], 117, 9, 18, 6)
            
            px.blt(self.x-9, self.y+5, 0, # Desenha a sprite do efeito da espada
            self.effect_left[self.effect_animation_frame], 117, 6, 8, 6)

        elif self.direction == 'right':  # Se o personagem estiver virado para direita, desenha as sprites de movimento da espada correspondentes
            px.blt(self.x+8, self.y+6, 0, # Desenha a sprite da espada
                   self.weapon_right[self.weapon_animation_frame], 135, 9, 18, 6)
            
            px.blt(self.x+15, self.y+5, 0, # Desenha a sprite do efeito da espada
                   self.effect_right[self.effect_animation_frame], 135, 6, 8, 6)
            
    def attack(self): # Função para o personagem atacar
        if px.btnp(px.KEY_SPACE): # Se a tecla SPACE for pressionada, executa a animação de ataque
            self.weapon_animation_frame = (self.weapon_animation_frame + 1) % 2
            self.effect_animation_frame = (self.effect_animation_frame + 1) % 3
            self.animation_frame = 0
            return True


    def check_collision(self, new_x, new_y): # Função para verificar se houve colisão do personagem com os objetos do cenário
        collision_rectangles = [
            {'left': 68, 'right': 77, 'top': 78, 'bottom': 90},
            {'left': 85, 'right': 142, 'top': 84, 'bottom': 92},
            {'left': 148, 'right': 159, 'top': 80, 'bottom': 92},
            {'left': 75, 'right': 75, 'top': 105, 'bottom': 110},
            {'left': 155, 'right': 155, 'top': 107, 'bottom': 115},
            {'left': 67, 'right': 75, 'top': 145, 'bottom': 160},
            {'left': 66, 'right': 115, 'top': 153, 'bottom': 160},
            {'left': 120, 'right': 140, 'top': 160, 'bottom': 160},
            {'left': 135, 'right': 147, 'top': 153, 'bottom': 150},
            {'left': 0, 'right': 8, 'top': 0, 'bottom': 250},
            {'left': 150, 'right': 158, 'top': 145, 'bottom': 160},
            {'left': 0, 'right': 250, 'top': 238, 'bottom': 250},
            {'left': 0, 'right': 250, 'top': 0, 'bottom': 10},
            {'left': 240, 'right': 250, 'top': 0, 'bottom': 250},
        ]

        self.new_character_box = [new_x, new_y, new_x + self.w, new_y + self.h] # Cria uma nova hitbox em volta do personagem

        for rect in collision_rectangles: # Verifica se houve colisão entre o retângulo do personagem e os retângulos dos objetos do cenário
            if (self.new_character_box[0] < rect['right'] and 
                self.new_character_box[2] > rect['left'] and
                self.new_character_box[1] < rect['bottom'] and
                    self.new_character_box[3] > rect['top']):
                return True # Se houver colisão, retorna True
        return False # Se não houver colisão, retorna False
    
    def out_map_saver(self):
        if self.x < 10:
            self.x = 10
        elif self.x > 228:
            self.x = 228
        elif self.y < 10:
            self.y = 10
        elif self.y > 215:
            self.y = 215
    

class Character2:  # Classe para o personagem 2
    def __init__(self, x, y, image, u, v, w, h): # Construtor da classe que recebe as coordenadas x e y, a imagem, a posição u e v na imagem de origem, a largura e altura
        self.x = x
        self.y = y
        self.new_x = x
        self.new_y = y
        self.image = image
        self.u = u 
        self.v = v
        self.w = w
        self.h = h
        self.right = [0, 14, 28, 42] # Posições das sprites do personagem para a direita
        self.left = [0, 14, 28, 42] # Posições das sprites do personagem para a esquerda
        self.up = [0, 14, 28, 42] # Posições das sprites do personagem para cima
        self.down = [0, 14, 28, 42] # Posições das sprites do personagem para baixo
        self.animation_frame = 0 # Frame da animação do personagem
        self.direction = 'left' # Inicializa o personagem virado para a esquerda
        self.weapon_right = [110, 125] # Posições das sprites da espada para a direita
        self.effect_right = [135,200, 120] # Posições das sprites do efeito da espada para a direita
        self.weapon_left = [130, 115] # Posições das sprites da espada para a esquerda
        self.effect_left = [125,200,109] # Posições das sprites do efeito da espada para a esquerda
        self.weapon_down = [88, 101] # Posições das sprites da espada para baixo
        self.effect_down = [101,200,94] # Posições das sprites do efeito da espada para baixo
        self.weapon_up = [61, 75] # Posições das sprites da espada para cima
        self.effect_up = [59,200,69] # Posições das sprites do efeito da espada para cima
        self.weapon_animation_frame = 0 # Frame da animação da espada
        self.effect_animation_frame = 0 # Frame da animação do efeito da espada
        self.health = 60 # Vida do personagem
        self.load_assets() # Carrega os assets do personagem


    def draw(self):  # Funcao para desenhar o personagem, a espada e suas animacoes na tela
        self.draw_character()
        self.direction_animation()
        self.weapon_animation()
        

    def update(self):  # Funcao para atualizar o personagem
        self.move()
        self.attack()


        if not self.check_collision(self.new_x, self.new_y): # Se não houver colisão, atualiza as coordenadas do personagem
            self.x = self.new_x
            self.y = self.new_y

        self.out_map_saver() # Função para manter o personagem dentro do mapa


    def load_assets(self):  # Funcao para carregar os assets do personagem
        px.image(0).load(0, 0, "assets.png")


    def draw_character(self):  # Funcao para desenhar o personagem
        if self.direction == 'down': # Se o personagem estiver virado para baixo, desenha a sprite correspondente
            px.blt(self.x, self.y, 0,
                   self.down[self.animation_frame], 80, 14, 18, 6)
            
        elif self.direction == 'up': # Se o personagem estiver virado para cima, desenha a sprite correspondente
            px.blt(self.x, self.y, 0,
                   self.up[self.animation_frame], 98, 14, 18, 6)
            
        elif self.direction == 'left': # Se o personagem estiver virado para a esquerda, desenha a sprite correspondente
            px.blt(self.x, self.y, 0,
                   self.left[self.animation_frame], 117, 14, 18, 6)
            
        elif self.direction == 'right': # Se o personagem estiver virado para a direita, desenha a sprite correspondente
            px.blt(self.x, self.y, 0,
                   self.right[self.animation_frame], 135, 14, 18, 6)


    def move(self):  # Funcao para mover o personagem
        self.new_x = self.x
        self.new_y = self.y

        if px.btn(px.KEY_UP): # Se a tecla W for pressionada, atualiza a posição do personagem
            self.new_y = self.y - 2
            self.direction = 'up'
            self.animation_frame = (self.animation_frame + 1) % 4

        elif px.btn(px.KEY_DOWN): # Se a tecla S for pressionada, atualiza a posição do personagem 
            self.new_y = self.y + 2
            self.direction = 'down'
            self.animation_frame = (self.animation_frame + 1) % 4

        elif px.btn(px.KEY_LEFT): # Se a tecla A for pressionada, atualiza a posição do personagem
            self.new_x = self.x - 2
            self.direction = 'left'
            self.animation_frame = (self.animation_frame + 1) % 4

        elif px.btn(px.KEY_RIGHT): # Se a tecla D for pressionada, atualiza a posição do personagem
            self.new_x = self.x + 2
            self.direction = 'right'
            self.animation_frame = (self.animation_frame + 1) % 4


    def direction_animation(self):  # Funcao para animar o movimento do personagem
        if self.direction == 'down': # Se o personagem estiver virado para baixo, desenha as sprites de movimento correspondentes
            px.blt(self.x, self.y, 0,
                   self.down[self.animation_frame], 80, 14, 18, 6)
            
        elif self.direction == 'up': # Se o personagem estiver virado para cima, desenha as sprites de movimento correspondentes
            px.blt(self.x, self.y, 0,
                   self.up[self.animation_frame], 98, 14, 18, 6)
            
        elif self.direction == 'left': # Se o personagem estiver virado para esquerda, desenha as sprites de movimento correspondentes
            px.blt(self.x, self.y, 0,
                   self.left[self.animation_frame], 117, 14, 18, 6)
            
        elif self.direction == 'right': # Se o personagem estiver virado para direita, desenha as sprites de movimento correspondentes
            px.blt(self.x, self.y, 0,
                   self.right[self.animation_frame], 135, 14, 18, 6)


    def weapon_animation(self):  # Funcao para animar o movimento do personagem
        if self.direction == 'down': # Se o personagem estiver virado para baixo, desenha as sprites de movimento da espada correspondentes
            px.blt(self.x, self.y+12, 0,
                   self.weapon_down[self.weapon_animation_frame], 80, 8, 9, 6)
            
            px.blt(self.x, self.y+21, 0, # Desenha a sprite do efeito da espada
            self.effect_down[self.effect_animation_frame], 89, 9, 8, 6)

        elif self.direction == 'up': # Se o personagem estiver virado para cima, desenha as sprites de movimento da espada correspondentes
            px.blt(self.x+9, self.y, 0,
                   self.weapon_up[self.weapon_animation_frame], 109, 9, 11, 6)
            
            px.blt(self.x+10, self.y-9, 0, # Desenha a sprite do efeito da espada
            self.effect_up[self.effect_animation_frame], 100, 9, 15, 6)

        elif self.direction == 'left': # Se o personagem estiver virado para esquerda, desenha as sprites de movimento da espada correspondentes 
            px.blt(self.x-5, self.y+4, 0,
                   self.weapon_left[self.weapon_animation_frame], 117, 9, 18, 6)
            
            px.blt(self.x-9, self.y+5, 0, # Desenha a sprite do efeito da espada
            self.effect_left[self.effect_animation_frame], 117, 6, 8, 6)

        elif self.direction == 'right': # Se o personagem estiver virado para direita, desenha as sprites de movimento da espada correspondentes
            px.blt(self.x+8, self.y+4, 0,
                   self.weapon_right[self.weapon_animation_frame], 135, 9, 18, 6)
            
            px.blt(self.x+15, self.y+5, 0, # Desenha a sprite do efeito da espada
                   self.effect_right[self.effect_animation_frame], 135, 6, 8, 6)


    def attack(self): # Função para o personagem atacar
        if px.btnp(px.KEY_BACKSPACE): # Se a tecla F for pressionada, executa a animação de ataque
            self.weapon_animation_frame = (self.weapon_animation_frame + 1) % 2
            self.effect_animation_frame = (self.effect_animation_frame + 1) % 3
            self.animation_frame = 0
            return True
    

    def check_collision(self, new_x, new_y): # Função para verificar se houve colisão do personagem com os objetos do cenário
        collision_rectangles = [
            {'left': 68, 'right': 77, 'top': 78, 'bottom': 90},
            {'left': 85, 'right': 142, 'top': 84, 'bottom': 92},
            {'left': 148, 'right': 159, 'top': 80, 'bottom': 92},
            {'left': 75, 'right': 75, 'top': 105, 'bottom': 110},
            {'left': 155, 'right': 155, 'top': 107, 'bottom': 115},
            {'left': 67, 'right': 75, 'top': 145, 'bottom': 160},
            {'left': 66, 'right': 115, 'top': 153, 'bottom': 160},
            {'left': 120, 'right': 140, 'top': 160, 'bottom': 160},
            {'left': 135, 'right': 147, 'top': 153, 'bottom': 150},
            {'left': 0, 'right': 8, 'top': 0, 'bottom': 250},
            {'left': 150, 'right': 158, 'top': 145, 'bottom': 160},
            {'left': 0, 'right': 250, 'top': 238, 'bottom': 250},
            {'left': 0, 'right': 250, 'top': 0, 'bottom': 10},
            {'left': 240, 'right': 250, 'top': 0, 'bottom': 250},
        ]

        self.new_character_box = [new_x, new_y, new_x + self.w, new_y + self.h] # Cria uma nova hitbox em volta do personagem

        for rect in collision_rectangles:
            if (self.new_character_box[0] < rect['right'] and
                self.new_character_box[2] > rect['left'] and
                self.new_character_box[1] < rect['bottom'] and
                    self.new_character_box[3] > rect['top']):
                return True # Se houver colisão, retorna True
        return False # Se não houver colisão, retorna False
    

    def out_map_saver(self): # Função para manter o personagem dentro do mapa, caso o outro o empurre para fora
        if self.x < 10:
            self.x = 10
        elif self.x > 228:
            self.x = 228
        elif self.y < 10:
            self.y = 10
        elif self.y > 215:
            self.y = 215
 


class Game:  # Classe principal do jogo
    def __init__(self):
        self.Map1 = self.load_map() # Carrega o mapa
        self.character1 = Character1(30, 133-18, 0, 76, 0, 14, 22) # Cria um objeto da classe Character1
        self.character2 = Character2(220, 133-18, 0, 76, 80, 14, 22) # Cria um objeto da classe Character2
        self.characters = [self.character1, self.character2] # Lista com os personagens
        self.show_game = True # Variável de controle para mostrar o jogo
        self.game_over = False # Variável de controle para o game over

        self.pause_menu = PauseMenu() # Cria um objeto da classe PauseMenu

        self.rounds_player1 = 0 # Variável para contar os rounds do player 1
        self.rounds_player2 = 0 # Variável para contar os rounds do player 2
        self.total_rounds = 2  # Variável para definir o total de rounds

    def update(self):
        self.pause_menu.update() # Atualiza o menu de pause

        if not self.pause_menu.is_paused: # Se o jogo não estiver pausado, atualiza os personagens
            for character in self.characters:
                character.update()

            self.handle_character_collision(self.character1, self.character2) # Verifica se houve colisão entre os personagens

        if self.character1.direction == 'down' or self.character2.direction == 'down': # Verifica se o personagem está virado para baixo

            if self.check_hit(self.character1.x, self.character1.y, self.character1.w, self.character1.h, # Verifica se houve colisão entre a espada e o personagem 1 e atualiza a vida do personagem 1
                          self.sword_position(self.character2)[0], self.sword_position(self.character2)[1],
                          self.sword_position(self.character2)[2], self.sword_position(self.character2)[3] +2,px.KEY_BACKSPACE):
                          self.update_health(self.character1, 10)                  

            if self.check_hit(self.character2.x, self.character2.y, self.character2.w, self.character2.h, # Verifica se houve colisão entre a espada e o personagem 2 e atualiza a vida do personagem 2
                          self.sword_position(self.character1)[0], self.sword_position(self.character1)[1],
                          self.sword_position(self.character1)[2], self.sword_position(self.character1)[3] +2, px.KEY_SPACE):
                self.update_health(self.character2, 10)

        if self.character1.direction == 'up' or self.character2.direction == 'up': # Verifica se o personagem está virado para cima

            if self.check_hit(self.character1.x, self.character1.y, self.character1.w, self.character1.h, # Verifica se houve colisão entre a espada e o personagem 1 e atualiza a vida do personagem 1
                          self.sword_position(self.character2)[0], self.sword_position(self.character2)[1] -2,
                          self.sword_position(self.character2)[2], self.sword_position(self.character2)[3] ,px.KEY_BACKSPACE):
                          self.update_health(self.character1, 10)                  

            if self.check_hit(self.character2.x, self.character2.y, self.character2.w, self.character2.h, # Verifica se houve colisão entre a espada e o personagem 2 e atualiza a vida do personagem 2
                          self.sword_position(self.character1)[0], self.sword_position(self.character1)[1] -2,
                          self.sword_position(self.character1)[2], self.sword_position(self.character1)[3] , px.KEY_SPACE):
                self.update_health(self.character2, 10)

        if self.character1.direction == 'left' or self.character2.direction == 'left' or self.character1.direction == 'right' or self.character2.direction == 'right': # Verifica se o personagem está virado para a esquerda ou direita
            
            if self.check_hit(self.character1.x, self.character1.y, self.character1.w, self.character1.h, # Verifica se houve colisão entre a espada e o personagem 1 e atualiza a vida do personagem 1
                          self.sword_position(self.character2)[0], self.sword_position(self.character2)[1] ,
                          self.sword_position(self.character2)[2], self.sword_position(self.character2)[3] ,px.KEY_BACKSPACE):
                          self.update_health(self.character1, 10) 

            if self.check_hit(self.character2.x, self.character2.y, self.character2.w, self.character2.h, # Verifica se houve colisão entre a espada e o personagem 2 e atualiza a vida do personagem 2
                          self.sword_position(self.character1)[0], self.sword_position(self.character1)[1] ,
                          self.sword_position(self.character1)[2], self.sword_position(self.character1)[3] , px.KEY_SPACE):
                self.update_health(self.character2, 10)
            

            if self.check_game_over(): # Verifica se o jogo acabou
                self.game_over = GameOver()
            
        
    def draw(self):
        self.pause_menu.draw() # Desenha o menu de pause

        if not self.pause_menu.is_paused: # Se o jogo não estiver pausado, desenha o mapa, os personagens e as barras de vida

            self.draw_map() # Desenha o mapa

            for character in self.characters: # Desenha os personagens
                character.draw()

            self.draw_health_bar(self.character1, self.character1.x - 15, self.character1.y - 15) # Desenha a barra de vida do personagem 1
            self.draw_health_bar(self.character2, self.character2.x - 15, self.character2.y - 15) # Desenha a barra de vida do personagem 2
            px.text(10, 10, f"Player 1: {self.rounds_player1} - Player 2: {self.rounds_player2}", px.COLOR_WHITE) # Desenha o placar dos rounds


    def load_map(self): # Função para carregar o mapa
        px.image(1).load(0, 0, "map1.png")


    def draw_map(self): # Função para desenhar o mapa
        px.blt(0, 0, 1, 0, 0, 250, 250, 0)


    def handle_character_collision(self, character1, character2): # Função para verificar se houve colisão entre os personagens
        if (character1.x < character2.x + character2.w and
            character1.x + character1.w > character2.x and
            character1.y < character2.y + character2.h and
            character1.y + character1.h > character2.y):

            overlap_x = min(character1.x + character1.w, character2.x + character2.w) - max(character1.x, character2.x) 
            overlap_y = min(character1.y + character1.h, character2.y + character2.h) - max(character1.y, character2.y)

            if overlap_x < overlap_y:
                if character1.x < character2.x:
                    character1.x -= overlap_x / 2
                    character2.x += overlap_x / 2
                else:
                    character1.x += overlap_x / 2
                    character2.x -= overlap_x / 2
            else:
                if character1.y < character2.y:
                    character1.y -= overlap_y / 2
                    character2.y += overlap_y / 2
                else:
                    character1.y += overlap_y / 2
                    character2.y -= overlap_y / 2


    def check_hit(self, x, y, w, h, x2, y2, w2, h2, key): # Função para verificar se houve colisão entre a espada e o personagem
        self.character_box = [x, y, x + w , y + h] # Hitbox do personagem
        self.sword_box = [x2, y2, x2 + w2, y2 + h2] # Hitbox da espada

        if px.btnp(key): # Se alguma das teclas de ataque for pressionada, verifica se houve colisão entre a espada do personagem que atacou e outro personagem
            if (self.character_box[0] < self.sword_box[2] and
                self.character_box[2] > self.sword_box[0] and
                self.character_box[1] < self.sword_box[3] and
                self.character_box[3] > self.sword_box[1]):
                return True        


    def draw_health_bar(self, character,x,y): # Função para desenhar a barra de vida, recebe como parâmetro o personagem e as coordenadas x e y
        if character.health >= 60: # Desenha a barra de vida do personagem em 100%
            px.blt(x, y, 0, 0, 72, 43, 8, 6)

        elif character.health >= 50: # Desenha a barra de vida do personagem em 83%
            px.blt(x, y, 0, 0, 72, 36, 8, 6)

        elif character.health >= 40: # Desenha a barra de vida do personagem em 67%
            px.blt(x, y, 0, 0, 72, 29, 8, 6)

        elif character.health >= 30: # Desenha a barra de vida do personagem em 50%
            px.blt(x, y, 0, 0, 72, 22, 8, 6)

        elif character.health >= 20: # Desenha a barra de vida do personagem em 33%
            px.blt(x, y, 0, 0, 72, 15, 8, 6)

        elif character.health >= 10: # Desenha a barra de vida do personagem em 17%
            px.blt(x, y, 0, 0, 72, 8, 8, 6)

        elif character.health <= 0: # Se a vida do personagem for menor ou igual a 0, retorna True
            return True
        

    def sword_position(self, character): # Função para definir a posição da espada do personagem de acordo com a direção do personagem
        if character.direction == 'down': # Se o personagem estiver virado para baixo, retorna a posição da espada
            return [character.x, character.y+12, 8, 9]
        
        elif character.direction == 'up': # Se o personagem estiver virado para cima, retorna a posição da espada
            return [character.x+9, character.y, 9, 11]
        
        elif character.direction == 'left': # Se o personagem estiver virado para esquerda, retorna a posição da espada
            return [character.x-5, character.y+4, 9, 18]
        
        elif character.direction == 'right': # Se o personagem estiver virado para direita, retorna a posição da espada
            return [character.x+8, character.y+4, 9, 18]
            

    def update_health(self,character, damage): # Função para atualizar a vida do personagem
        character.health -= damage
        
        
    def check_game_over(self): # Função para verificar se o jogo acabou
        if self.character1.health <= 0 or self.character2.health <= 0: # Verifica se a vida de algum dos personagens é menor ou igual a 0 
            
            if self.character1.health <= 0: # Se a vida do personagem 1 for menor ou igual a 0, o personagem 2 venceu
                winning_player = 2
            else: #Caso contrário, o personagem 1 venceu
                winning_player = 1

            if self.character1.health <= 0: # Se a vida do personagem 1 for menor ou igual a 0, adiciona 1 ao contador de rounds do personagem 2
                self.rounds_player2 += 1
            else: # Caso contrário, adiciona 1 ao contador de rounds do personagem 1
                self.rounds_player1 += 1


            if self.rounds_player1 >= self.total_rounds or self.rounds_player2 >= self.total_rounds: # Verifica se o total de rounds foi atingido, se sim, o jogo acabou
                self.game_over = True 
                game_over_screen = GameOver(winning_player) # Cria um objeto da classe GameOver
                while self.game_over: # Enquanto o jogo não acabar, atualiza e desenha a tela de game over
                    game_over_screen.update()
                    game_over_screen.draw()
                    px.flip()
            else: # Caso contrário, reinicia o jogo
                self.character1 = Character1(30, 133-18, 0, 76, 0, 14, 22)
                self.character2 = Character2(220, 133-18, 0, 76, 80, 14, 22)
                self.characters = [self.character1, self.character2]



if __name__ == "__main__": # Inicializa o jogo na tela de início
    launch_screen = LaunchScreen() 