//Problem 1
//Create JSON for each employee with the following details (first name, department, designation, salary, raise eligible)
// Sam, Tech, Manager, 40000, true
// Mary, Finance, Trainee, 18500, true
// Bill, HR, Executive, 21200, false

let text = '{ "employees" : [' +
'{ "firstName":"Sam" , "department":"Tech", "designation":"Manager", "salary":"40000", "raise eligible":"true"},' +
'{ "firstName":"Mary" , "department":"Finance", "designation":"Trainee", "salary":"18500", "raise eligible":"true"},' +
'{ "firstName":"Bill" , "department":"HR", "designation":"Executive", "salary":"21200", "raise eligible":"false"} ]}';

//console log the JSON
const obj = JSON.parse(text);
console.log("Problem 1");
console.log(text);
console.log(obj);

//Problem 2
// Create JSON for the company with the following details (companyName, website, employees)
// Tech Stars, www.techstars.site, array of Employees

let text2 = '{ "company" : [' +
'{ "companyName":"Tech Stars" , "website":"www.techstars.site", "employees":[' +
'{ "firstName":"Sam" , "department":"Tech", "designation":"Manager", "salary":"40000", "raise eligible":"true"},' +
'{ "firstName":"Mary" , "department":"Finance", "designation":"Trainee", "salary":"18500", "raise eligible":"true"},' +
'{ "firstName":"Bill" , "department":"HR", "designation":"Executive", "salary":"21200", "raise eligible":"false"} ]}]}';

//console log the JSON
const obj2 = JSON.parse(text2);
console.log("Problem 2");
console.log(text2);
console.log(obj2);

//Problem 3
// A new employee has joined the company. Update the JSON from problems 1 and 2 to reflect the addition of:
// Anna, Tech, Executive, 25600, false

let employeeLength = obj["employees"].length;
obj["employees"][employeeLength] = { "firstName":"Anna" , "department":"Tech", "designation":"Executive", "salary":"25600", "raise eligible":"false"};

//console log the JSON
console.log("Problem 3");
console.log(obj);

//Problem 4
// Given the JSON for the company, calculate the total salary for all company employees.

let totalSalary = 0;
for (let i = 0; i < obj["employees"].length; i++) {
    totalSalary += parseInt(obj["employees"][i]["salary"]);
}

//console log the JSON
console.log("Problem 4");
console.log("Total Salary: " + totalSalary);

//Problem 5
// It's raise time. If an employee is raise eligible, increase their salary by 10%. Given the JSON of the company and its employees, write a function to update the salary for each employee who is raised eligible, then set their eligibility to false.

for (let i = 0; i < obj["employees"].length; i++) {
    if (obj["employees"][i]["raise eligible"] == "true") {
        obj["employees"][i]["salary"] = parseInt(obj["employees"][i]["salary"]) * 1.1;
        obj["employees"][i]["raise eligible"] = "false";
    }
}

//console log the JSON
console.log("Problem 5");
console.log(obj);

//Problem 6
// Some employees have decided to work from home. The following array indicates who is working from home. Use the array to update the company JSON. For each employee, add another property called 'wfh' and set it to true of false
// Working from home: ['Anna', 'Sam']

let wfh = ['Anna', 'Sam'];
for (let i = 0; i < obj["employees"].length; i++) {
    if (wfh.includes(obj["employees"][i]["firstName"])) {
        obj["employees"][i]["wfh"] = "true";
    } else {
        obj["employees"][i]["wfh"] = "false";
    }
}

//console log the JSON
console.log("Problem 6");
console.log(obj);

//end of code