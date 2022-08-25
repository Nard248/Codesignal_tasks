def solution_reverse_in_parenthesis(input_string):
    st = []

    for i in range(len(input_string)):

        # Push the index of the current
        # opening bracket
        if input_string[i] == '(':
            st.append(i)

        # Reverse the substring starting
        # after the last encountered opening
        # bracket till the current character
        elif input_string[i] == ')':
            temp = input_string[st[-1]:i + 1]
            input_string = input_string[:st[-1]] + temp[::-1] + input_string[i + 1:]
            del st[-1]

    # To store the modified string
    res = ""
    for i in range(len(input_string)):
        if input_string[i] != ')' and input_string[i] != '(':
            res += (input_string[i])
    return res
