#LOADING_REQUIRED_DATA


import pandas as pd


#loading_users

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users=pd.read_csv(r'movie_lens_dataset\u.user',sep='|', names=user_cols, encoding="ISO-8859-1")



#loading_ratings

rating_cols=['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings=pd.read_csv(r'movie_lens_dataset\u.data',sep='\t', names=rating_cols, encoding="ISO-8859-1")



#loading_genres

items_cols=['movie_id', 'movie_title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items=pd.read_csv(r'movie_lens_dataset\u.item',sep='|', names=items_cols,encoding="ISO-8859-1" )



#merging users and ratings on user_id

movies_users_ratings = pd.merge(users, ratings, on='user_id')



#merging movies_users_ratings and items on movie_id

final_merged=pd.merge(movies_users_ratings,items,on='movie_id')


