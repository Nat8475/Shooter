from Enemy import Enemy
from Entity import Entity


class EntityMediator():

    #o VERIFY COLLISION WINDOW (PRIVATE METHOD)

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    #o VERIFY ENTITY HEALTH 

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)


    #o VERIFY COLLISION

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_test = entity_list[i]

            EntityMediator.__verify_collision_window(entity_test)
    