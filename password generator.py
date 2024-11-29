import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Define possible character sets
    char_sets = []
    
    if use_letters:
        char_sets.append(string.ascii_letters)  # includes both lowercase and uppercase letters
    if use_numbers:
        char_sets.append(string.digits)  # includes digits 0-9
    if use_symbols:
        char_sets.append(string.punctuation)  # includes common punctuation symbols
    
    # If no character set is selected, raise an error
    if not char_sets:
        raise ValueError("You must select at least one character set (letters, numbers, symbols).")
    
    # Combine all selected character sets
    all_chars = ''.join(char_sets)
    
    # Generate a random password by selecting 'length' characters from the combined set
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Python Password Generator!")
    
    # Get password criteria from the user
    try:
        length = int(input("Enter the password length: "))
        if length <= 0:
            print("Password length should be a positive number.")
            return
        
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        # Generate the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
