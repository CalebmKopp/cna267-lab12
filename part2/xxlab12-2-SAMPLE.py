# Take in a file name from the user
input_file_name = input("Enter a filename to be read: ")

# Open the file specified by the user
example_file = open(input_file_name, 'r')

# Read all the text from that file into some sort of container
#   either a list, or one big string
file_as_a_string = example_file.read()
# In this case, one big string

giberish_string = ""

# Take each element of this container and as a CharacterByte
#   add 4 to the CharacterByte
#   store in a different container (either list or string)
for character in file_as_a_string:
    
    character_byte = ord(character)
    
    giberish_character_byte = character_byte + 4

    giberish_character = chr(giberish_character_byte)

    giberish_string += giberish_character    


# Ask the user for an output filename
output_file_name = input("Enter the name of your outfile: ")

# Open the outfile
output_file = open(output_file_name, 'w')

# Write out the string data from that new container to
#   the output file

output_file.write(giberish_string)

output_file.close()







