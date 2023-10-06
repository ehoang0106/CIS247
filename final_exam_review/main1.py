from Movie import Movie



def main():
    m1 = Movie("Indian Jones")
    m2 = Movie("Harry Potter")

    m1.add_review(1)
    m1.add_review(1)

    m1.add_review(2)
    m1.add_review(2)
    m1.add_review(3)
    m1.add_review(4)
    m1.add_review(4)
    m1.add_review(5)

    m2.add_review(2)
    m2.add_review(5)
    m2.add_review(3)
    
    print(m1)
    print(m2)
    print(m1.get_avg())
    
main()