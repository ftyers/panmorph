import argparse
parser = argparse.ArgumentParser()
# The input file name is required
parser.add_argument("-i", "--input", type=str, required=True, help="input file")
# The output file name is optional
parser.add_argument("-o", "--output", type=str, help="output file")
args = parser.parse_args()

with open(args.input, "r") as ud_text:  # Read input file name from command-line
    # Delete the last blank line
    texts = ud_text.read()[:-1]
    # Split the texts by blank lines
    separate_text = texts.split("\n\n")
    output = ""
    for text in separate_text:
        lines = text.split("\n")
        for line in lines:
            # Separate comments that contain the text_id, text content, and optional translation
            if line[0] == "#":
                output += line + "\n"
            # Remove the lines in UD used for ellipsis analysis
            elif "." in line.split()[0]:
                continue
            # Transform the token information into Panmorph format
            else:
                strings = line.split()
                # Set the default value
                token = strings[0] + "\t" + strings[1] + "\t" + ("_" + "\t") * 8
                output += token + "\n"
        output += "\n"

# If the output file is specified, then write to specified file
if args.output:
    pan_text = open(args.output, "w+")
    pan_text.write(output)
    pan_text.close()
# Otherwise output to StdOut
else:
    print output

ud_text.close()
