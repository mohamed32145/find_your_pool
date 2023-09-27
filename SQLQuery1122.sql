use pools

CREATE TABLE Manager (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(255),
    Age INT,
    Salary DECIMAL(10, 2)
);

CREATE TABLE Pools (
    CODE INT PRIMARY KEY IDENTITY(1,1),
    PoolName NVARCHAR(255),
	depth int,
	width int,
	lenght int

);

CREATE TABLE ManagerPools (
    ManagerID INT,
    PoolID INT,
    PRIMARY KEY (ManagerID, PoolID),
    FOREIGN KEY (ManagerID) REFERENCES Manager(ID),
    FOREIGN KEY (PoolID) REFERENCES Pools(CODE)
);


create table Bracelet(
    CODE INT PRIMARY KEY IDENTITY(1,1),
	customer_name nvarchar(100),
	age int
);


create table braceletpools (
  poolcode int,
  braccode int,
  primary key  (poolcode, braccode),
  foreign key (poolcode) REFERENCES Pools(CODE),
  foreign key (braccode) REFERENCES Bracelet(CODE)

)