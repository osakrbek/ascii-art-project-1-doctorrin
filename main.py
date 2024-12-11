import sys


# Define the load_banner function
def load_banner(file_path):
    with open(file_path, "r") as f:
        lines = f.read().splitlines()

    banner_dict = {}
    ascii_height = 8  # Each character occupies 8 lines
    start = 0

    for i in range(95):  # ASCII printable characters (32-126)
        char_lines = lines[start : start + ascii_height]
        banner_dict[chr(32 + i)] = char_lines
        start += ascii_height + 1  # Include a blank line separator

    return banner_dict


# Define the render_text function
def render_text(input_text, banner_dict):
    ascii_height = 8
    output_lines = ["" for _ in range(ascii_height)]

    for char in input_text:
        if char == "\n":
            output_lines.append("")
        elif char in banner_dict:
            char_lines = banner_dict[char]
            for i in range(ascii_height):
                output_lines[i] += char_lines[i]
        else:  # Handle unsupported characters
            for i in range(ascii_height):
                output_lines[i] += "." * len(banner_dict[" "])  # Substitute with spaces

    return "\n".join(output_lines)


# Main function
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <text>")
        return

    input_text = sys.argv[1]
    banner_file = "standard.txt"  # Default banner
    banner_dict = load_banner(banner_file)

    ascii_art = render_text(input_text, banner_dict)
    print(ascii_art)


if __name__ == "__main__":
    main()
