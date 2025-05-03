
The BookScape Explorer project aims to facilitate users in discovering and analyzing book data through a web application. The application will extract data from online book APIs, store this information in a SQL database, and enable data analysis using SQL queries. The project will provide insights into book trends, user preferences, and reviews, helping users make informed reading choices while also offering a platform for community engagement. This initiative targets avid readers, researchers, and book enthusiasts.

Business Use Cases:
Search Optimization: Filter books based on genre, author, or publication year.
Trend Analysis: Identify trending genres or authors over time.
Data Insights: Perform analysis on user reviews and ratings to identify popular books.
Decision Support: Provide insights for libraries or bookstores to stock trending books.


Approach:
Data Extraction: 
 Google Books API is used to gather comprehensive data on a variety of books.
Information such as book titles, authors, publication dates, genres, descriptions, user reviews etc is extracted

Data Storage:  SQL database is created with well-designed schema (e.g., defining appropriate data types and primary keys).
Table reference given below,

Column Name
Data Type
Description
book_id
VARCHAR
A unique identifier for each book record.
search_key
VARCHAR
The keyword or term used to search for the book via the API
book_title
VARCHAR
The title of the book.
book_subtitle
TEXT
A secondary or extended title for the book, if available.
book_authors
TEXT
The author(s) of the book. 
book_description
TEXT
A brief summary or overview of the book's content.
industryIdentifiers
TEXT
Identifiers like ISBN (International Standard Book Number) used by the publishing industry. 


text_readingModes
BOOLEAN
Indicates whether the book is available in a readable text format.
image_readingModes
BOOLEAN
Indicates whether the book is available in an image-based reading mode.
pageCount
INT
The total number of pages in the book.
categories
TEXT
The genres or categories the book belongs to. 
language
VARCHAR
The language code of the book
imageLinks
TEXT
URLs or links to the book's cover image or other related images.
ratingsCount
INT
The total number of user ratings the book has received.
averageRating
DECIMAL
The average rating of the book based on user reviews 
country
VARCHAR
The country code where the book is available or published
saleability
VARCHAR
Describes the availability of the book for sale
isEbook
BOOLEAN
Indicates whether the book is available as an eBook
amount_listPrice
DECIMAL
The list price of the book in its native currency 
currencyCode_listPrice
VARCHAR
The currency code for the list price 
amount_retailPrice
DECIMAL
The retail or discounted price of the book.
currencyCode_retailPrice
VARCHAR
The currency code for the retail price.
buyLink
TEXT
A URL to purchase or access the book online.
year
TEXT
The year of publication or release.
publisher
TEXT
The publisher of the book.


Data is inserted systematically and verified for consistency post-load.
Data Analysis:
 SQL queries to answer the following  questions:
Check Availability of eBooks vs Physical Books
Find the Publisher with the Most Books Published
Identify the Publisher with the Highest Average Rating
Get the Top 5 Most Expensive Books by Retail Price
Find Books Published After 2010 with at Least 500 Pages
List Books with Discounts Greater than 20%
Find the Average Page Count for eBooks vs Physical Books
Find the Top 3 Authors with the Most Books
List Publishers with More than 10 Books
Find the Average Page Count for Each Category
Retrieve Books with More than 3 Authors
Books with Ratings Count Greater Than the Average
Books with the Same Author Published in the Same Year
Books with a Specific Keyword in the Title
Year with the Highest Average Book Price
Count Authors Who Published 3 Consecutive Years
Write a SQL query to find authors who have published books in the same year but under different publishers. Return the authors, year, and the COUNT of books they published in that year.
Create a query to find the average amount_retailPrice of eBooks and physical books. Return a single result set with columns for avg_ebook_price and avg_physical_price. Ensure to handle cases where either category may have no entries.
Write a SQL query to identify books that have an averageRating that is more than two standard deviations away from the average rating of all books. Return the title, averageRating, and ratingsCount for these outliers.
Create a SQL query that determines which publisher has the highest average rating among its books, but only for publishers that have published more than 10 books. Return the publisher, average_rating, and the number of books published.


Streamlit Application
A user-friendly interface with input fields is designed(e.g., search boxes or filters).
Streamlit app is connected with the SQL database for real-time query execution.
Analysis results in the form of tables or dashboards within the app is displayed


Results: 
The expected results of the project include a fully functional Streamlit application that enables users to search for and analyze book data extracted from APIs, a well-structured SQL database that stores book information, and a set of SQL queries that facilitate data analysis. Ultimately, learners should achieve hands-on experience in data extraction, SQL database management, and building interactive applications. This project will enhance their skills in data handling and application development while providing insights into the world of literature.

Skills Takeaway:
Data Extraction: API calls or web scraping.
SQL Database Management: Designing tables and schema.
Data Analysis: Writing SQL queries to derive insights.
Project Evaluation metrics:
Data Extraction Accuracy:Successful retrieval of the desired data from APIs or sources without errors or missing values.
SQL Database Design:Proper structuring of tables with normalized data and correct relationships between them.
Query Efficiency:Ability to write optimized SQL queries that retrieve relevant insights quickly.
Streamlit Application Functionality:Smooth navigation and interactive features for data display and analysis.
Project Completeness:End-to-end workflow execution from data extraction to SQL storage and visualization.
Documentation Quality:Clear explanations of each step, insights, and challenges faced in the process.
Presentation and Usability:An intuitive user interface with meaningful outputs and actionable insights.
Error Handling:Ability to manage API rate limits, database constraints, or user input errors effectively.
Innovation and Creativity:Unique implementation ideas, creative visualizations, or insightful SQL queries.


Technical Tags:
Languages: Python
Database: SQL (MySQL/PostgreSQL)
Visualization Tool: Streamlit
API Integration: Google Books API
Libraries: Pandas, Mysql 
Project Deliverables:
SQL Database: Fully populated with book data
API Scripts: For data extraction and transformation
Streamlit Application: User-friendly book exploration tool

