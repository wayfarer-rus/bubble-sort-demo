import random
import time
import sys
from bubble_sort import bubble_sort

def to_roman(n):
    """Convert an integer to a Roman numeral."""
    val = [
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return roman_num

def main():
    print("Welcome to the Weird Counter!")
    print("To reach 100, we must satisfy the Bubble Sort gods for each step.")
    print("Each number must be manifested through a computational ritual.")
    print("-" * 50)
    
    start_time = time.monotonic()
    
    for i in range(1, 101):
        # Ritual difficulty increases linearly
        # Size 100 to 8000
        list_size = i * 80 
        data = [random.randint(0, 10000) for _ in range(list_size)]
        
        # Perform the ritual
        bubble_sort(data)
        
        # Tiny delay to let the universe breathe
        time.sleep(random.uniform(0.01, 0.03))
        
        # Display the result in a weird way (Roman Numerals)
        roman = to_roman(i)
        progress = f"[{i:3}/100]"
        message = f" Ritual complete: {roman}"
        
        # Use carriage return to keep it on one line mostly, but milestone on new lines
        sys.stdout.write(f"\r{progress}{message} (Complexity: {list_size})")
        sys.stdout.flush()
        
        if i % 10 == 0:
            print(f"\n>>> MILESTONE {i} REACHED <<<")

    end_time = time.monotonic()
    print("-" * 50)
    print(f"The 100 numbers have been manifested in {end_time - start_time:.2f} seconds.")
    print("The ritual is complete. The count is done.")

if __name__ == "__main__":
    main()
