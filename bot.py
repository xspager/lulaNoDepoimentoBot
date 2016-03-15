import sys
from markovgen import Markov

#markov = Markov(sys.stdin)

db = file('db.pickle', 'r')
markov = Markov.from_database(db)

#while True:
#    print(markov.generate_markov_text(10).capitalize())
#    raw_input("Gerar mais um?")
print(markov.generate_markov_text(13).capitalize())
#import pdb; pdb.set_trace()

#db = file('db.pickle', 'w')
#markov.save_database(db)
