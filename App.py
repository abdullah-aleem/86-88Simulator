import pygame



def run(x):
    	
   
# write(screen, x - 20, y, "ALU", width, i)
    color = (250, 250, 255)
    colorReg = (250, 250, 250)
    colorM = (250, 250, 250)
    colorBus = (250, 250, 250)
    alucolor = (250, 250, 250)
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
        line1 = pygame.draw.line(screen, color, (1400, 215), (1400, 60), 2)
        line2 = pygame.draw.line(screen, color, (300, 370), (400, 370), 2)
        line3 = pygame.draw.line(screen, color, (400, 370), (400, 480), 2)
        line4 = pygame.draw.line(screen, color, (500, 490), (500, 930), 2)
        line5 = pygame.draw.line(screen, color, (455, 930), (750, 930), 2)
        line6 = pygame.draw.line(screen, color, (750, 930), (750, 850), 2)
        line7 = pygame.draw.line(screen, color, (500, 720), (455, 720), 2)
        line8 = pygame.draw.line(screen, color, (500, 570), (430, 570), 2)
        line8 = pygame.draw.line(screen, color, (500, 570), (430, 570), 2)
        line9 = pygame.draw.line(screen, color, (1530, 80), (1630, 80), 2)
        line9 = pygame.draw.line(screen, color, (1630, 80), (1630, 700), 2)
        line9 = pygame.draw.line(screen, color, (1630, 700), (1400, 700), 2)
        line9 = pygame.draw.line(screen, color, (1300, 710), (1225, 710), 2)
        line10 = pygame.draw.line(screen, color, (950, 740), (820, 740), 2)
        line11 = pygame.draw.line(screen, color, (650, 170), (650, 480), 2)
        one = pygame.draw.rect(screen, colorReg, (50, 50, 130, 40))
        two = pygame.draw.rect(screen, colorReg, (190, 50, 130, 40))
        three = pygame.draw.rect(screen, colorReg, (50, 100, 130, 40))
        four = pygame.draw.rect(screen, colorReg, (190, 100, 130, 40))
        five = pygame.draw.rect(screen, colorReg, (50, 150, 130, 40))
        six = pygame.draw.rect(screen, colorReg, (190, 150,130, 40))
        seven = pygame.draw.rect(screen, colorReg, (50, 200, 130, 40))
        eight = pygame.draw.rect(screen, colorReg, (190, 200,130, 40))
        # control_unit = pygame.draw.rect(screen, color, (240, 50, 40, 40))
        increment=122
        # alu=pygame.draw.polygon(screen, color,
        #                     [(1300, 130+increment*18 ),
        #                      (1300 + 40, 130 + increment * 23),
        #                      (1300 + 200, 130 + increment * 23),
        #                      (1300 + 240, 130 + increment * 18),
        #                      (1300 + 180, 130 + increment * 18),
        #                      (1300 + 160, 130 + increment * 21),
        #                      (1300 + 80, 130 + increment * 21),
        #                      (1300+ 60, 130 + increment * 18)
        #                     ])
        # operands = pygame.draw.rect(screen, color, (280, 50, 40, 40))
        flags = pygame.draw.rect(screen, color, (255, 900, 200, 40))
        temp = pygame.draw.rect(screen, color, (270, 550, 170, 40))
        # # memory_interface=ellipse()
        # # summation=summation()
        busControlLogic = pygame.draw.rect(screen, color, (1300, 650, 100, 100))
        insQ=pygame.draw.rect(screen, color, (950, 700, 275, 60))
        eusc=pygame.draw.rect(screen, color, (700, 730, 120, 120))
        es = pygame.draw.rect(screen, color, (1300, 215, 260, 40))
        cs = pygame.draw.rect(screen, color, (1300, 260, 260, 40))
        ss = pygame.draw.rect(screen, color, (1300, 305, 260, 40))
        ds = pygame.draw.rect(screen, color, (1300, 350, 260, 40))
        ip = pygame.draw.rect(screen, color, (1300, 395,260, 40))
        adder = pygame.draw.rect(screen, color, (1330, 60, 200, 40))
        alu = pygame.draw.rect(screen, alucolor, (255, 700, 200, 40))
        internal=pygame.draw.rect(screen, color, (1300, 440,260, 120))
        memory=pygame.draw.rect(screen, colorM, (600, 50,260, 120))
        dataBusALU = pygame.draw.rect(screen, colorBus, (50, 480,1250, 20))
        sp = pygame.draw.rect(screen, colorReg, (50, 250,270, 40))
        bp = pygame.draw.rect(screen, colorReg, (50, 300,270, 40))
        si = pygame.draw.rect(screen, colorReg, (50, 350, 270, 40))
        di = pygame.draw.rect(screen, colorReg, (50, 400,270, 40))
        
        text_alu = my_font.render('ALU', False, (0, 0, 0))
        screen.blit(text_alu, (255,700))
        text_memory = my_font.render('MEMORY', False, (0, 0, 0))
        screen.blit(text_memory, (600,50))
        text_al = my_font.render('AL', False, (0, 0, 0))
        screen.blit(text_al, (50,50))
        text_bl = my_font.render('BL', False, (0, 0, 0))
        screen.blit(text_bl, (50,100))
        text_cl = my_font.render('CL', False, (0, 0, 0))
        screen.blit(text_cl, (50,150))
        text_dl = my_font.render('DL', False, (0, 0, 0))
        screen.blit(text_dl, (50, 200))
        text_ah = my_font.render('AH', False, (0, 0, 0))
        screen.blit(text_ah, (190, 50))
        text_bh = my_font.render('BH', False, (0, 0, 0))
        screen.blit(text_bh, (190, 100))
        text_ch = my_font.render('CH', False, (0, 0, 0))
        screen.blit(text_ch, (190, 150))
        text_dh = my_font.render('DH', False, (0, 0, 0))
        screen.blit(text_dh, (190, 200))
        text_sp = my_font.render('SP', False, (0, 0, 0))
        screen.blit(text_sp, (50, 250))
        text_bp = my_font.render('DP', False, (0, 0, 0))
        screen.blit(text_bp, (50, 300))
        text_si = my_font.render('SI', False, (0, 0, 0))
        screen.blit(text_si, (50, 350))
        text_di = my_font.render('DI', False, (0, 0, 0))
        screen.blit(text_di, (50, 400))
        text_flags = my_font.render('FLAGS', False, (0, 0, 0))
        screen.blit(text_flags, (255, 900))
        text_tReg = my_font.render('Temporary', False, (0, 0, 0))
        screen.blit(text_tReg, (270, 550))
        text_es = my_font.render('SP', False, (0, 0, 0))
        screen.blit(text_es, (1300, 215))
        text_cs = my_font.render('BP', False, (0, 0, 0))
        screen.blit(text_cs, (1300, 260))
        text_ss = my_font.render('SI', False, (0, 0, 0))
        screen.blit(text_ss, (1300, 305))
        text_ds = my_font.render('DS', False, (0, 0, 0))
        screen.blit(text_ds, (1300, 350))
        text_ip = my_font.render('IP', False, (0, 0, 0))
        screen.blit(text_ip, (1300, 395))
        text_adder = my_font.render('ADDER', False, (0, 0, 0))
        screen.blit(text_adder, (1330, 60))
        text_ensu = my_font.render('EUSC', False, (0, 0, 0))
        screen.blit(text_ensu, (700, 730))
        text_insq = my_font.render('INSQ', False, (0, 0, 0))
        screen.blit(text_insq, (950, 700))
        text_busControlLogic = my_font.render('BCL', False, (0, 0, 0))
        screen.blit(text_busControlLogic, (1300, 650))
        text_internal = my_font.render('internal', False, (0, 0, 0))
        screen.blit(text_internal, (1300, 440))
        
        
        
        # ah = pygame.draw.rect(screen, color, (560, 50, 40, 40))
        # bh = pygame.draw.rect(screen, color, (600, 50, 40, 40))
        # ch = pygame.draw.rect(screen, color, (640, 50, 40, 40))
        # dh = pygame.draw.rect(screen, color, (680, 50, 40, 40))
        # al = pygame.draw.rect(screen, color, (720, 50, 40, 40))
        # bl = pygame.draw.rect(screen, color, (760, 50, 40, 40))
        # cl = pygame.draw.rect(screen, color, (800, 50, 40, 40))
        # dl = pygame.draw.rect(screen, color, (840, 50, 40, 40))
       
        
        #labels
        
        # pygame.draw.polygon(self.screen, self.color,
                            # [(self.end_x, self.end_y), (self.end_x - 10, self.end_y - 5),
                            #  (self.end_x - 10, self.end_y + 5)])
    while True:
        pygame.init()
        pygame.font.init()  # you have to call this at the start,

        # if you want to use this module.
        my_font = pygame.font.SysFont('Comic Sans MS', 30) 
        if x==1:
            colorReg=(255,0,0)
            colorBus=(255,0,0)
            alucolor = (255, 0, 0)
        if x==2:
            colorReg=(0,255,0)
            colorM=(0,255,0)
            colorBus=(0,255,0)
            alucolor=(0,255,0)
        if x==3:
            
            colorM=(0,255,0)
            colorBus=(0,255,0)
            alucolor=(0,255,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                  color = (5, 25, 55)
            else:
                color = (250, 250, 250)
        collective_function_drawing()
        pygame.display.update()
