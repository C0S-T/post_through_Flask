import statistics
def read_swim_data(FOLDER,filename):
    swimmer,age,meters,style = filename.removesuffix('.txt').split('-')
    #print(f'{swimmer},{age},{meters},{style}')
    with open(FOLDER + filename, 'r') as f:
        data = f.read().strip().split(',')
    convert_time=[]
    for i in data:
        first = i
        if ':' in first:
            mins,rest = first.split(':')
            seconds,hundredths = rest.split('.')
        else :
            mins = 0
            seconds,hundredths = first.split('.')
        convert_time.append((int(mins)*60*100) + (int(seconds)*100) + (int(hundredths)))
    #print(f'time : {convert_time}') 
    c= round((statistics.mean(convert_time))/100,2)
    #print(f'Mean time : {c}')
    min_secs,hund = str(c).split('.')
    min = int(min_secs) // 60
    sec = int(min_secs) - (min*60)
    average = f'{min} : {sec} . {hund}'
    #print(f'Average Time : {average}')
    return swimmer,age,meters,style,convert_time,average