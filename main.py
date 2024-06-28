def max_square2 (days):
    c = 0
    n = 1
    while n <= days:
        n=n*2
        c+=1
    return c+1

def insert_between_elements(array, elem):
    if not array:
        return array
    return [subelem for item in array[:-1] for subelem in (item, elem)] + [array[-1]]

def create_array(days):
    c = max_square2(days)
    array=[]
    for i in reversed(range(1, c+1)):
        if array:
            if c in array:
                c-=1
                array=insert_between_elements(array, c)
        else:
            array = [c, c]
    return array

def day_of_year(year, month, day):
    import datetime
    date_obj = datetime.date(year, month, day)
    day_number = date_obj.timetuple().tm_yday
    return day_number

def parse_filename(filename):
    from datetime import datetime
    date_part, value = filename.split('-')
    date = datetime.strptime(date_part, '%d_%m_%Y')
    return date, value

def keep_two_most_recent_backups(folder_path):
    import os
    backups = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.bkp'):
            date, value = parse_filename(filename)
            if value not in backups:
                backups[value] = []
            backups[value].append((date, filename))
    for value in backups:
        backups[value].sort(reverse=True, key=lambda x: x[0])
        recent_backups = backups[value][:2]
        for _, filename in backups[value][2:]:
            os.remove(os.path.join(folder_path, filename))
        backups[value] = recent_backups

def get_today_number ():
    from datetime import datetime
    today = datetime.today()
    year, month, day = today.year, today.month, today.day
    return [day_of_year(year, month, day), day, month, year]

days=365
today_number, day, month, year = get_today_number()
today_value = create_array(days)[today_number-1]
print(f"{day}_{month}_{year}-{today_value}.bkp")


folder_path = 'path/to/your/folder'
keep_two_most_recent_backups(folder_path)
