"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""


def fn_hack_10():
    result = "fooziman"
    # ...\
    upperResult = result.upper()
    lst = []
    for letter in upperResult:
        lst.append(letter)
    lst[1:3] = ["0", "0"]
    lst[4] = "1"
    lst[6] = "@"

    return lst
