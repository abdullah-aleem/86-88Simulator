import pygame



def run():

   
# write(screen, x - 20, y, "ALU", width, i)
    color = (220, 208, 255)
    twoColor = (250, 250, 250)
    threeColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fiveColor = (250, 250, 250)
    sixColor = (250, 250, 250)
    controlunitColor = (250, 250, 250)
    aluColor = (250, 250, 250)
    operandsColor = (250, 250, 250)
    flagsColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)
    fourColor = (250, 250, 250)

    print("started")

    screen = pygame.display.set_mode((1900, 980))

    def collective_function_drawing():
        one = pygame.draw.rect(screen, color, (50, 50, 130, 40))
        two = pygame.draw.rect(screen, color, (190, 50, 130, 40))
        three = pygame.draw.rect(screen, color, (50, 100, 130, 40))
        four = pygame.draw.rect(screen, color, (190, 100, 130, 40))
        five = pygame.draw.rect(screen, color, (50, 150, 130, 40))
        six = pygame.draw.rect(screen, color, (190, 150,130, 40))
        seven = pygame.draw.rect(screen, color, (50, 200, 130, 40))
        eight = pygame.draw.rect(screen, color, (190, 200,130, 40))
        # control_unit = pygame.draw.rect(screen, color, (240, 50, 40, 40))
        increment=122
        alu=pygame.draw.polygon(screen, color,
                            [(1300, 130+increment*18 ),
                             (1300 + 40, 130 + increment * 23),
                             (1300 + 200, 130 + increment * 23),
                             (1300 + 240, 130 + increment * 18),
                             (1300 + 180, 130 + increment * 18),
                             (1300 + 160, 130 + increment * 21),
                             (1300 + 80, 130 + increment * 21),
                             (1300+ 60, 130 + increment * 18)
                            ])
        # operands = pygame.draw.rect(screen, color, (280, 50, 40, 40))
        flags = pygame.draw.rect(screen, color, (255, 900, 200, 40))
        temp = pygame.draw.rect(screen, color, (270, 550, 170, 40))
        # # memory_interface=ellipse()
        # # summation=summation()
        busControlLogic = pygame.draw.rect(screen, color, (1300, 650, 100, 100))
        insQ=pygame.draw.rect(screen, color, (950, 750, 275, 60))
        eusc=pygame.draw.rect(screen, color, (700, 730, 120, 120))
        es = pygame.draw.rect(screen, color, (1300, 215, 260, 40))
        cs = pygame.draw.rect(screen, color, (1300, 260, 260, 40))
        ss = pygame.draw.rect(screen, color, (1300, 305, 260, 40))
        ds = pygame.draw.rect(screen, color, (1300, 350, 260, 40))
        ip = pygame.draw.rect(screen, color, (1300, 395,260, 40))
        # ah = pygame.draw.rect(screen, color, (560, 50, 40, 40))
        # bh = pygame.draw.rect(screen, color, (600, 50, 40, 40))
        # ch = pygame.draw.rect(screen, color, (640, 50, 40, 40))
        # dh = pygame.draw.rect(screen, color, (680, 50, 40, 40))
        # al = pygame.draw.rect(screen, color, (720, 50, 40, 40))
        # bl = pygame.draw.rect(screen, color, (760, 50, 40, 40))
        # cl = pygame.draw.rect(screen, color, (800, 50, 40, 40))
        # dl = pygame.draw.rect(screen, color, (840, 50, 40, 40))
        internal=pygame.draw.rect(screen, color, (1300, 440,260, 120))
        dataBusALU = pygame.draw.rect(screen, color, (50, 480,1250, 20))
        sp = pygame.draw.rect(screen, color, (50, 250,270, 40))
        bp = pygame.draw.rect(screen, color, (50, 300,270, 40))
        si = pygame.draw.rect(screen, color, (50, 350, 270, 40))
        di = pygame.draw.rect(screen, color, (50, 400,270, 40))

    while True:
        pygame.init()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                  color = (5, 25, 55)
            else:
                color = (250, 250, 250)
        collective_function_drawing()
        pygame.display.update()