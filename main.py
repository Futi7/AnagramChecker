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
            for char in sorted(string):
                if char not in keys:
                    keys[char] = 1
                else:
                    keys[char] = keys.get(char) + 1

        if self.list_of_keys[0] == self.list_of_keys[1]:
            print("Is anagram")
        else:
            self.check_required_deletions()



    def check_required_deletions(self):
        chars_to_delete = [0,0]
        first_keys, second_keys = self.list_of_keys
        for key in first_keys:
            if key in second_keys:
                if first_keys[key] > second_keys[key]:
                    chars_to_delete[0] += (first_keys[key] - second_keys[key])
                elif first_keys[key] < second_keys[key]:
                    chars_to_delete[1] += (second_keys[key] - first_keys[key])
            else:
                chars_to_delete[0] += first_keys[key]

        for key in second_keys:
            if key not in first_keys:
                chars_to_delete[1] += second_keys[key]

        print("remove " + str(chars_to_delete[0]) + " characters from '" + self.list_of_strings[0] + "' and " + str(chars_to_delete[1]) + " characters from '" + self.list_of_strings[1] + "'")



if __name__ == "__main__":
    first_string = input("Enter first string:\n")
    second_string = input("Enter second string:\n")
    anagramChecker = AnagramChecker(first_string, second_string)
    print("First:"+anagramChecker.list_of_strings[0]+ "\nSecond:"+anagramChecker.list_of_strings[1])
    anagramChecker.check_if_anagrams()