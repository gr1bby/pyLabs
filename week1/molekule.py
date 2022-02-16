from collections import Counter


def parse_molecule(molecule: str) -> dict:
    # this list will contain final list and nested lists
    atoms = [[]]
    for el in molecule:
        # checking capital letter or not
        if el.isalpha() and el.istitle():
            # 'last' is main var here; 
            # in many cases we add directly this to the final list.
            last = [el]
            upper = el
            atoms[-1].append(el)
        # checking lowercase letter or not
        elif el.isalpha():
            last = upper + el
            atoms[-1] = [last]
        # checking for digital    
        elif el.isdigit():
            atoms[-1].extend(last*(int(el)-1))
        # in next two blocks checking for parentheses
        elif el == '(' or el == '[' or el == '{':
            # when parenthes is opening we make addition list inside 'atoms'
            # for processing included atoms
            atoms.append([])
        elif el == ')' or el == ']' or el == '}':
            last = atoms.pop()
            atoms[-1].extend(last)

    return dict(Counter(atoms[-1]))


if __name__ == '__main__':
    print(parse_molecule("K4[ON(SO3)2]2"))
