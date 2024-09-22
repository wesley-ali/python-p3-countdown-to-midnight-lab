import time

def countdown(n):
    while n > 0:
        print(f'{n} SECOND(S)!')
        n -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(n):
    while n > 0:
        print(f'{n} SECOND(S)!')
        time.sleep(1)  # Pause for one second
        n -= 1
    print("HAPPY NEW YEAR!")

# Example:
countdown(10)
countdown_with_sleep(10)  #Runs with a one-second pause

