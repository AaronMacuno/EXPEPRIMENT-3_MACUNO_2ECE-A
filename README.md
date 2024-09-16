# EXPEPRIMENT-3_MACUNO_2ECE-A
## **I. Intended Learning Outcome:**

  **1.** To identify the codes and functions incorporated in the Pandas library

  **2.** To be able to apply and use the different codes and functions in creating a Python program using a
     Pandas library
  
## **II. Instructions:**

Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter
notebook in the dedicated submission bin.

## **III. Solution**
  Use panda for data manipulation all throughout the program.
    
    import panda as pd

  ### **_PROBLEM 1_**
  
   **a.** Load the recently downloaded .csv file in the dataframe with the variable name 'cars' using pandas
   
 ![image](https://github.com/user-attachments/assets/0cc92454-cb20-49fa-90b8-6074fb37e18e)
 
   **b.** To display the first five and last five rows of the data base, the .head() & .tail() are utilized

.head() - displays the first five rows
 ![image](https://github.com/user-attachments/assets/9ee9bb20-96b4-4d93-9aa2-c3f54ae0796a)

 .tail() - display the last five rows
 ![image](https://github.com/user-attachments/assets/d569fdb7-23ad-4aba-9884-492d2b15220d)

  ### **_PROBLEM 2_**

 **a.** Loading and using cars to dispay cars.iloc to only display Odd Numbers due to slicing.
	
**EXPLANATION:**

		.iloc[:5] - used for slicing and selects rows from the start, but not including 5.

		::2 - a slicing notation that chosses every second coloumn, and the : before :2 selects all the coloumns from the start to the end but with two intervals
 ![image](https://github.com/user-attachments/assets/40d23b4d-eb5d-42f6-9efe-83bfc51c73ae)
 
**b.** The row of Mazda RX4 is accessible due to the variable 'mazda' being used to store the row

**EXPLANATION:**

		mazda = cars[cars['Model'] == 'Mazda RX4'] - This boolean indexing filters those rows inside the variable cars where the Model coloumn matches 'Mazda RX4.' Those rows with Mazda RX4 are stored inside the variable 'mazda'

![image](https://github.com/user-attachments/assets/c69381ca-8cb9-4a41-a000-92ff7deeecdd)

**c.** The number of cylinder in the car Camaro z28 is now accessible due to the varibalbe 'camaro'

**EXPLANATION:**

		cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']] - Filters the cars dataframe to only include those rows with Camaro z28, and then proceed to only show the Model and cyl.
		
![image](https://github.com/user-attachments/assets/ba3e4f65-bc42-4965-af06-08302ae7ec83)

**d.** The variable 'both' was used to store the data containing the cylinders and gears of the given cars

**EXPLANATION:**

			a list was created with the name of three cars inside 'both'
			
			cars[cars['Model'].isin(both)] - then used to check rows inside the dataframe which 'Models' have the same three names in 'both'
			[['Model', 'cyl', 'gear']] - After filtering the dataframe, it only prints those under model, cyl, and gear.
			
![image](https://github.com/user-attachments/assets/3635ca8b-5397-405c-b9ae-a4e098c3a7f3)


## VERSIONS

**1.2** - Completion of the README file

**1.1** - The files are uploaded in the repository

**1.0** - The whole programming assignment was started
