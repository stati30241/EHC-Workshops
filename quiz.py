score = 0

def main():
    do_quiz("Who is the best person ever? ", "sahib")

def do_quiz(question, answer):
    # We have attempts from 1 to 3
    for attempt in range(3, 0, -1):
        inp = input(question)
        if inp == answer:
            print("Correct Answer")
            score = score + 1
            return
        else:
            print("Try again, attempts remaing: ", attempt - 1)
    print("You couldn't figure it out")

if __name__ == "__main__":
    main()
