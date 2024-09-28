import os

class MealProvider:
    def __init__(self):
        self.base_path = 'static/html'

    def get_meal(self, day):
        file_path = os.path.join(self.base_path, f'{day}.html')
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return f"No meal found for day {day}"
        except IOError:
            return f"Error reading meal file for day {day}"