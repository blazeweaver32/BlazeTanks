from data.constants import objects, result_false


class UI:
    def __init__(self):
        pass


    def update(self):
        pass

    def draw(self):
        from run import window, fontUI
        title_game = fontUI.render("BLAZE TANKS", 1, "white")
        rect_2 = title_game.get_rect(center=(400, 5 + 11))
        window.blit(title_game, rect_2)
        i = 0

        #Отображение победителя игры
        if len(result_false) != 0:
            for char in result_false:
                text = fontUI.render(f"{char.nickname} проиграл", 1, char.color)
                rect = text.get_rect(center = (400,280))
                window.blit(text, rect)

            for obj in objects:
                if obj.type == 'tank':
                    text = fontUI.render(f"{obj.nickname} выиграл", 1, obj.color)
                    rect = text.get_rect(center=(400, 300))
                    window.blit(text, rect)
        else:
            for obj in objects:
                if obj.type == 'tank':
                    if i == 0:
                        text_player = f"{obj.nickname} {str(obj.hp)}"
                    else:
                        text_player = f"{str(obj.hp)} {obj.nickname}"
                    text = fontUI.render(text_player, 1, obj.color)
                    rect = text.get_rect(center = (70 + i * 650, 5 + 11))
                    window.blit(text, rect)
                    i += 1
