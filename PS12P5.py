def load_arrays(lname3, batavg):
  with open("myfile.txt", "r") as f:
      for _ in range(10):
          player_data = f.readline().strip().split(',')
          if player_data:  
              lname3.append(player_data[0])
              batavg.append(float(player_data[1]))
          else:
              break  

def display_arrays(lname3, batavg):
  for i in range(len(lname3)):
      print(lname3[i], "has a batting average of", batavg[i])
      print("                 ")

def search_lastname(lname3, batavg):
  while True:
      search_name = input("Enter a last name to search for (or 'exit' to quit): ")
      if search_name.lower() == 'exit':
          break
      if search_name in lname3:
          index = lname3.index(search_name)
          print(search_name, "has a batting average of", batavg[index])
      else:
          print("Last name not found.")

lname3 = []
batavg = []
load_arrays(lname3, batavg)
display_arrays(lname3, batavg)
search_lastname(lname3, batavg)