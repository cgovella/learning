INSERT INTO Employee (Name, HireDate, Grade, ManagerID)
       VALUES ('John Brown','20030623','Foreman', NULL);
INSERT INTO Employee (Name, HireDate, Grade, ManagerID)
       VALUES ('Fred Smith','20040302','Labourer',NULL);
INSERT INTO Employee (Name, HireDate, Grade, ManagerID)
       VALUES ('Anne Jones','19991125','Labourer',NULL);

UPDATE Employee
SET ManagerID = (SELECT EmpID 
                 From Employee 
                 WHERE Name = 'John Brown')
WHERE Name IN ('Fred Smith', 'Anne Jones');

INSERT INTO Salary (Grade, Amount)
       VALUES('Foreman','60000');
INSERT INTO Salary (Grade, Amount)
       VALUES('Labourer','35000');

