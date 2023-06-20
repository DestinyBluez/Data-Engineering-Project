--- SQL queries for the reports ---
-- Report 1: Right mode to contact the customers
SELECT * FROM contacts WHERE contacted = 1;
-- Report 2: Count of customers by profession, income, age, education
SELECT profession, income, age, education, COUNT(*) AS count FROM customers GROUP BY profession, income, age, education;
-- Report 3: Possibility of existing loans, credit history, etc.
SELECT loan, credit_history, COUNT(*) AS count FROM customers GROUP BY loan, credit_history;
-- Report 4: Possibility of customers contacted earlier who subscribed to term deposits
SELECT contacted_earlier, subscribed, COUNT(*) AS count FROM customers GROUP BY contacted_earlier, subscribed;
-- Report 5: Existing customers with no term deposits
SELECT * FROM customers WHERE subscribed = 0;
