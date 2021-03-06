INSERT OR IGNORE INTO `Student` (`name`) VALUES ("Geoffrey Weiss"),("Sybil Burt"),("Wynne Tyler"),("Hoyt Weiss"),("Ian Guerra"),("Adam Manning"),("Allegra Shaffer"),("Sylvester Hall"),("Silas Bates"),("Ina Sims");
INSERT OR IGNORE INTO `Student` (`name`) VALUES ("Mason Burris"),("Kyle Vinson"),("Warren Humphrey"),("Jena Lynn"),("Brady Morris"),("Xanthus Washington"),("Andrew Carney"),("Sonya Kennedy"),("Hope Robbins"),("Leslie Harmon");
INSERT OR IGNORE INTO `Student` (`name`) VALUES ("Isaac Wade"),("Heidi Pacheco"),("Aladdin Whitaker"),("Hall Herrera"),("Jonas Weiss"),("Shoshana Ashley"),("Rahim Jackson"),("Beck Whitney"),("Addison Kerr"),("Jasmine Hebert");
INSERT OR IGNORE INTO `Student` (`name`) VALUES ("Dominic Parks"),("Bryar Dean"),("Hammett Shaw"),("Samantha Wyatt"),("Lila Flowers"),("Amelia Lang"),("Hyatt Mccall"),("Erasmus Alston"),("Tasha Jackson"),("Mary Best");
INSERT OR IGNORE INTO `Student` (`name`) VALUES ("Callum Todd"),("Xaviera Solomon"),("Allistair Shepard"),("Nasim Fowler"),("Keegan Nguyen"),("Graham Roach"),("Jameson Kerr"),("Ezekiel Hamilton"),("Hilel Odonnell"),("Stone Beach");
INSERT OR IGNORE INTO `Student` (`name`) VALUES ("Orson Trevino"),("Mark Stark"),("Mari Jackson"),("Blythe Avery"),("Brendan Mayer"),("Dexter Beard"),("Macy Fox"),("Melvin Padilla"),("Arthur Warner"),("Tiger Fox");
INSERT OR IGNORE INTO `Student` (`name`) VALUES ("Justine Boyle"),("Galena Perkins"),("Sebastian Gay"),("Cody Ortega"),("Ciaran Fletcher"),("Jesse Clarke"),("Cathleen Miller"),("Macaulay Burke"),("Camden Lester"),("Ulla Talley");
INSERT OR IGNORE INTO `Student` (`name`) VALUES ("Doris Dillon"),("Justina Mooney"),("Blossom Reyes"),("Teagan Melendez"),("Amos Stevens"),("Alfonso Sanders"),("Ivor Sexton"),("Minerva Wooten"),("Raymond Walters"),("Dante Fields");
INSERT OR IGNORE INTO `Student` (`name`) VALUES ("Quail Blevins"),("Quinlan Murray"),("Imogene Webster"),("Ila Rice"),("Lee Rivera"),("Giselle Fischer"),("Rowan Dodson"),("Eden Miranda"),("Drew Sharpe"),("Owen Molina");
INSERT OR IGNORE INTO `Student` (`name`) VALUES ("Rhonda Mason"),("Sean Romero"),("Rajah Burch"),("Leroy Cross"),("Ulric Hopkins"),("Bernard Ewing"),("Regan Sexton"),("Keaton Witt"),("Rosalyn Peck"),("Hu Jennings");


INSERT OR IGNORE INTO Course (title, credits, description) VALUES ("COMP 7481", 3, "Selected Topics"), ("COMP 8082", 3, "Project Management"), ("COMP 8006", 3, "Network Security Administration"), ("COMP 8005", 3, "Network Applications Development"), ("LIBS 7002", 3, "Applied Ethics");

INSERT OR IGNORE INTO Teacher (name) VALUES ("Vielka Marshall"),("Jessica Alvarez"),("Kibo Bowen"),("Hyatt Mullen"),("Kylynn Wallace"),("Karly Craft"),("Lynn Dejesus"),("John Marks"),("Robert Hobbs"),("Zelenia Gardner");
INSERT OR IGNORE INTO Teacher (name) VALUES ("Callum Sherman"),("George Campbell"),("Velma Flores"),("Mara Shields"),("Portia Dickerson"),("Quin Page"),("Derek Johns"),("Carl Foreman"),("Callum Fitzpatrick"),("Noble Carlson");
INSERT OR IGNORE INTO Teacher (name) VALUES ("Thaddeus Mckee"),("Cathleen Dejesus"),("Cameron Savage"),("Leigh Romero"),("Francesca Waters"),("Todd Orr"),("Noble Parsons"),("Keefe Abbott"),("Nora Watson"),("Suki Delacruz");
INSERT OR IGNORE INTO Teacher (name) VALUES ("Xyla Cotton"),("Aimee Munoz"),("Addison Macias"),("Wing Johns"),("Amery Perry"),("Chadwick Dominguez"),("Dalton Mooney"),("Briar Cross"),("Allen Spence"),("Harrison Hood");
INSERT OR IGNORE INTO Teacher (name) VALUES ("Fritz Hughes"),("Vincent Pena"),("Lydia Harris"),("Tad Wood"),("Uriah Burris"),("Faith Craig"),("Deirdre Burgess"),("Phillip Flores"),("Xyla Shepard"),("Cora Rivers");
INSERT OR IGNORE INTO Teacher (name) VALUES ("Brian Ayala"),("Davis Mcintosh"),("Vivien Harding"),("Burke Robles"),("Brenden Cotton"),("Felix Trevino"),("Josephine Espinoza"),("Hasad Alexander"),("Aurora Stuart"),("Reese Hays");
INSERT OR IGNORE INTO Teacher (name) VALUES ("Brandon French"),("Kevin Gray"),("Mason Sharpe"),("Dana Schroeder"),("Whitney Santana"),("Leilani Lynch"),("Kyra Ramsey"),("Henry Schneider"),("Hasad Patrick"),("Quinlan Tran");
INSERT OR IGNORE INTO Teacher (name) VALUES ("Duncan Dickerson"),("Merrill Franklin"),("Lila Gamble"),("Macaulay Bean"),("Mason Moore"),("Madonna Knapp"),("David Castaneda"),("Hammett Cline"),("Lucius Mullins"),("Lyle Cross");
INSERT OR IGNORE INTO Teacher (name) VALUES ("Venus Pollard"),("Keiko Prince"),("Libby Giles"),("Haley Hicks"),("Ashton Gentry"),("Sylvester Wright"),("Chester Moran"),("Hayes Frye"),("Griffith Valdez"),("Eric Hines");
INSERT OR IGNORE INTO Teacher (name) VALUES ("Leila Buchanan"),("Joshua Orr"),("Keane Perry"),("April Burch"),("Hu Tate"),("Jakeem Mathews"),("Zenaida Bryan"),("Blair Norman"),("Rae Rodgers"),("Ignacia Hebert");

INSERT OR IGNORE INTO User (username, password) VALUES ("Will", "pbkdf2:sha256:150000$RoIeTP8e$2084f2c7cae604c4bfae1d66f4234e5291ecdb9e983cbeed37926816eebe1b53");

INSERT OR IGNORE INTO Section (course_id, teacher_id) VALUES (1,1),(2,2),(3,3),(4,4),(5,5);

INSERT OR IGNORE INTO Enrolment (student_id, section_id, grade) VALUES (1, 1, (SELECT abs(random() % 100)));
INSERT OR IGNORE INTO Enrolment (student_id, section_id, grade) VALUES (1, 2, (SELECT abs(random() % 100)));
INSERT OR IGNORE INTO Enrolment (student_id, section_id, grade) VALUES (1, 3, (SELECT abs(random() % 100)));
