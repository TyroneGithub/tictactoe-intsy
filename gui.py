import pygame

pygame.init()

class GUI: 
    @staticmethod
    def text_list_setup(texts, font, colors, x, y):
        text_list = []
        text_rect_list = []
        # x = 90
        for i in range(len(texts)):
            text_obj = font.render(texts[i], False, colors[i])
            text_rect = text_obj.get_rect()
            text_rect.center = (x, y)
            y += 175
            text_list.append(text_obj)
            text_rect_list.append(text_rect)
        
        return text_list, text_rect_list 

    @staticmethod
    def render_text(texts, text_rects, win):

        for i in range(len(texts)):
            win.blit(texts[i], text_rects[i])

    @staticmethod
    def text_setup(word, font, x, y, color):
        text = font.render(word, False, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        # text_rect.width = 500
        
        return text, text_rect