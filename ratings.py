"""Restaurant rating lister."""


# put your code here
open_file = open('scores.txt')


def score_compiler(file):
    dict = []
    for i in file:
        values = i.split(':')
        name = values[0]
        rating = values[1].strip()
        dict.append({'name': name,
                            'rating': rating})
    return dict

score_dict = score_compiler(open_file)
open_file.close()

def sorted_loop(dict):
    loop_listed = []
    for i in dict:
        name = i.get('name')
        rating = i.get('rating')
        loop_listed.append(f"{name} is rated at {rating}.")
    return sorted(loop_listed)

# print(sorted_loop(score_dict))


def user_access(dict):
    while True:
        user_input = input('what would you like to do?')
        if (user_input == 'add' ):
            name = input('whats the name of the resturant?')
            rating = int(input('how would you rate it?'))
            dict.append({'name': name,
                        'rating': rating})
            looper = sorted_loop(dict)
            for i in looper:
                print(i)
        elif(user_input == 'view'):
            looper = sorted_loop(dict)
            for i in looper:
                print(i)
        elif(user_input == 'exit'):
            print('ok, take care =]')
            break
        else:
            print('invalid input, try again')


user_access(score_dict)