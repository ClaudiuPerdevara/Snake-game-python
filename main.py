import pygame,sys,random
from pygame.examples.go_over_there import screen
from pygame.math import Vector2 #ca sa nu scriu de fiecare data


class FRUIT:
    def __init__(self):
        # coordonate
        self.randomize()
    def draw_fruit(self):
        fruit_rect=pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect(screen,(255,46,0),fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number_line - 1)
        self.y = random.randint(0, cell_number_column - 1)
        self.pos = Vector2(self.x, self.y)
class SNAKE:
    def __init__(self):
        self.body= [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction=Vector2(0,0)

        self.head_up=pygame.image.load('head_up.png').convert_alpha()
        self.head_down=pygame.image.load('head_down.png').convert_alpha()
        self.head_left=pygame.image.load('head_left.png').convert_alpha()
        self.head_right=pygame.image.load('head_right.png').convert_alpha()

        self.tail_up = pygame.image.load('tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('tail_left.png').convert_alpha()
        self.tail_right = pygame.image.load('tail_right.png').convert_alpha()

        self.body_tr = pygame.image.load('body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('body_bl.png').convert_alpha()

        self.body_up = pygame.image.load('body_up.png').convert_alpha()
        self.body_side = pygame.image.load('body_side.png').convert_alpha()

    def draw_snake(self):

        self.update_head()
        self.update_tail()
        for index,block in enumerate(self.body):
            x_pos=int(block.x*cell_size)
            y_pos=int(block.y*cell_size)
            block_rect=pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index==0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body)-1:
                screen.blit(self.tail, block_rect)

            else:
                previous_block = self.body[index+1] - block
                next_block= self.body[index-1] - block
                if previous_block.x==next_block.x:
                    screen.blit(self.body_up,block_rect)
                if previous_block.y == next_block.y:
                    screen.blit(self.body_side, block_rect)
                else:
                    if previous_block.x==-1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==-1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x==1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x==1 and next_block.y==1 or previous_block.y==1 and next_block.x==1:
                        screen.blit(self.body_br,block_rect)
    def update_head(self):
        head_pos=self.body[1]-self.body[0]
        if head_pos==Vector2(1,0): self.head=self.head_left
        elif head_pos == Vector2(-1, 0): self.head = self.head_right
        elif head_pos==Vector2(0,1): self.head=self.head_up
        elif head_pos==Vector2(0,-1): self.head=self.head_down
    def update_tail(self):
        tail_pos=self.body[-2]-self.body[-1]
        if tail_pos==Vector2(1,0): self.tail=self.tail_left
        elif tail_pos == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_pos==Vector2(0,1): self.tail=self.tail_up
        elif tail_pos==Vector2(0,-1): self.tail=self.tail_down
    def move_snake(self):
        body_copy=self.body[:-1] #face copie dar fara ultimul block
        body_copy.insert(0,body_copy[0]+self.direction)
        self.body=body_copy[:]
        # acum vreau sa verifica asta o data la ceva timp
    def add_block(self):
        body_copy = self.body[:]  # face copie dar fara ultimul block
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
    def reset(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction= Vector2(0,0)


class MAIN:
    def __init__(self):
        self.snake= SNAKE()
        self.fruit= FRUIT()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_outside()
        self.check_selfhit()
    def draw_elements(self):
        self.draw_grass()
        self.draw_score()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def check_collision(self):
        if self.fruit.pos==self.snake.body[0]:
            self.fruit.randomize()
            self.fruit.draw_fruit()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    def check_outside(self):
        if not (0<=self.snake.body[0].y<cell_number_column and 0<=self.snake.body[0].x<cell_number_line):
            self.game_over()
    def check_selfhit(self):
        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                self.game_over()
    def game_over(self):
        self.snake.reset()
    def draw_grass(self):
        grass_color=(63, 143, 17)
        for row in range(cell_number_column):
            if row%2==0:
                for col in range(cell_number_line):
                    if col%2==0:
                        grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        screen.blit(texture1,grass_rect)
                    else:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        screen.blit(texture2, grass_rect)
            else:
                for col in range(cell_number_line):
                    if col%2==1:
                        grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        screen.blit(texture1,grass_rect)
                    else:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        screen.blit(texture2, grass_rect)
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface=game_font.render(score_text,True,(56,74,12))
        score_x=int(cell_size* cell_number_line-68)
        score_y=int(cell_size*cell_number_column-63)
        score_rect=score_surface.get_rect(center=(score_x,score_y))
        apple_rect=apple.get_rect(midright=(score_rect.left,score_rect.centery))
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)


pygame.init()

SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

cell_size=45
cell_number_column=20
cell_number_line=25
screen=pygame.display.set_mode((cell_size*cell_number_line,cell_size*cell_number_column))
clock = pygame.time.Clock()
apple=pygame.image.load('fruit.png').convert_alpha()
texture1=pygame.image.load('textura1.png').convert_alpha()
texture2=pygame.image.load('textura2.png').convert_alpha()
game_font=pygame.font.Font(None,80)

main_game=MAIN()

while True:
    for event in pygame.event.get(): #loop pentru eventuri
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # se inchide orice executie
        if event.type==SCREEN_UPDATE:
            main_game.update()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and not main_game.snake.direction.y==1:
                main_game.snake.direction=Vector2(0,-1)
            if event.key==pygame.K_DOWN and not main_game.snake.direction.y==-1:
                main_game.snake.direction=Vector2(0,1)
            if event.key==pygame.K_RIGHT and not main_game.snake.direction.x==-1:
                main_game.snake.direction= Vector2(1,0)
            if event.key==pygame.K_LEFT and not main_game.snake.direction.x==1:
                main_game.snake.direction= Vector2(-1,0)
    pygame.display.update()
    #screen.fill((63, 123, 17))
    main_game.draw_elements()
    clock.tick(120) #sa mearga in 120 fps-uri