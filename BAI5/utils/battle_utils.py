import random

from utils.player_utils import find_player


def fight_monster(records):
    if not records:
        print('Hệ thống chưa có dữ liệu người chơi.')
        return

    monsters = [
        {
            'name': 'Bug Python',
            'damage': 20,
            'reward_gold': 100
        },
        {
            'name': 'Import Error',
            'damage': 35,
            'reward_gold': 150
        },
        {
            'name': 'Module Not Found',
            'damage': 50,
            'reward_gold': 250
        }
    ]

    player_id = input('Nhập mã người chơi chiến đấu: ')

    index = find_player(records, player_id)

    if index == -1:
        print('Không tìm thấy người chơi!')
        return

    player = records[index]

    if player['hp'] <= 0:
        print('Người chơi đã gục ngã, không thể tiếp tục chiến đấu!')
        return

    monster = random.choice(monsters)

    print(f'>> Quái vật xuất hiện: {monster["name"]}')

    player['hp'] -= monster['damage']

    print(
        f'>> {player["name"]} bị mất {monster["damage"]} HP.'
    )

    if player['hp'] > 0:
        player['gold'] += monster['reward_gold']

        print(
            f'>> Chiến thắng! Bạn nhận được {monster["reward_gold"]} vàng.'
        )

        print(f'>> HP còn lại: {player["hp"]}')

    else:
        player['hp'] = 0
        print('>> Bạn đã thất bại và không nhận được vàng.')