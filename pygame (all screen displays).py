import pygame

# From Lukas Peraza's blog post!


class CozmoMaze(object):

    def isKeyPressed(self, key):
        return self._keys.get(key, False)

    def mousePressed(event):
        print(event.pos)

    def mouseReleased(event):
        print(event.pos)

    def keyPressed(event, key, mod):
        pass

    def __init__(self, width=600, height=400, fps=50, title="Cozmo Maze"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.gameDisplay = pygame.display.set_mode((self.width, self.height))
        self.menu = True
        self.game = False
        self.gameOver = False
        pygame.init()

    def redrawAll(self):
        if self.menu:
            self.gameDisplay.fill((100, 100, 100))
            messageDisplay("Welcome to Cozmo Race!", (255, 0, 0))

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        # self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            # self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                # elif (event.type == pygame.MOUSEMOTION and
                #       event.buttons == (0, 0, 0)):
                #     self.mouseMotion(*(event.pos))
                # elif (event.type == pygame.MOUSEMOTION and
                #       event.buttons[0] == 1):
                #     self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
                    pygame.quit()
                    quit()
            screen.fill((255, 255, 255))
            self.redrawAll()
            pygame.display.flip()


def messageDisplay(s, color):
    message = pygame.font.Font("freesansbold.ttf", 50)
    textSurface, textRectangle = textObjects(s, message, color)
    textRectangle.center = (Game.width / 2, (1 / 5) * Game.height)
    Game.gameDisplay.blit(textSurface, textRectangle)


def textObjects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


Game = CozmoMaze()

Game.run()

pygame.quit()
quit()

# pygame.init()

displayWidth = 800
displayHeight = 600
# gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
# clock = pygame.time.Clock()


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# drPhil = pygame.image.load('pygametestpic.jpg')

# # menu = True
# # game = False
# # gameOver = False


# def pic(x, y):
#     gameDisplay.blit(drPhil, (x, y))


# # def messageDisplay(s):
# #     message = pygame.font.Font("freesansbold.ttf", 50)
# #     textSurface, textRectangle = textObjects(s, message)
# #     textRectangle.center = (displayWidth / 2, (1 / 5) * displayHeight)
# #     gameDisplay.blit(textSurface, textRectangle)


# # def textObjects(text, font):
# #     textSurface = font.render(text, True, black)
# #     return textSurface, textSurface.get_rect()


# # running = True

# # while running:
# #     clock.tick(60)
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
# #         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
# #             running = False

# #         # print(event)
# #     if menu == True:
# #         gameDisplay.fill(white)
# #         messageDisplay("Welcome to Cozmo Race!")

# #     pygame.display.update()


# # pygame.quit()
# # quit()
