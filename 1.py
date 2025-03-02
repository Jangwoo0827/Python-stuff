
import random
import os
import time

# 속성 정의
TYPES = ["노말", "불", "물", "풀", "전기", "얼음", "격투", "독", "땅", "비행", "에스퍼", "벌레", "바위", "고스트", "드래곤", "강철", "페어리"]

# 상성 관계 정의 (공격 타입, 방어 타입, 효과)
TYPE_CHART = {
    ("물", "불"): 2.0, ("불", "풀"): 2.0, ("풀", "물"): 2.0, ("전기", "물"): 2.0,
    ("땅", "전기"): 2.0, ("얼음", "드래곤"): 2.0, ("격투", "노말"): 2.0, ("독", "풀"): 2.0,
    ("에스퍼", "격투"): 2.0, ("벌레", "풀"): 2.0, ("바위", "비행"): 2.0, ("고스트", "에스퍼"): 2.0,
    ("드래곤", "드래곤"): 2.0, ("강철", "얼음"): 2.0, ("페어리", "드래곤"): 2.0,
    ("불", "물"): 0.5, ("풀", "불"): 0.5, ("물", "풀"): 0.5, ("전기", "풀"): 0.5,
    ("노말", "바위"): 0.5, ("비행", "전기"): 0.5, ("에스퍼", "에스퍼"): 0.5, ("강철", "불"): 0.5,
    ("고스트", "노말"): 0, ("전기", "땅"): 0, ("드래곤", "페어리"): 0
}

SKILLS = [
    ("기본 공격", 1.0, 100, "기본적인 물리 공격", "노말", "👊"),
    ("파워 어택", 1.5, 150, "강력한 물리 공격", "노말", "💥"),
    ("불꽃 펀치", 1.6, 160, "불속성 근접 공격", "불", "🔥"),
    ("물대포", 1.7, 170, "강력한 물속성 원거리 공격", "물", "💧"),
    ("잎날가르기", 1.6, 160, "날카로운 잎으로 공격", "풀", "🍃"),
    ("전기 충격", 1.7, 170, "전기 속성 공격, 마비 확률", "전기", "⚡"),
    ("얼음 빔", 1.6, 160, "얼음 속성 공격, 빙결 확률", "얼음", "❄️"),
    ("용의 분노", 1.9, 190, "드래곤 속성의 강력한 공격", "드래곤", "🐉"),
    ("대지진", 2.0, 200, "넓은 범위 지면 공격", "땅", "🌋"),
    ("폭풍", 1.8, 180, "강력한 바람 공격", "비행", "🌪️"),
    ("섀도 볼", 1.7, 170, "유령 속성 원거리 공격", "고스트", "👻"),
    ("강철 날개", 1.6, 160, "강철 속성의 날개 공격", "강철", "🔩"),
    ("독 찌르기", 1.5, 150, "독 속성 공격, 중독 확률", "독", "☠️"),
    ("사이코 키네시스", 1.8, 180, "강력한 정신 공격", "에스퍼", "🔮"),
    ("메가톤 펀치", 1.9, 190, "매우 강력한 펀치 공격", "격투", "🥊"),
    ("하이퍼 빔", 2.2, 220, "강력한 에너지 빔", "노말", "🌟"),
    ("솔라 빔", 2.1, 210, "태양 에너지를 모아 공격", "풀", "☀️"),
    ("화염방사", 1.9, 190, "강력한 화염 공격", "불", "🔥"),
    ("하이드로 펌프", 2.0, 200, "강력한 물 공격", "물", "🌊"),
    ("번개", 2.1, 210, "강력한 전기 속성 공격", "전기", "⚡"),
    ("냉동빔", 1.8, 180, "강력한 얼음 속성 빔", "얼음", "❄️"),
    ("지진", 2.0, 200, "강력한 지진 공격", "땅", "🌍"),
    ("사이코 쇼크", 1.9, 190, "상대방의 정신을 공격", "에스퍼", "💫"),
    ("벌레의 야단법석", 1.7, 170, "벌레들의 집단 공격", "벌레", "🐛"),
    ("스톤 엣지", 1.8, 180, "날카로운 돌로 공격", "바위", "🗿"),
    ("유령 찍기", 1.7, 170, "유령의 기운으로 공격", "고스트", "👻"),
    ("용의 숨결", 1.8, 180, "드래곤의 강력한 숨결", "드래곤", "🐲"),
    ("철제 주먹", 1.7, 170, "강철의 주먹으로 공격", "강철", "🦾"),
    ("요정의 바람", 1.8, 180, "요정의 힘을 담은 바람", "페어리", "🧚"),
    ("메테오 메시", 2.4, 240, "우주의 힘을 빌린 필살기", "드래곤", "☄️"),
    ("초신성 폭발", 3.0, 300, "우주의 힘으로 폭발을 일으킴", "노말", "💥"),
    ("시공간 왜곡", 3.2, 320, "시공간을 뒤틀어 공격", "에스퍼", "🌀"),
    ("천지창조", 3.5, 350, "새로운 세계를 창조하여 적을 없앰", "페어리", "🌈"),
    ("멸망의 카운트다운", 4.0, 400, "3턴 후 엄청난 위력으로 공격", "드래곤", "⏰"),
    ("차원 절단", 3.8, 380, "차원을 가르는 공격", "고스트", "✂️"),
    ("유서우펀치", 99.9, 4000, "걍 개 셈", "드래곤", "👊💯")
]

MONSTERS = [
    ("불꽃거북", 100, 15, "불"),
    ("물거북", 110, 14, "물"),
    ("풀거북", 105, 13, "풀"),
    ("전기쥐", 90, 18, "전기"),
    ("불꽃여우", 95, 17, "불"),
    ("물오리", 100, 15, "물"),
    ("돌뱀", 120, 12, "바위"),
    ("독나방", 85, 20, "독"),
    ("용", 130, 16, "드래곤"),
    ("요정", 80, 22, "페어리"),
    ("격투닭", 95, 18, "격투"),
    ("얼음여우", 100, 16, "얼음"),
    ("에스퍼고양이", 95, 19, "에스퍼"),
    ("강철새", 115, 15, "강철"),
    ("땅두더지", 110, 15, "땅"),
    ("비행도마뱀", 100, 17, "비행"),
    ("벌레전사", 90, 19, "벌레"),
    ("유령인형", 95, 18, "고스트"),
    ("노말토끼", 100, 16, "노말"),
    ("페어리나비", 85, 21, "페어리")
]

def clear_screen():
    # Windows의 경우
    if os.name == 'nt':
        _ = os.system('cls')
    # Mac 및 Linux의 경우
    else:
        _ = os.system('clear')

class Character:
    def __init__(self, name, hp, attack, type):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.type = type
        self.skills = []
        self.special_skill_uses = 3  # 특수 스킬 사용 횟수

    def use_skill(self, skill, target):
        if skill[1] >= 3.0:  # 종결급 스킬 판단
            if self.special_skill_uses > 0:
                self.special_skill_uses -= 1
                print(f"특수 스킬 사용! 남은 사용 횟수: {self.special_skill_uses}")
            else:
                print("특수 스킬의 사용 횟수가 모두 소진되었습니다.")
                return

        base_damage = skill[2]
        type_multiplier = TYPE_CHART.get((skill[4], target.type), 1.0)
        actual_damage = int(self.attack * skill[1] * type_multiplier)
        target.hp -= actual_damage
        
        print(f"{self.name}의 {skill[0]} {skill[5]}! (기본 데미지: {base_damage}, 실제 데미지: {actual_damage})")
        if type_multiplier > 1:
            print(f"{skill[5]} 효과가 굉장했다! {skill[4]} 속성의 강점!")
        elif type_multiplier < 1:
            print(f"{skill[5]} 효과가 별로인 듯하다... {skill[4]} 속성의 약점...")
        elif type_multiplier == 0:
            print(f"{skill[5]} 효과가 없는 듯하다... {skill[4]} 속성의 무효...")
        
        print(f"{target.name}에게 {actual_damage}의 데미지를 입혔습니다.")
        if target.hp < 0:
            target.hp = 0

class Player(Character):
    def __init__(self, name, hp, attack, type):
        super().__init__(name, hp, attack, type)

    def level_up(self):
        self.max_hp += 10
        self.hp = self.max_hp
        self.attack += 2
        print(f"{self.name}의 레벨이 올랐습니다! 최대 체력: {self.max_hp}, 공격력: {self.attack}")

    def learn_ultimate_skill(self):
        ultimate_skills = [s for s in SKILLS if s[1] >= 3.0 and s not in self.skills]
        if ultimate_skills:
            new_skill = random.choice(ultimate_skills)
            self.skills.append(new_skill)
            print(f"{self.name}이(가) 종결급 스킬 {new_skill[0]}을(를) 습득했습니다!")

    def learn_new_skill(self):
        if len(self.skills) < len(SKILLS):
            new_skill = random.choice([s for s in SKILLS if s not in self.skills and s[1] < 3.0])
            self.skills.append(new_skill)
            print(f"{self.name}이(가) 새로운 스킬 {new_skill[0]}을(를) 배웠습니다!")

class Monster(Character):
    pass

class FinalBoss(Monster):
    def __init__(self, name, hp, attack, type):
        super().__init__(name, hp, attack, type)
        self.phase = 1
        self.max_phase = 3

    def use_skill(self, skill, target):
        if skill[0] == "궁극의 힘":
            damage = int(self.attack * skill[1] * self.phase)
            target.hp -= damage
            print(f"{self.name}의 {skill[0]}! {target.name}에게 엄청난 {damage}의 데미지를 입혔습니다!")
        else:
            super().use_skill(skill, target)

    def phase_change(self):
        if self.hp < self.max_hp * (1 - self.phase / self.max_phase) and self.phase < self.max_phase:
            self.phase += 1
            self.attack += 10
            print(f"\n{self.name}이(가) {self.phase}단계로 변신했습니다! 공격력이 증가합니다.")

def battle(player, monster):
    while player.hp > 0 and monster.hp > 0:
        clear_screen()
        print(f"\n{player.name} ({player.type}) VS {monster.name} ({monster.type})")
        print(f"\n{player.name} HP: {player.hp}/{player.max_hp}")
        print(f"{monster.name} HP: {monster.hp}/{monster.max_hp}")

        # 플레이어 턴
        print(f"\n{player.name}의 턴")
        for i, skill in enumerate(player.skills):
            print(f"{i+1}. {skill[0]} {skill[5]}-{skill[2]} ({skill[4]})")
        
        while True:
            try:
                choice = int(input("사용할 스킬을 선택하세요: ")) - 1
                if 0 <= choice < len(player.skills):
                    break
                else:
                    print("올바른 번호를 입력하세요.")
            except ValueError:
                print("숫자를 입력하세요.")
        
        player.use_skill(player.skills[choice], monster)

        if monster.hp <= 0:
            print(f"{monster.name}을(를) 물리쳤습니다!")
            time.sleep(2)  # 2초 대기
            return True

        # 몬스터 턴
        print(f"\n{monster.name}의 턴")
        monster_skill = random.choice(monster.skills)
        monster.use_skill(monster_skill, player)

        if isinstance(monster, FinalBoss):
            monster.phase_change()

        if player.hp <= 0:
            print(f"{player.name}이(가) 쓰러졌습니다...")
            time.sleep(2)  # 2초 대기
            return False

        time.sleep(2)  # 2초 대기

def main_game():
    player = Player("주인공", 100, 20, random.choice(TYPES))
    player.skills = random.sample([s for s in SKILLS if s[1] < 3.0], 3)  # 3개의 랜덤 일반 스킬로 시작
    current_stage = 1
    final_stage = 5

    print("포켓몬스터 스타일 RPG 게임을 시작합니다!")
    print(f"{player.name}은(는) 최종 보스를 물리치기 위해 여행을 떠납니다.")
    time.sleep(2)

    while current_stage <= final_stage:
        clear_screen()
        print(f"\n=== 스테이지 {current_stage} ===")
        if current_stage == final_stage:
            boss = FinalBoss("궁극의 보스", 1500, 40, random.choice(TYPES))
            boss.skills = random.sample(SKILLS, 5) + [("궁극의 힘", 5.0, 100, "보스의 필살기", boss.type, "🔱")]
            victory = battle(player, boss)
        else:
            monster_type = random.choice(MONSTERS)
            monster = Monster(monster_type[0], monster_type[1] + 5 * current_stage, monster_type[2] + current_stage, monster_type[3])
            monster.skills = random.sample([s for s in SKILLS if s[1] < 3.0], 3)  # 일반 몬스터는 3개의 랜덤 일반 스킬
            victory = battle(player, monster)
        
        if not victory:
            print("게임 오버!")
            return False
        
        player.level_up()
        if random.random() < 0.05:  # 5% 확률로 종결급 스킬 습득
            player.learn_ultimate_skill()
        elif random.random() < 0.40:  # 40% 확률로 일반 스킬 습득
            player.learn_new_skill()
        
        current_stage += 1
        time.sleep(2)

    if current_stage > final_stage:
        print("축하합니다! 모든 스테이지를 클리어하고 최종 보스를 물리쳤습니다!")
    return True

def game_loop():
    while True:
        game_result = main_game()
        if game_result:
            print("게임을 완료했습니다!")
        
        play_again = input("다시 시작하시겠습니까? (y/n): ").lower()
        if play_again != 'y':
            print("게임을 종료합니다. 감사합니다!")
            break
        else:
            print("게임을 다시 시작합니다...")
            time.sleep(2)

if __name__ == "__main__":
    game_loop()
