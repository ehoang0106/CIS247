

class Movie:
    def __init__(self, movie_name):

        self._movie_name = movie_name
        self._num_reviews = 0
        self._reviews = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        

    @property
    def movie_name(self):
        return self._movie_name
    @movie_name.setter
    def movie_name(self, new_movie_name):
        self._movie_name = new_movie_name


     
    def add_review(self, num_stars):
        #if rating is invalid
        if num_stars < 1 or num_stars > 5:
            print("Invalid number of start! Review must be between 1 and 5")
            return
        
        #rating is valid. Increment its value in the dictionary

        self._reviews[num_stars] += 1
        self._num_reviews += 1

    
        
    def get_avg(self):
        total_stars = self._reviews[1]
        total_stars += self._reviews[2] * 2
        total_stars += self._reviews[3] * 3
        total_stars += self._reviews[4] * 4
        total_stars += self._reviews[5] * 5

        return round(total_stars / self._num_reviews, 2)
        
    def __str__(self):
        return_string = self._movie_name + '\n'
        return_string += f'1 Star: {self._reviews[1]}' + '\n'
        return_string += f'2 Star: {self._reviews[2]}' + '\n'
        return_string += f'3 Star: {self._reviews[3]}' + '\n'
        return_string += f'4 Star: {self._reviews[4]}' + '\n'
        return_string += f'5 Star: {self._reviews[5]}' + '\n'


        return return_string

