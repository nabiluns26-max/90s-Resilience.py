friends = ['Semar', 'Gareng', 'Petruk', 'Bagong']
watak = ['bijaksana','humoris','suka menolong', 'setia']
first_message= f"Punakawan yang memiliki watak {watak[0].lower()} yaitu {friends[0].title()}."
second_message= f"Punakawan yang memiliki watak {watak[-3].lower()} yaitu {friends[1].title()}."
third_message= f"Punakawan yang memiliki watak {watak[2].lower()} yaitu {friends[-2].title()}."
fourth_message= f"Punakawan yang memiliki watak {watak[3].lower()} yaitu {friends[-1].title()}." 
print(first_message)
print(second_message)
print(third_message)
print(fourth_message)