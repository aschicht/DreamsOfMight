
class Combatable:

    def get_hit_dice(self):
        pass

    def get_hit_modifier(self):
        pass

    def get_damage_dice(self):
        pass

    def get_damage_modifier(self):
        pass

    def get_defense(self):
        pass

    def get_protection(self):
        pass


class CombatManager:

    @staticmethod
    def fight(attacker, defender):
        hit = attacker.get_hit_dice().roll(attacker.get_hit_modifier())
        print('hit %d' % hit)
        if hit > defender.get_defense():
            print('hit')
            damage = attacker.get_damage_dice().roll(attacker.get_damage_modifier())
            damage = damage - defender.get_protection()
            print('damage %d' % damage)
            return damage if damage >= 0 else 0
        else:
            print('missed')
            return 0


