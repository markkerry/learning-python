# First open the file with append
file = open("example-file.txt", "a")

# Add escape charater to add a new line first
file.write("\n# EOF")

# Close the file
file.close()

# Create a new file which doesn't exist
file_new = open("index.html", "w")
file_new.write("<p>This HTML file was created with Python</p>")
file_new.close()