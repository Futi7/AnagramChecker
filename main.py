class AnagramChecker:

    list_of_strings = []
    first_string_keys = {}
    second_string_keys = {}
    list_of_keys = [first_string_keys, second_string_keys]

    def __init__(self, first_string, second_string):
        self.list_of_strings.append(first_string)
        self.list_of_strings.append(second_string)

    def check_if_anagrams(self):
        for string, keys in zip(self.list_of_strings, self.list_of_keys):
            for char in string:
                if char not in keys:
                    keys[char] = 1
                else:
                    keys[char] = keys.get(char) + 1

        if self.list_of_keys[0] == self.list_of_keys[1]:
            print("Is anagram")
        else:
            print("Not anagram")




    def check_required_deletions():
        


if __name__ == "__main__":
    first_string = input("Enter first string:\n")
    second_string = input("Enter second string:\n")
    anagramChecker = AnagramChecker(first_string, second_string)
    print("First:"+anagramChecker.list_of_strings[0]+ "\nSecond:"+anagramChecker.list_of_strings[1])
    anagramChecker.check_if_anagrams()