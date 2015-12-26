import utility
def remove_null():
    utility.remove_null('user_click_data.txt')

def create_sorted_by_time_file():
    utility.create_sorted_by_time_file()

def generate_training_testing():
    utility.generate_training_testing('user_click_data_sorted.txt')

def generate_training_testing_1():
    utility.generate_training_testing_1('user_click_data_sorted.txt')
#create_sorted_by_time_file()


generate_training_testing_1()
