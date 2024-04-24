# def magical_stairs():

#   for i in range(1, 20):
#     delbar_med_två = int(i) % 2 == 0
#     delbar_med_tre = int(i) % 3 == 0

#     if delbar_med_två  and delbar_med_tre :
#       print(f'Ett magisk hinder på trappstege {i}!')

#     elif delbar_med_två :
#       print(f'Kliv på trappsteg {i} och finn en gnistrande magi')

#     elif delbar_med_tre :
#       print(f'Ett magisk hinder här i trappstegen {i}!')

# magical_stairs()


def mystical_show(tricks):
 
  tricks_mapping = {
    1:"make_hat_levitate", 
    2:"make_coin_disappear",
    3:"take_walet",
    4:"" 
    }
  performed_tricks = [tricks_mapping[int(trick)] for trick in tricks.split(',') if int(trick) in tricks_mapping]
   
 
  for performed_trick in performed_tricks:
   if performed_trick == "make_hat_levitate":
     print('I am making the hat levitate')
   elif performed_trick == 'make_coin_disappear':
     print('I am make the coin disappear')
   elif performed_trick == 'take_walet':
     print('I toke you walet without you noticing')
      
   elif performed_trick == '':
     break
    
    
  


ask_user = input('What trick do you want to see? levitate press 1, disappear press 2, take your walet press 3, or nothing press 4: ')
mystical_show(ask_user)

  
