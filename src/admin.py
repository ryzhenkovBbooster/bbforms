import csv

def read_csv(path):
    res = []
    try:
        with open(path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i in reader:
                res.append(i)
        return res
    except Exception as e:
        print('[ERROR]' + str(e))
        return False

def write_csv(res: list, path):
    headers = res[0].keys()

    with open(path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        file.seek(0,2)
        if file.tell() == 0:
            writer.writeheader()
        result = writer.writerows(res)

    return result


def delete_csv(value, path):
    with open(path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader if row['chat_id'] != str(value)]


    res = rewrite(path, rows)

    return res




def rewrite(path, res):
    if len(res) > 0:

        headers = res[0].keys()

        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            file.seek(0, 2)
            if file.tell() == 0:
                writer.writeheader()
            result = writer.writerows(res)

        return result
    else:
        with open(path, 'w', newline='', encoding='utf-8') as file:
            file.write('')

def add_chat(chat_id: int, chatname: str):
    obj = read_csv('chats.csv')
    if obj:

        for i in obj:
            if i['chat_id'] == str(chat_id):
                return False

    res = write_csv([{'chat_id': chat_id, 'chatname': chatname}], 'chats.csv')
    return res





