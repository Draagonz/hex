import streamlit as st

def split_hex_to_8bit(hex_str):
    try:
        # Remove any leading '0x' or spaces
        hex_str = hex_str.strip().replace('0x', '').replace(' ', '')
        
        # Check if the input is a valid 24-bit hex
        if len(hex_str) != 6:
            raise ValueError("Input must be a 24-bit hexadecimal value (6 characters).")
        
        # Split into three 8-bit hex values
        hex1 = hex_str[0:2]
        hex2 = hex_str[2:4]
        hex3 = hex_str[4:6]
        
        return hex1, hex2, hex3
    except ValueError as e:
        st.error(str(e))
        return None, None, None

def hex_to_binary(hex_str, bits=8):
    try:
        # Convert hex to integer
        int_value = int(hex_str, 16)
        
        # Convert integer to zero-padded binary string
        binary_str = f"{int_value:0{bits}b}"
        
        return binary_str
    except ValueError as e:
        st.error(str(e))
        return ""

def reverse_bits(binary_str):
    # Reverse the binary string
    return binary_str[::-1]

def binary_not(binary_str):
    # Perform binary NOT operation
    return ''.join('1' if bit == '0' else '0' for bit in binary_str)

def binary_to_hex(binary_str):
    # Convert binary string to hexadecimal
    return f"{int(binary_str, 2):02X}"

def split_32bit_to_16bit(hex_32bit):
    # Split 32-bit hex into two 16-bit parts
    part1 = hex_32bit[0:4]  # First 16 bits
    part2 = hex_32bit[4:8]  # Second 16 bits
    return f"0x{part1}", f"0x{part2}"

def main():
    st.title("24-bit Hex to 8-bit Split, Binary, Reversed, NOT, and 32-bit HEX Converter")

    # Input: 24-bit Hex
    hex_input = st.text_input("Enter 24-bit Hex:", value="A1B2C3", max_length=6)

    if st.button("Convert"):
        hex1, hex2, hex3 = split_hex_to_8bit(hex_input)
        
        if hex1 and hex2 and hex3:
            # Display 8-bit Hex values
            st.subheader("8-bit Hex Values")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.text_input("8-bit Hex 1:", value=hex1, disabled=True)
            with col2:
                st.text_input("8-bit Hex 2:", value=hex2, disabled=True)
            with col3:
                st.text_input("8-bit Hex 3:", value=hex3, disabled=True)

            # Convert to Binary
            binary1 = hex_to_binary(hex1)
            binary2 = hex_to_binary(hex2)
            binary3 = hex_to_binary(hex3)

            st.subheader("Binary Conversion")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.text_input("Binary 1:", value=binary1, disabled=True)
            with col2:
                st.text_input("Binary 2:", value=binary2, disabled=True)
            with col3:
                st.text_input("Binary 3:", value=binary3, disabled=True)

            # Reverse Bits
            reversed1 = reverse_bits(binary1)
            reversed2 = reverse_bits(binary2)
            reversed3 = reverse_bits(binary3)

            st.subheader("Reversed Bits")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.text_input("Reversed 1:", value=reversed1, disabled=True)
            with col2:
                st.text_input("Reversed 2:", value=reversed2, disabled=True)
            with col3:
                st.text_input("Reversed 3:", value=reversed3, disabled=True)

            # Binary NOT of Reversed 3
            not_reversed3 = binary_not(reversed3)
            st.text_input("NOT Reversed 3:", value=not_reversed3, disabled=True)

            # Convert Reversed and NOT to Hex
            hex_reversed1 = binary_to_hex(reversed1)
            hex_reversed2 = binary_to_hex(reversed2)
            hex_reversed3 = binary_to_hex(reversed3)
            hex_not_reversed3 = binary_to_hex(not_reversed3)

            st.subheader("Reversed Bits to HEX")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.text_input("HEX Reversed 1:", value=hex_reversed1, disabled=True)
            with col2:
                st.text_input("HEX Reversed 2:", value=hex_reversed2, disabled=True)
            with col3:
                st.text_input("HEX Reversed 3:", value=hex_reversed3, disabled=True)
            with col4:
                st.text_input("HEX NOT Reversed 3:", value=hex_not_reversed3, disabled=True)

            # Joined 32-bit HEX Value
            joined_32bit_hex = hex_reversed1 + hex_reversed2 + hex_reversed3 + hex_not_reversed3
            st.subheader("32-bit HEX Value")
            st.text_input("32-bit HEX:", value=joined_32bit_hex, disabled=True)

            # Split 32-bit HEX into 16-bit parts
            split_16bit_1, split_16bit_2 = split_32bit_to_16bit(joined_32bit_hex)
            st.subheader("16-bit Split Values")
            st.text_input("16-bit Split (0x):", value=f"{split_16bit_1}, {split_16bit_2}", disabled=True)

if __name__ == "__main__":
    main()
