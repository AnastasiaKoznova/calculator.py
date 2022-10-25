import controller as c
import view as v
import model

if v.what_to_do() == 1:
    form_file = v.input_name_file()
    new_line = 'Yes'
    while new_line == 'Yes':
        c.add_phone_number(form_file, *v.input_numbers())
        new_line = v.new_input()
else:
    print(c.import_phone_number(v.output_name_file()))

async def add(update, context) -> None: # Добавление записи
    msg = update.message.text
    in_info = msg.split()
    print(msg)
    model.add_info(in_info)    