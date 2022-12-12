score = 0

def do_quiz(question, answer):
  # We have attempts from 3 to 1
  # range(start, stop, interval)
  global score
  for attempt in range(3, 0, -1):
    inp = input(question)
    if inp == answer:
      score = score + 1
      print("Correct Answer. " + "Your score is " + str(score) + ".")
      return
    else:
      print("Try again, attempts remaining: ", attempt - 1)
  print("You couldn't figure it out")


do_quiz("What is 5+5 ", "10")
