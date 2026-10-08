def main():
    print("--- Python Type Casting Demonstration ---\n")

    # 1. Integer to Float
    val_int = 10
    val_float = float(val_int)
    print(f"Integer: {val_int} ({type(val_int)}) -> Float: {val_float} ({type(val_float)})")

    # 2. Float to Integer
    val_f = 9.87
    val_i = int(val_f)  # Note: This truncates the decimal part
    print(f"Float: {val_f} -> Integer (Truncated): {val_i}")

    # 3. Numeric to String
    age = 25
    str_age = str(age)
    print(f"Numeric: {age}(type : {type(age)}) -> String: {str_age}(type : {type(str_age)})")

    # 4. String to Numeric
    num_str = "123.5"
    converted_num = float(num_str)
    print(f"String: {num_str} ({type(num_str)}) -> Integer: {converted_num}({type(converted_num)})")

    # 5. List to Tuple and Set
    my_list = [1, 2, 2, 3]
    my_tuple = tuple(my_list)
    my_set = set(my_list)  # Sets remove duplicates
    print(f"\nList: {my_list}")
    print(f"Tuple: {my_tuple}")
    print(f"Set (duplicates removed): {my_set}")

    # 6. String to List
    word = "Python"
    char_list = list(word)
    print(f"\nString: '{word}' -> List of characters: {char_list}")

if __name__ == "__main__":
    main()