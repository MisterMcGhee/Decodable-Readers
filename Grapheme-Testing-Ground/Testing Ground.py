import requests


def load_graphemes():
    f = open('graphemes.txt', 'r')
    graphemes = f.read()
    graphemes_list = graphemes.split()
    f.close()
    return graphemes_list


def get_target_grapheme(grapheme_list):
    student_level = int(input("What level is the student at?"))
    target_grapheme = grapheme_list[student_level]
    return target_grapheme


def get_grapheme_words(target_grapheme):
    url = "http://api.datamuse.com/words?sp=*" + target_grapheme + "*"
    response = requests.get(url)
    words = response.json()
    return [word["word"] for word in words]


def main():
    grapheme_list = load_graphemes()
    target_grapheme = get_target_grapheme(grapheme_list)
    grapheme_words = get_grapheme_words(target_grapheme)
    print(grapheme_words)
    print(len(grapheme_words))


if __name__ == '__main__':
    main()
