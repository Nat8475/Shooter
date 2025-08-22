from Background import Background
from Const import WIN_WIDTH


class entityFactory():

    @staticmethod
    def get_entity(entity_name: str, position= (0,0)):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                for i in range(5):
                        list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                        list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg