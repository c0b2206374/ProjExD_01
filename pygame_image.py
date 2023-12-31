import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20231121/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01-20231121/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_list = [kk_img,pg.transform.rotozoom(kk_img, 10, 1.0)]
    bg_flip = pg.transform.flip(bg_img,True,False)
    

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        
        x = tmr%3200

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_flip, [1600-x, 0])
        
        tme = (tmr // 10) % 10

        if tme % 2:
            screen.blit(kk_list[0],[300,200])
        else:
            screen.blit(kk_list[1],[300,200])
            
        
        pg.display.update()
        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()