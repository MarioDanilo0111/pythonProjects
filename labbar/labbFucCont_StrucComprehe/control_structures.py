def magical_stairs():

  for i in range(1, 20):
    delbar_med_två = int(i) % 2 == 0
    delbar_med_tre = int(i) % 3 == 0

    if delbar_med_två  and delbar_med_tre :
      print(f'Ett magisk hinder på trappstege {i}!')

    elif delbar_med_två :
      print(f'Kliv på trappsteg {i} och finn en gnistrande magi')

    elif delbar_med_tre :
      print(f'Ett magisk hinder här i trappstegen {i}!')

magical_stairs()