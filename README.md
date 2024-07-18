# cheap-flights-finder

This program takes a google sheet that has the follwing cities and loweest price columns and then does the follwing 

<img width="224" alt="Screenshot 2024-07-18 105700" src="https://github.com/user-attachments/assets/34dea483-826f-480f-ab55-cc4e79ecabe7">


1- populate the IATA code for each city 

  <img width="234" alt="Screenshot 2024-07-18 105633" src="https://github.com/user-attachments/assets/52a19cf2-6d13-4f37-9b19-3c755fce2f36">
  
2- using those IATA codes, it tries to find flight prices from LAX to those cities codes that are lower than the lowest price column in the google sheet.

3- it searches fist for direct flights if it finds one. if it doesnt then it saeeches for multistops flights.

4- then it populates emails from another google sheet that has all the emails of the "signed in" users.

5- it sends the results to those users as an SMS, WHatsApp and email .

