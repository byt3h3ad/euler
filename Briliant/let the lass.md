[Problem](https://brilliant.org/daily-problems/cryptogram-lass/)
```python
#checking all 10 P 6 = 151200 ways to permute 10 digits to 6 letters - but using recursion to generate the permutations. 
def calc_value(string, dict_vals):
    total = 0
    if dict_vals[string[0]] != 0: # if the leading digit isn't 0
        for letter in string:
            total *= 10
            total += dict_vals[letter]
    return total # returns 0 if a leading digit is 0, which will always make the check false

def generate_selection(letters, current_index, possible_vals, nonselected_vals, vals):
    """ Generates a selection of len(letters) numbers from nonselected_vals; once that selection is achieved,
        it's checked. """
    if current_index == len(letters):
        if calc_value("LET", vals) + calc_value("THE", vals) == calc_value("LASS", vals):
            print("solution:", vals)
            for letter in letters:
                possible_vals[letter].add(vals[letter])
    else:
        for i in range(0, len(nonselected_vals)):
            reinsert = nonselected_vals[i]
            vals[letters[current_index]] = reinsert
            nonselected_vals.pop(i)

            generate_selection(letters, current_index + 1, possible_vals, nonselected_vals, vals)
            nonselected_vals.insert(i, reinsert)

if __name__ == "__main__":
    letters = list(set("LETTHELASS")) 
    possible_vals = dict() # possible_vals[x] is a set containing the possible values for a letter x
    vals = dict()

    for letter in letters:
        possible_vals[letter] = set()

    generate_selection(letters, 0, possible_vals, list(range(10)), vals)

    print("Letters that don't change:", end=' ')
    for letter in possible_vals:
        if len(possible_vals[letter]) == 1:
            print(letter, end = ' ')
    print()
``` 
    
    
    
    
```python
    import itertools
def get_value(in_digit_list):
    """
    returns the number represented by the in_digit_list
    in_digit_list[0] represents the most significant digit
    """
    assert len(in_digit_list) <= 1 or in_digit_list[0] != 0
    res_val = 0
    cur_multip = 1
    for cur_digit in reversed(in_digit_list):
        res_val += cur_multip*cur_digit
        cur_multip *= 10
    return res_val

def check(in_data):
    """
    checks if in_data represents a solution of:
        https://brilliant.org/daily-problems/cryptogram-lass/
    """
    def get_value_of_str(in_str):
        return get_value([in_data[_] for _ in in_str])
    if 0 in [in_data['L'], in_data['T']]:
        res = False
    else:
        val_1 = get_value_of_str("LET")
        val_2 = get_value_of_str("THE")
        val_3 = get_value_of_str("LASS")
        res = val_1+val_2 == val_3
    return res

FREE_LETTER_LIST = sorted(list(set("LETTHELASS")))
SOL_LIST = []
print("Solutions:")
for cur_data in itertools.permutations(list(range(10)), r=len(FREE_LETTER_LIST)):
    cur_dict = dict(zip(FREE_LETTER_LIST, cur_data))
    if check(cur_dict):
        print(cur_dict)
        SOL_LIST.append(cur_dict)
print("Fixed letters:")
for cur_letter in FREE_LETTER_LIST:
    tmp_val_set = {tmp_dict[cur_letter] for tmp_dict in SOL_LIST}
    if len(tmp_val_set) == 1:
        print(cur_letter)
```
