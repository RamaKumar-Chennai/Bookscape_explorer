import streamlit as st
import pandas as pd
from fetch_books import fetch_books
from insert_books import create_connection, insert_book_data

from select_books import select_book_data1

from select_books import select_book_data2
from select_books import select_book_data3


from select_books import select_book_data4
from select_books import select_book_data5
from select_books import select_book_data6
from select_books import select_book_data7
from select_books import select_book_data8

from select_books import select_book_data9

from select_books import select_book_data10
from select_books import select_book_data11
from select_books import select_book_data12
from select_books import select_book_data13

from select_books import select_book_data14

from select_books import select_book_data15

from select_books import select_book_data16
from select_books import select_book_data17

from select_books import select_book_data18

from select_books import select_book_data19
from select_books import select_book_data20



def main():
    #Set the title of the streamlit dashboard
    st.title("Google Books Data Fetcher")
   
   #Text  box to enter the search term
    search_query = st.text_input("Enter a search term (e.g., 'Python programming'):")
   #Check if the Fetch and Save Data button is clicked
    if st.button("Fetch and Save Data"):
      if not search_query:
            st.error("Please enter a search term.")
            return

      st.info(f"Fetching data for: {search_query}")

        #Call the fetch_books function to fetch the data from Google Books API
      for i in range(0,10):
        print("No.of iterations:",i)
        books = fetch_books(search_query)
        print("The length of books list is ",len(books))

        if not books:
            st.warning("No books found for this search term.")
            return
        #Create the database connection object
        connection = create_connection()

        if connection:
            for item in books:
                print("length of item is-for item in books",len(item))
                print(" the keys in item dictionary are",item.keys())
                volume_info = item.get("volumeInfo", {})
                print(" the keys in volume_info dictionary are",volume_info.keys())
                sale_info = item.get("saleInfo", {})
                print(" the keys in sale_info dictionary are",sale_info.keys())

                book_data = (
                    item.get("id"),
                    search_query,
                    volume_info.get("title"),
                    volume_info.get("subtitle"),
                    ", ".join(volume_info.get("authors", [])),
                    volume_info.get("description"),
                    str(volume_info.get("industryIdentifiers")),
                    volume_info.get("readingModes", {}).get("text", False),
                    volume_info.get("readingModes", {}).get("image", False),
                    volume_info.get("pageCount"),
                    ", ".join(volume_info.get("categories", [])),
                    volume_info.get("language"),
                    volume_info.get("imageLinks", {}).get("thumbnail"),
                    volume_info.get("ratingsCount"),
                    volume_info.get("averageRating"),
                    sale_info.get("country"),
                    sale_info.get("saleability"),
                    sale_info.get("isEbook"),
                    sale_info.get("listPrice", {}).get("amount"),
                    sale_info.get("listPrice", {}).get("currencyCode"),
                    sale_info.get("retailPrice", {}).get("amount"),
                    sale_info.get("retailPrice", {}).get("currencyCode"),
                    sale_info.get("buyLink"),
                    volume_info.get("publishedDate", "")[:4]
                )
                
                #Call the insert_book_data to insert the book data into MySQL Table
                insert_book_data(connection, book_data)

      connection.close()
      st.success("Data fetched and inserted into MySQL successfully!")
    
    #Initialise the sidebar title
    st.sidebar.title("DATA ANALYSIS")

    
    #Initialise the option list for the select box
    Options=[" ","1.Check Availability of eBooks vs Physical Books","2.Find the Publisher with the Most Books Published","3.Identify the Publisher with the Highest Average Rating",
    "4.Get the Top 5 Most Expensive Books by Retail Price","5.Find Books Published After 2010 with at Least 500 Pages","6.List Books with Discounts Greater than 20%",
    "7.Find the Average Page Count for eBooks vs Physical Books","8.Find the Top 3 Authors with the Most Books","9.List Publishers with More than 10 Books",
    "10.Find the Average Page Count for Each Category","11.Retrieve Books with More than 3 Authors","12.Books with Ratings Count Greater Than the Average",
     "13.Books with the Same Author Published in the Same Year","14.Books with a Specific Keyword in the Title",
     "15.Year with the Highest Average Book Price","16.Count Authors Who Published 3 Consecutive Years",
     "17.Find authors who have published books in the same year but under different publishers. Return the authors, year, and the COUNT of books they published in that year.",
     "18.Find the average amount_retailPrice of eBooks and physical books. Return a single result set with columns for avg_ebook_price and avg_physical_price. Ensure to handle cases where either category may have no entries.",
     "19. Identify books that have an averageRating that is more than two standard deviations away from the average rating of all books. Return the title, averageRating, and ratingsCount for these outliers.",
     "20.Which publisher has the highest average rating among its books, but only for publishers that have published more than 10 books. Return the publisher, average_rating, and the number of books published."

     ]


    #Initialise the sidebar select box
    choice=st.sidebar.selectbox("SELECT YOUR QUERY HERE",Options)

    #CHECK THE CHOICE AND CALL THE RESPECTIVE SELECT_BOOK_DATA CODE ACCORDINGLY  
    if choice== "1.Check Availability of eBooks vs Physical Books":
      
      connection = create_connection()
      results,df=select_book_data1(connection)   
      st.write("## Availability of eBooks vs Physical Books")
      st.write("E-books count:",results.count(1)) 
      st.write("Physical books count:",results.count(0))        
      connection.close()
      
    
    if choice== "2.Find the Publisher with the Most Books Published":
      
      connection = create_connection()
      results,df=select_book_data2(connection)   
      st.write("## The Publisher with the Most Books Published")
      st.write(df)
            
      connection.close()
      
    

    if choice== "3.Identify the Publisher with the Highest Average Rating":
      
      connection = create_connection()
      results,df=select_book_data3(connection)   
      st.write("## The Publisher with the Highest Average Rating")
      st.write(df)
            
      connection.close()



       
    elif choice=="4.Get the Top 5 Most Expensive Books by Retail Price":
        connection = create_connection()
        results,df=select_book_data4(connection) 
        st.write("## Top 5 Most Expensive Books by Retail Price")
        st.write(df)
        connection.close()

    
    elif choice=="5.Find Books Published After 2010 with at Least 500 Pages":
        connection = create_connection()
        results,df=select_book_data5(connection) 
        st.write("##  Books Published After 2010 with at Least 500 Pages")
        st.write(df)
        connection.close()

   
    elif choice=="6.List Books with Discounts Greater than 20%":
        connection = create_connection()
        results,df=select_book_data6(connection) 
        st.write("##  Books with Discounts Greater than 20%")
        st.write(df)
        connection.close()

    elif choice=="7.Find the Average Page Count for eBooks vs Physical Books":
        connection = create_connection()
        results1,df1=select_book_data7(connection) 
        st.write("##  Average Page Count for eBooks vs Physical Books")
        st.write(df1)
        connection.close()
        
    elif choice=="8.Find the Top 3 Authors with the Most Books":
        connection = create_connection()
        results1,df1=select_book_data8(connection) 
        st.write("##  Top 3 Authors with the Most Books")
        st.write(df1)
        connection.close()

    

    elif choice=="9.List Publishers with More than 10 Books":
        connection = create_connection()
        results1,df1=select_book_data9(connection) 
        st.write("##  Publishers with More than 10 Books")
        st.write(df1)
        connection.close()
    
    elif choice=="10.Find the Average Page Count for Each Category":
        connection = create_connection()
        results1,df1=select_book_data10(connection) 
        st.write("##  Average Page Count for Each Category")
        st.write(df1)
        connection.close()

        

    elif choice=="11.Retrieve Books with More than 3 Authors":
        connection = create_connection()
        results1,df1=select_book_data11(connection) 
        st.write("##  Books with More than 3 Authors")
        st.write(df1)
        connection.close()
        
        


    elif choice=="12.Books with Ratings Count Greater Than the Average":
        connection = create_connection()
        results1,df1=select_book_data12(connection) 
        st.write("##  Books with Ratings Count Greater Than the Average")
        st.write(df1)
        connection.close()


    
    elif choice=="13.Books with the Same Author Published in the Same Year":
        connection = create_connection()
        results1,df1=select_book_data13(connection) 
        st.write("##  Books with the Same Author Published in the Same Year")
        st.write(df1)
        connection.close()


    elif choice=="14.Books with a Specific Keyword in the Title":
        connection = create_connection()
        results1,df1,row_number=select_book_data14(connection) 
        st.write("##   Books with a Specific Keyword in the Title ")
        st.write(df1)
        st.write("The number of rows in this condition is",row_number)

        connection.close()





    elif choice=="15.Year with the Highest Average Book Price":
        connection = create_connection()
        results1,df1=select_book_data15(connection) 
        st.write("##  Year with the Highest Average Book Price")
        st.write(df1)
        connection.close()

    elif choice=="16.Count Authors Who Published 3 Consecutive Years":
        connection = create_connection()
        results1,df1=select_book_data16(connection) 
        st.write("##  Authors Who Published 3 Consecutive Years")
        st.write(df1)
        connection.close()
    
    
    
    elif choice=="17.Find authors who have published books in the same year but under different publishers. Return the authors, year, and the COUNT of books they published in that year.":
        connection = create_connection()
        results1,df1=select_book_data17(connection) 
        st.write("##  The authors who have published books in the same year but under different publishers")
        st.write(df1)
        connection.close()
    





    elif choice=="18.Find the average amount_retailPrice of eBooks and physical books. Return a single result set with columns for avg_ebook_price and avg_physical_price. Ensure to handle cases where either category may have no entries.":
        connection = create_connection()
        results1,df1=select_book_data18(connection) 
        st.write("##   Average amount_retailPrice of eBooks and physical books")
        st.write(df1)
        connection.close()


    elif choice=="19. Identify books that have an averageRating that is more than two standard deviations away from the average rating of all books. Return the title, averageRating, and ratingsCount for these outliers.":
        connection = create_connection()
        results1,df1=select_book_data19(connection) 
        st.write("##   Books that have an averageRating that is more than two standard deviations away from the average rating of all books")
        st.write(df1)
        connection.close()

    elif choice=="20.Which publisher has the highest average rating among its books, but only for publishers that have published more than 10 books. Return the publisher, average_rating, and the number of books published.":
        connection = create_connection()
        results1,df1=select_book_data20(connection) 
        st.write("##  Publisher with the highest average rating among its books, but only for publishers that have published more than 10 books")
        st.write(df1)
        connection.close()

if __name__ == "__main__":
    main()
