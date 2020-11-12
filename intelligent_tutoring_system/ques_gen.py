import random

class Ques_Gen_Book:

    def __init__(self):
        self.tables = {
        'Customer':['cust_id','lname','fname','area','phone_no'],
        'Invoice':['inv_no','book_no','cust_id','issue_date','return_date'],
        'Book':['book_no','title','genre','author','price']
        }

        self.cust_ids = [1,2,3,4,5,6,7,8]
        self.inv_nos = [201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216]
        self.cust_fnames = ['Devansh', 'Himanshu', 'Ansh', 'Parth', 'Bhavesh', 'Dhaval', 'Riddhi', 'Srishti']
        self.cust_lnames = ['Mehta','Ashar', 'Shah', 'Tank','Singh','Prasad']
        self.cust_areas = ['Malad','Parle','Bandra','Ulhasnagar','Thane','Borivali','Kandivali','Chembur']
        self.invoice_issue_dates = []
        self.invoice_return_dates = []
        self.book_titles = ['One Hundred Years of Solitude', 'Flowers in the Attic', 'The Eagle Has Landed', 'Then There Were None', 'A Tale of Two Cities', 'Lord of the Rings', 'The Catcher in the Rye', 'Harry Potter', 'Immortals of Meluha']
        self.book_genres = ['Magic Realism', 'Young Adult', 'Historical', 'Mystery', 'Classic Literary', 'Fiction', 'Fiction', 'Fantasy','Mythology']
        self.book_authors = ['Gabriel Marquez','V.C.Andrews', 'Jack Higgings','Agatha Cristie','Charles Dickens', 'J.R.R.Tolkein','J.D Salinger', 'JK Rowling','Amish']
        self.book_prices = [699, 999, 499, 649, 1099, 749, 1599, 1899, 399]
        self.phone_nos = [1232424,3453455,2348564, 7645523,8723454, 9675467, 7867868, 3453534]

    def lvl_1_ques(self):

        ques_list = []
        query_list = []

        tables_list = list(self.tables.keys())
        table_name = random.choice(tables_list)
        ques = 'Retrieve all values from the table '+table_name
        query = 'SELECT * FROM '+table_name
        ques_list.append(ques)
        query_list.append(query)

        tab_name = random.choice(tables_list)
        cols = random.sample(range(0,len(self.tables[tab_name])),2)
        ques = 'Write an SQL query to get '+self.tables[tab_name][cols[0]]+' and '+self.tables[tab_name][cols[1]]+' from '+tab_name
        query = 'SELECT '+self.tables[tab_name][cols[0]]+', '+self.tables[tab_name][cols[1]]+' FROM '+tab_name
        ques_list.append(ques)
        query_list.append(query)

        ques = 'Get all details of customers having no phone number'
        query = 'SELECT * FROM Customer WHERE phone_no is NULL'
        ques_list.append(ques)
        query_list.append(query)

        cust_fname = random.choice(self.cust_fnames)
        ques = 'Get the rows where the Customer has first name "'+cust_fname+'".'
        query = 'SELECT * FROM Customer WHERE fname like "'+cust_fname+'"'
        ques_list.append(ques)
        query_list.append(query)

        cust_lname = random.sample(self.cust_lnames,2)
        ques = 'What is the customer ID of Customer having last name "'+cust_lname[0]+'" or "'+cust_lname[1]+'".'
        query = 'SELECT cust_id FROM Customer WHERE lname like "'+cust_lname[0]+'" OR lname like "'+cust_lname[1]+'"'
        ques_list.append(ques)
        query_list.append(query)

        i = random.randint(0,len(ques_list)-1)
        ques = ques_list[i]
        query = query_list[i]

        return ques, query

    def lvl_2_ques(self):
        ques_list = []
        query_list = []
        #customer specific
        fname_starts_with = ['D','H','B','R','S'] #put all 4 in a dictionary of lists, randomise and execute in a single question
        lname_starts_with = ['M','A','S','T','P']
        fname_ends_with = ['H','U','L','I']
        lname_ends_with = ['A','R','H','K','D',]

        fname_starting = random.choice(fname_starts_with)
        ques = 'Retrieve all Customer details having their first name starting with "'+fname_starting+'"'
        query = 'SELECT * FROM Customer WHERE fname like "'+fname_starting+'%"'
        ques_list.append(ques)
        query_list.append(query)

        lname_ending = random.choice(lname_ends_with)
        ques = 'Get the area of the Customer whose last name ends with "'+lname_ending+'"'
        query = 'SELECT area FROM Customer WHERE lname like "%'+lname_ending+'"'
        ques_list.append(ques)
        query_list.append(query)

        fname_ending = random.choice(fname_ends_with)
        ques = 'Which Customers have '+fname_ending+' at the end of their first name? Get all details.'
        query = 'SELECT * FROM Customer WHERE fname like "%'+fname_ending+'"'
        ques_list.append(ques)
        query_list.append(query)

        lname_starting = random.choice(lname_starts_with)
        ques = 'List the phone number of Customers who have the letter "'+lname_starting+'" at the beginning of their last name.'
        query = 'SELECT phone_no FROM Customer WHERE lname like "'+lname_starting+'%"'
        ques_list.append(ques)
        query_list.append(query)

        #book specific
        title_starts_with = ['O','F','T','A','L','H','I'] #put all 4 in a dictionary of lists, randomise and execute in a single question
        title_ends_with = ['E','C','D','S','R','A']
        author_starts_with = ['G','V','J','A','C']
        author_ends_with = ['Z','S','E','N','R','G','H']

        authorname_starting = random.choice(author_starts_with)
        ques = "What are the names of the Books with author names starting with '"+authorname_starting+"'?"
        query = 'SELECT title FROM Book where author like "'+authorname_starting+'%"'
        ques_list.append(ques)
        query_list.append(query)

        authorname_ending = random.choice(author_ends_with)
        ques = "Get all rows of Books with '"+authorname_ending+"' at the end of the author name?"
        query = 'SELECT * FROM Book where author like "%'+authorname_ending+'"'
        ques_list.append(ques)
        query_list.append(query)

        title_starting = random.choice(title_starts_with)
        ques = 'What is the name of the author who wrote the Book whose name starts with "'+title_starting+'"?'
        query = 'SELECT author FROM Book where title like "'+title_starting+'%"'
        ques_list.append(ques)
        query_list.append(query)

        title_ending = random.choice(title_ends_with)
        ques = 'What is the price of the books whose name ends with "'+title_ending+'"?'
        query = 'SELECT price FROM Book where title like "%'+title_ending+'"'
        ques_list.append(ques)
        query_list.append(query)

        i = random.randint(0,len(ques_list)-1)
        ques = ques_list[i]
        query = query_list[i]

        return ques,query

    def lvl_3_ques(self):
        ques_list = []
        query_list = []

        range_price = random.sample(self.book_prices,2)
        range_price.sort()
        ques = 'What are the titles of the books which have a price between '+str(range_price[0])+' and '+str(range_price[1])+'?'
        query = 'SELECT title FROM Book WHERE price>'+str(range_price[0])+' and price<'+str(range_price[1])
        ques_list.append(ques)
        query_list.append(query)

        ques = 'List all the details about books with titles sorted in ascending order.'
        query = 'SELECT * FROM Book ORDER BY title'
        ques_list.append(ques)
        query_list.append(query)

        range_id = random.sample(self.cust_ids,2)
        range_id.sort()
        ques = 'Retrieve the phone numbers of the customers whose IDs are between '+str(range_id[0])+' and '+str(range_id[1])+'.'
        query = 'SELECT phone_no FROM Customer WHERE cust_id>'+str(range_id[0])+' and cust_id<'+str(range_id[1])
        ques_list.append(ques)
        query_list.append(query)

        ques = 'Mention unique genres of all books in the data.'
        query = 'SELECT DISTINCT genre FROM Book'
        ques_list.append(ques)
        query_list.append(query)

        ques = 'Calculate the total price of all the Books.'
        query = 'SELECT SUM(price) FROM Book'
        ques_list.append(ques)
        query_list.append(query)

        ques = 'Find the number of Books from each genre.'
        query = 'SELECT COUNT(title), genre FROM Book GROUP BY genre'
        ques_list.append(ques)
        query_list.append(query)

        price_avg = random.choice(self.book_prices)
        ques = 'Find the average price for each genre that has an average price over '+str(price_avg)+'.'
        query = 'SELECT AVG(price), genre FROM Book GROUP BY genre HAVING AVG(price)>'+str(price_avg)
        ques_list.append(ques)
        query_list.append(query)

        i = random.randint(0,len(ques_list)-1)
        ques = ques_list[i]
        query = query_list[i]

        return ques, query

    def lvl_4_ques(self):
        ques_list = []
        query_list = []

        ques = 'What are the last and first names respectively of those customers who have been issued some Book.'
        query = 'SELECT c.lname,c.fname FROM Customer c, Invoice i WHERE c.Cust_id=i.Cust_id'
        ques_list.append(ques)
        query_list.append(query)

        inv_no_choose = random.choice(self.inv_nos)
        ques = 'What is the customer name who has an invoice no of '+str(inv_no_choose)
        query = 'SELECT c.fname,c.lname FROM Customer c, Invoice i WHERE c.Cust_id=i.Cust_id and i.Inv_no='+str(inv_no_choose)
        ques_list.append(ques)
        query_list.append(query)

        i = random.randint(0,len(ques_list)-1)
        ques = ques_list[i]
        query = query_list[i]

        return ques,query


class Ques_Gen_Movie:

    def __init__(self):
        self.tables = {
        'movie':['mov_id','mov_title','mov_year','mov_time','mov_lang','mov_dt_rel','mov_rel_country'],

        'movie_cast':['act_id','mov_id','role'],
        'actor':['act_id','act_fname','act_lname','act_gender'],

        'movie_genres':['mov_id','gen_id'],
        'genres':['gen_id','gen_title'],

        'movie_direction':['dir_id','mov_id'],
        'director':['dir_id','dir_fname','dir_lname']
        }

        self.movie_names = []
        self.genre_names = []
        self.dir_fnames = []
        self.dir_lnames = []
        self.actor_fnames = []
        self.actor_lnames = []
        self.movie_langs = []
        self.movie_years = []
        self.movie_countries = []

    def lvl_1_ques(self):
        tables_list = list(self.tables.keys())
        ques = 'List all values in the table',tables_list[random.randint(0,len(tables_list))]

        tab_name = random.randint(0,len(tables_list))
        cols = random.sample(range(0,len(self.tables[tab_name])),2)
        ques = 'Write an SQL query to get',cols[0],'and',cols[1],'from',tab_name

    def lvl_2_ques(self):
        #movie table specific ques
        ques = 'Find all the movies released in',movie_countries[random.randint(0,len(self.movie_countries))],'.'
        ques = 'Which movies were released in the year',movie_years[random.randint(0,len(self.movie_years))],'?'

        #actor table specific ques
        gender = ['Male','Female']
        alpha = []
        ques = 'Select all',random.choice(gender),'actors whose first name starts with',random.choice(alpha),'.'
