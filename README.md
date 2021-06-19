# MatchJobSystem
This project is a system to match job with academic staff by using past achievements or proven experiences. A pretrained Word2vec model is used to find the matching rate between the job and the academic staff.

 ## What can this project do
1. Searching job by input term (e.g.: java)
2. Job list related with the inputted term will be listed out.
3. Show the job description by clicking the "🔽" button.
4. Sort job list by ascending or descending.
5. Match the job by clicking "Match" button.
6. Matching rate list between the selected job and acedemic staff will be listed out.
7. Sort matching rate list by matching rate.
8. Change the entries that will show the list in one page.
9. Search academic staff by inputting the name.
10. Redirect to the selected job by clicking the job name.
11. Redirect to the scopuslink of selected academic staff by clicking the academic staff name.

## Technical Details
The demo site of this project is https://match-job-system.herokuapp.com/
If you want to build your own match job system, you are welcome to fork this project.

1. Clone this repository.
2. Change this ![image](https://user-images.githubusercontent.com/48663954/122637973-f63a2b80-d123-11eb-88cf-48b56d5e22b6.png) to our own mysql database.
3. Download https://docs.google.com/spreadsheets/d/1xPHmTxZAmj1cpAIbKlB7CjvQPHMaGnVCNebIG_8eqc0/edit?usp=sharingand import into your table in database. The table should be name as job and the column should be:![image](https://user-images.githubusercontent.com/48663954/122637323-98581480-d120-11eb-8903-638aa21a6612.png)
4. Download https://docs.google.com/spreadsheets/d/1iPhLiDV1NjblwIHe1wueD3mGs6Q6Lqq9S4f_9jgMVEs/edit?usp=sharing import into your table in database. The table should be name as user and the column should be: ![image](https://user-images.githubusercontent.com/48663954/122637359-c2113b80-d120-11eb-8f4e-9336935f94d0.png)
5. Create a table in database and the table name should be result. The table column should be: ![image](https://user-images.githubusercontent.com/48663954/122637398-f84ebb00-d120-11eb-98de-de9af9981c24.png)


