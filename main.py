print("***Welcome to the NIGHT ALONE***")

options = ["A", "a", "B", "b"]

name = input("Hello there, what is your name?")

print(f"Hello{name}! Let's start this amazing and eerie adventure.")

def start():
  print("Its late at night on a thursday afternoon when your parents have a last minute buissness trip over night.")

  print("Your parents are only gone for one night and you have our dog so you are not worried. But, when you are sleeping, you hear dripping sounds somewhere inside your house.")

  scene1 = input("What do you do? \n A) Go and check out the bathroom for any water leaks \n B) Stay in bed because you are too lazy")

  while scene1 not in options:
    print("Not a valid option. Please answer A or B") 
    scene1 = input("What do you do? \n A) Go and check out the bathroom for any water leaks \n B) Stay in bed because you are too lazy")

  scene1_options(scene1)



def scene1_checking():
  print("There is no leakage and you decide to go back to your bed.")

def scene1_lazy():
  print("You wait until the morning to check what the sound was.")


def scene1_options(scene1):
  if scene1 == "A":
    scene1_checking()
  elif scene1 == "B":
    scene1_lazy()
  else:
    print("Hey man, you gotta choose A or B")
    start()


def main():
  start()


main()



