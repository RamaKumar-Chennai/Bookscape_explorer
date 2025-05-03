def res_fn(connection,query):
     #This function is to fetch the results from the query
     import pandas as pd
     cursor=connection.cursor()
     # Execute a SELECT statement

     cursor.execute(query)
     # Fetch all results from the executed query
     results=cursor.fetchall()
     
     #COPY THE RESULTS TO A DATAFRAME

     df=pd.DataFrame(results,columns=[i[0] for i in cursor.description])        
     cursor.close()
     return results,df


def select_book_data1(connection):
     
       
     import pandas as pd
     cursor = connection.cursor()
     # Execute a SELECT statement
     
     query = "SELECT isEbook FROM books"
     
      
     cursor.execute(query)

     # Fetch all results from the executed query
     results = cursor.fetchall()
     
     print("data type of results is ",type(results))
     print("The elements in resulsts are",results[0],results[1])
     res_lst=[]
     for i in range(0,len(results)):
         res_lst.append(results[i][0])
     print("the res list is",res_lst)
     df = pd.DataFrame(res_lst, columns=[desc[0] for desc in cursor.description])
     cursor.close()  
     
    
     return res_lst,df
     
def select_book_data2(connection):
     #Initialise the query
     query="select count(book_id),industryIdentifiers from bookscape.books group by industryIdentifiers having industryIdentifiers != 'None' order by count(book_id) desc limit 1"
     
     #Call the res_fn to fetch the results
     results,df=res_fn(connection,query)
     
     return results,df

def select_book_data3(connection):
     #Initialise the query
     query="select industryIdentifiers,avg(averageRating) from bookscape.books group by industryIdentifiers having industryIdentifiers != 'None' order by avg(averageRating) desc limit 1"

     #Call the res_fn to fetch the results
     results,df=res_fn(connection,query)
     
     return results,df



def select_book_data4(connection):
     #Initialise the query
     query="select book_title,book_subtitle,book_authors,amount_retailPrice from bookscape.books order by amount_retailPrice desc limit 5"
     
     #Call the res_fn to fetch the results
     results,df=res_fn(connection,query)
     
     return results,df

def select_book_data5(connection):
     #Initialise the query

     query="select book_id,book_title,book_subtitle,book_authors,year,pageCount from bookscape.books where year>=2010 and pageCount>=500"
     
     #Call the res_fn to fetch the results
     results,df=res_fn(connection,query)
     df = df.drop_duplicates(keep='last')
     return results,df

def select_book_data6(connection):
     #Initialise the query
     query="select book_id,book_title,((amount_listPrice-amount_retailPrice)*100)/amount_listPrice  from bookscape.books where   ((amount_listPrice-amount_retailPrice)*100)/amount_listPrice >=20 "
     
     #Call the res_fn to fetch the results
     results,df=res_fn(connection,query)
     df.columns=['Book_id','Book_title','Discount']
     df = df.drop_duplicates(keep='last')
     return results,df


def select_book_data7(connection):
     import pandas as pd

     #Initialise the query
     
     query="select avg(pageCount),isEbook from bookscape.books group by isEbook"
     
     #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     df1.columns=["Avg_page_count","isEbook"]
     print(df1)
     df1.insert(2,column="Book_status",value=" ") 
     df1.loc[df1["isEbook"]==0,["Book_status"]]="Physical book"
     df1.loc[df1["isEbook"]==1,["Book_status"]]="E-book"
     
     return results1,df1


def select_book_data8(connection):
      #Initialise the query
     query="select count(book_authors),book_authors from bookscape.books group by book_authors having book_authors is not null  order by count(book_authors) desc  limit 4 "
     
     #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     print("before droppping null values",df1)
     df1=df1.drop(df1[df1['book_authors'] == ""].index)
     print("after droppping null values")
     print(df1)
     return results1,df1

def select_book_data9(connection):
     import pandas as pd
     
     #Initialise the query
     query="select industryIdentifiers,count(book_id) from bookscape.books group by industryIdentifiers having industryIdentifiers != 'None' and count(book_id)>10"
     
     #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     
     
     return results1,df1


def select_book_data10(connection):
     import pandas as pd

     #Initialise the query
     query="select avg(pageCount),categories from bookscape.books group by categories"
     

     #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     #df1.columns=["Avg_page_count","categories"]
     print("the ave page count  catergoes df is ")
     print(df1)
     
     return results1,df1


def select_book_data11(connection):
     import pandas as pd

     #Initialise the query
     query="select book_id,book_title,book_subtitle,book_authors from bookscape.books where book_authors like '%,%,%,%' "
     
     #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     
     df1 = df1.drop_duplicates(keep='last')
     print(df1)
     
     return results1,df1


def select_book_data12(connection):
     import pandas as pd

      #Initialise the query

     query="select book_id,book_title,book_subtitle,book_authors,ratingsCount,averageRating from bookscape.books where ratingsCount > averageRating"
     

     #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
         
     print(df1)
     
     return results1,df1

def select_book_data13(connection):
     import pandas as pd

     #Initialise the query
     query="select count(book_authors),book_title,book_authors,year from bookscape.books group by book_authors,year,book_title having count(book_authors) > 1 and year is  not null"
     
     #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     
    
     print(df1)
     
     return results1,df1

def select_book_data14(connection):
     import pandas as pd
     print("inside 14th question")

     #Initialise the query
     query=" select  book_title from bookscape.books order by book_authors desc limit 2"
     
      #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     print("the tuple results is ",results1)
     print("the datat tpe of tuple results is ",type(results1))
     full_df=pd.DataFrame()
     for i in range(0,len(results1)):
      temp_str=str(results1[i])


      print("the temp str  is \n",temp_str)
      import re
      temp_str=re.sub(r"[(,)]","",temp_str)
      print("the temp str after re.sub  is \n",temp_str)
      print("the data type of temp_str is",type(temp_str))
      temp_lst=temp_str.split()
      print("the temp list is ",temp_lst)


      for j in range(0,len(temp_lst)):
             if j==0 or j==len(temp_lst)-1:
                 temp_lst[j]=re.sub(r"'","",temp_lst[j])
             q_str=temp_lst[j]
             print("each string is ",q_str)
             query="select * from bookscape.books where book_title like " + "'%" + q_str + "%'"
             results,df=res_fn(connection,query)
             #print("the final results list  in each iteration is\n",results)
             print("the  df in each iteration is \n",df)
             
             if not df.empty:
                 full_df=pd.concat([full_df,df])


     df_no_duplicates = full_df.drop_duplicates(keep='last')
     print(df_no_duplicates)
     print("the number of rows in the final dataframe is ",df_no_duplicates.shape[0])
     
     return results1,df_no_duplicates,df_no_duplicates.shape[0]



def select_book_data15(connection):
     import pandas as pd

     #Initialise the query
     query="select avg(amount_retailPrice),year from bookscape.books group by year order by avg(amount_retailPrice) desc limit 1 "
     
     #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     
    
     print(df1)
     
     return results1,df1


def select_book_data16(connection):
     import pandas as pd
      #Initialise the query
     query='''SELECT DISTINCT b1.book_authors FROM bookscape.books b1
              JOIN bookscape.books b2 ON b1.book_authors = b2.book_authors AND b2.year = b1.year + 1
              JOIN bookscape.books b3 ON b1.book_authors = b3.book_authors AND b3.year = b1.year + 2
              WHERE b1.book_authors IS NOT NULL'''
     
     #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     
    
     print(df1)
     
     return results1,df1








def select_book_data17(connection):
     import pandas as pd
      #Initialise the query
     query="select book_authors,count(book_authors),year from bookscape.temp group by book_authors,year order by year"
     
      #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     
    
     print(df1)
     
     return results1,df1

def select_book_data18(connection):
     import pandas as pd

     #Initialise the query
     query="select avg(amount_retailPrice),isEbook from bookscape.books group by isEbook"
     
      #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     
    
     print(df1)

     df1.columns=["Avg_retail_price","isEbook"]
     print(df1)
     df1.insert(2,column="Book_status",value=" ") 
     df1.insert(3,column="Retail_price_status",value=" ") 
     df1.loc[df1["isEbook"]==0,["Book_status"]]="Physical book"
     df1.loc[df1["isEbook"]==1,["Book_status"]]="E-book"
     df1.loc[df1["isEbook"]==0,["Retail_price_status"]]="Retail price not available for Physical books except for 5 books"
     df1.loc[df1["isEbook"]==1,["Retail_price_status"]]="Average retail price for Ebooks has been mentioned in the Table here"
    
     return results1,df1


def select_book_data19(connection):
     import pandas as pd

     #Initialise the query
     query="select avg(averageRating) as aver,std(averageRating) as stdd, avg(averageRating)-(2*std(averageRating)) as final_rating from bookscape.books"
     
     #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
         
     print(df1)
     print(df1.columns)
     print(df1['final_rating'])
     lst=df1['final_rating'].tolist()

     query="select * from bookscape.books"
     results2,df2=res_fn(connection,query)
     print(df2)
     
     df2.insert(24,'Final_rating',None)
     df2['Final_rating']=df1['final_rating']
     print(df2)
     df2['Final_rating']= df2['Final_rating'].fillna( df2['Final_rating'].mean())
     print(df2)
     print(df2.columns)

     #print(df2.loc[df2['averageRating']>df2['Final_rating'],:])
     df3=df2.loc[df2['averageRating']>df2['Final_rating'],['book_id','averageRating','ratingsCount']]
     print("final df3 is ")
     print(df3)
     df3=df3.drop_duplicates(keep='last')
     return results1,df3


def select_book_data20(connection):
     import pandas as pd

     #Initialise the query
     query="select count(book_id),industryIdentifiers,max(averageRating) from bookscape.books group by industryIdentifiers having  count(book_id) >10"
     
     #Call the res_fn to fetch the results
     results1,df1=res_fn(connection,query)
     
    
     print(df1)
     
          
     
     return results1,df1


