def main(table):
    table = list(filter(len, map(lambda row: list(filter(bool, row)), table)))
    table = map(list, zip(*table))
    table2 = []
    for i in table:
        if i not in table2:
            table2.append(i)
    table2 = map(list, zip(*table2))
    table = [
        [phone1.replace(' ', '').replace('-', ''),
         state.
         replace("Выполнено", "Да")
         if state == "Выполнено" else
         state.replace("Не выполнено",
                       "Нет"),
         "{:.2f}".format(float(val))] for phone1, state, val in table2]
    table = sorted(table, key=lambda x: x[0])
    table = list(map(list, zip(*table)))
    return list(table)


tabl = [[None, None, None, None],
        ["+7 191 982 - 11 - 60", "+7 191 982 - 11 - 60", "Выполнено", "0.6"],
        ["+7 609 554 - 39 - 82", "+7 609 554 - 39 - 82", "Выполнено", "0.1"],
        ["+7 812 082 - 13 - 41", "+7 812 082 - 13 - 41", "Выполнено", "0.5"]]

tabl2 = [[None, None, None, None],
         ['+7 191 982-11-60', '+7 191 982-11-60', 'Выполнено', '0.6'],
         [None, None, None, None],
         ['+7 609 554-39-82', '+7 609 554-39-82', 'Выполнено', '0.1'],
         ['+7 812 082-13-41', '+7 812 082-13-41', 'Выполнено', '0.5']]

tabl3 = [['+7 624 074-27-80', '+7 624 074-27-80', 'Не выполнено', '0.9'],
         ['+7 263 639-61-68', '+7 263 639-61-68', 'Выполнено', '0.6'],
         [None, None, None, None],
         ['+7 711 965-31-14', '+7 711 965-31-14', 'Не выполнено', '0.8'],
         [None, None, None, None],
         ['+7 737 699-37-84', '+7 737 699-37-84', 'Не выполнено', '0.8']]

print(main(tabl3))
