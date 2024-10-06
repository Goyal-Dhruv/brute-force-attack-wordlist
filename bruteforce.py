import itertools

def generate_wordlist(characters, min_length, max_length, output_file):
    with open(output_file, 'w') as f:
        for length in range(min_length, max_length + 1):
            for combo in itertools.product(characters, repeat=length):
                word = ''.join(combo)
                f.write(word + '\n')

characters = 'abc123'  # Define the character set you want
min_length = 3         # Minimum password length
max_length = 5         # Maximum password length
output_file = 'wordlist.txt'  # Output file name

generate_wordlist(characters, min_length, max_length, output_file)
