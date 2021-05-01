key = input().split()
key = list(map(int, key))

line = input()

while line != "find":
    helping = ""
    translated_msg = ""
    start = 0
    end = 0

    for elements_indexes in range(0,len(line)+len(key),len(key)):
        start = end
        end = elements_indexes
        helping = line[start:end]

        for index in range(len(helping)):
            translated_msg += chr(ord(helping[index])-key[index])

    tr_type = translated_msg.split("&")[1]
    tr_coordinates_start = translated_msg.index("<")
    tr_coordinates_end = translated_msg.index(">")

    print(f"Found {tr_type} at {translated_msg[tr_coordinates_start+1:tr_coordinates_end]}")

    line = input()

