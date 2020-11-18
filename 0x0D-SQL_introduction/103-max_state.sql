-- max temperature of each state (
SELECT state, MAX(value) AS mas_temp FROM temperatures GROUP BY state ORDER by state;
