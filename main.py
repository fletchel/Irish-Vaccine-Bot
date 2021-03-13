from get_data import check_new
from bot import update_bot

with open("bot_data.txt") as f:

    prev_v, prev_date, prev_v2 = f.read().split(",")
    prev_v = int(prev_v)
    prev_v2 = int(prev_v2)


cur_v, cur_date, cur_v2 = check_new(prev_v, prev_v2)

if cur_v != 0 and cur_date != 0 and cur_v2 != 0:

    update_bot(cur_v, cur_date, cur_v2, prev_v, prev_date, prev_v2)

    with open("bot_data.txt", 'r+') as f:

        new_data = str(cur_v) + "," + cur_date + "," + str(cur_v2)
        f.truncate(0)
        f.write(new_data)


