from data.player_list import player_records

from utils.item_utils import open_treasure_chest
from utils.item_utils import buy_item

from utils.battle_utils import fight_monster

from report.report import (
    display_players,
    show_leaderboard as leaderboard
)


def main():
    while True:

        choice = input('''
===== RIKKEI DUNGEON - PYTHON MODULE ADVENTURE =====
1. Hiển thị danh sách người chơi
2. Mở rương báu ngẫu nhiên
3. Mua vật phẩm trong cửa hàng
4. Chiến đấu với quái vật
5. Xem bảng xếp hạng người chơi
6. Thoát chương trình
====================================================
Chọn chức năng (1-6): ''')

        match choice:

            case '1':
                display_players(player_records)

            case '2':
                open_treasure_chest(player_records)

            case '3':
                buy_item(player_records)

            case '4':
                fight_monster(player_records)

            case '5':
                leaderboard(player_records)

            case '6':
                print(
                    'Cảm ơn bạn đã tham gia Rikkei Dungeon!'
                )
                break

            case _:
                print('Lựa chọn không hợp lệ!')


if __name__ == '__main__':
    main()