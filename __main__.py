from data_grapper import fetch_info
import sys


def get_args():
    title_from_arg = ''
    args = sys.argv
    args.pop(0)
    try:
        if args[0] == '--help' or args[0] == '-h':
            print('heeelp')
            exit(0)
        else:
            title_from_arg = ' '.join(args)
    except IndexError:
        print('For usage information use: --help or -h')
        exit(0)
    return title_from_arg


def display(data):
    print('-----------------------------')
    print('Title:   ', data[0], data[3], '('+data[2]+')')
    print('Rating:  ', data[5], 'Out', data[6], 'Votes')
    print('Genre:   ', data[4], '|', 'Runtime:', data[1])
    print('Actors:  ', data[9])
    print('Director:', data[8])
    print('Writer:  ', data[10])
    print('Link:    ', 'http://www.imdb.com/title/' + data[11])
    print('Plot:    ', data[7])
    print('-----------------------------')


def main():
    title = get_args()
    title_info = fetch_info(title)

    if not title_info:
        exit(0)
    else:
        display(title_info)


if __name__ == '__main__':
    main()
