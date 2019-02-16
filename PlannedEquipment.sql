-- CREATE DATABASE oprema

CREATE TABLE PlannedEquipment (
     Num            INT PRIMARY KEY
    ,ProductNumber  INT 
    ,Naziv          VARCHAR(255)
    ,Kolicina       INT DEFAULT 1
);

-- umjesto INT, za Num je bilo moguce koristiti SERIAL, no tad bi iz xlsx ucitali samo tri stupca