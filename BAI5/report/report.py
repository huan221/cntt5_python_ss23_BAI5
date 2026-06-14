from operator import itemgetter

from tabulate import tabulate


def display_players(records):
    if not records:
        print('Hệ thống chưa có dữ liệu người chơi.')
        return

    table = []

    for player in records:

        hp = player['hp']

        if hp <= 0:
            status = 'Đã gục ngã'
        elif hp < 50:
            status = 'Nguy hiểm'
        elif hp < 100:
            status = 'Ổn định'
        else:
            status = 'Sung sức'

        table.append([
            player['player_id'],
            player['name'],
            player['hp'],
            player['mana'],
            player['gold'],
            player['level'],
            status
        ])

    print('\n--- DANH SÁCH NGƯỜI CHƠI ---')

    print(
        tabulate(
            table,
            headers=[
                'ID',
                'Tên',
                'HP',
                'Mana',
                'Gold',
                'Level',
                'Trạng thái'
            ],
            tablefmt='grid'
        )
    )


def show_leaderboard(records):
    if not records:
        print('Hệ thống chưa có dữ liệu người chơi.')
        return

    ranking = sorted(
        records,
        key=lambda player: (
            player['level'],
            player['gold'],
            player['hp']
        ),
        reverse=True
    )

    print('\n--- BẢNG XẾP HẠNG NGƯỜI CHƠI ---')

    for index, player in enumerate(ranking, start=1):
        print(
            f'{index}. '
            f'{player["name"]} | '
            f'Level: {player["level"]} | '
            f'Gold: {player["gold"]} | '
            f'HP: {player["hp"]}'
        )

    print('--------------------------------')