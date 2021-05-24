import System as sysmain
let_index = 0
complete_code = ''

def read_save_codes():
    index = 0
    with open("Client_File", "r") as ReadCode:
        for var in range(len(sysmain.clients)):
            ReadCode.seek(0)
            code = ReadCode.readlines()[index + 2].rstrip()
            num_code = int(code[1])
            letter_code = code[0]
            index += 4
    ReadCode.close()
    return generateCode(num_code, letter_code)


def generateCode(sys_cl, letter_code):
    global let_index, complete_code
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter_code != 'A':
        for index, let in enumerate(letters):
            if let == letter_code:
                let_index = index
                break

    if sys_cl < 9:
        sys_cl += 1
    else:
        sys_cl = 1
        let_index += 1
    letter = letters[let_index]
    complete_code = letter + str(sys_cl)
    return complete_code
