bot_name: str = 'Bob'
print(f"Hello! I'm {bot_name}! How can I assist you today?")

while True:
    user_input: str = input('You: ').lower().strip()

    if user_input in ['hi', 'hello']:
        print(f'{bot_name}: Hi there! How can I help you?')
        
    elif user_input in ['bye', 'goodbye']:
        print(f'{bot_name}: Goodbye! Have a great day!')
        break  # Stops the loop so the program actually exits
        
    elif user_input in ['+', 'add']:
        print(f'{bot_name}: Sure! Let\'s add two numbers.')
        try:
            num1: float = float(input('Enter the first number: '))
            num2: float = float(input('Enter the second number: '))
            print(f'{bot_name}: {num1} + {num2} = {num1 + num2}')
        except ValueError:
            print(f'{bot_name}: Oops! Please enter valid numbers next time.')
            
    else:
        print(f'{bot_name}: I\'m sorry, I didn\'t understand that.')

