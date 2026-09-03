
const registrationForm = document.getElementById("registrationForm");

let fname = registrationForm.querySelector("#fname");
let lname = registrationForm.querySelector("#lname");
let email = registrationForm.querySelector("#email");
let phone = registrationForm.querySelector("#phone");
let password = registrationForm.querySelector("#password");
let dob = registrationForm.querySelector("#dob");
let country = registrationForm.querySelector("#country");
let city = registrationForm.querySelector("#city");
let skills = registrationForm.querySelector("#skills");


registrationForm.addEventListener("submit", function (e) {

    // Form ko submit/reload hone se rokna
    e.preventDefault();


    // VALUES
    let fnameValue = fname.value.trim();
    let lnameValue = lname.value.trim();
    let emailValue = email.value.trim();
    let phoneValue = phone.value.trim();
    let passwordValue = password.value.trim();
    let dobValue = dob.value;
    let countryValue = country.value.trim();
    let cityValue = city.value.trim();
    let skillsValue = skills.value.trim();


    // Gender ko submit ke time select karenge
    let gender = registrationForm.querySelector(
        "[name='gender']:checked"
    );

    let genderValue = gender?.value;


    // ERROR VARIABLES
    let fnameError = false;
    let lnameError = false;
    let emailError = false;
    let phoneError = false;
    let passwordError = false;
    let dobError = false;
    let genderError = false;
    let countryError = false;
    let cityError = false;
    let skillsError = false;


    // FIRST NAME
    if (!checkfName(fnameValue, fname)) {
        fnameError = true;
    }
    // LAST NAME
    if (!checklName(lnameValue, lname)) {
        lnameError = true;
    }

    // EMAIL
    if (!checkEmail(emailValue, email)) {
        emailError = true;
    }

    // PHONE
    if (!checkPhone(phoneValue, phone)) {
        phoneError = true;
    }

    // PASSWORD
    if (!checkPassword(passwordValue, password)) {
        passwordError = true;
    }

    // DOB
    if (!checkDob(dobValue, dob)) {
        dobError = true;
    }

    // GENDER
    if (!checkGender(gender)) {
        genderError = true;
    }


    // COUNTRY
    if (!checkCountry(countryValue, country)) {
        countryError = true;
    }


    // CITY
    if (!checkCity(cityValue, city)) {
        cityError = true;
    }


    // SKILLS
    if (!checkSkills(skillsValue, skills)) {
        skillsError = true;
    }


    // FINAL CHECK
    if (
        !fnameError &&
        !lnameError &&
        !emailError &&
        !phoneError &&
        !passwordError &&
        !dobError &&
        !genderError &&
        !countryError &&
        !cityError &&
        !skillsError
    ) {

        console.log("No Error found. The form can be submitted now");

       
        console.log({
            firstName: fnameValue,
            lastName: lnameValue,
            email: emailValue,
            phone: phoneValue,
            password: passwordValue,
            dob: dobValue,
            gender: genderValue,
            country: countryValue,
            city: cityValue,
            skills: skillsValue.split(",").map(skill => skill.trim())
        });

    } else {

        console.log("Please fill the form correctly and submit again");

    }

});




function checkfName(fname, el) {

    let pattern = /^[A-Za-z\s]{3,100}$/;

    let passed = pattern.test(fname);

    let errorEl = el
        .closest("form")
        .querySelector(".fname-error");

    if (!passed) {
        errorEl.classList.add("show");
    } else {
        errorEl.classList.remove("show");
    }

    return passed;
}





function checklName(lname, el) {

    let pattern = /^[A-Za-z\s]{2,100}$/;

    let passed = pattern.test(lname);

    let errorEl = el
        .closest("form")
        .querySelector(".lname-error");

    if (!passed) {
        errorEl.classList.add("show");
    } else {
        errorEl.classList.remove("show");
    }

    return passed;
}





function checkEmail(email, el) {

    let pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    let passed = pattern.test(email);

    let errorEl = el
        .closest("form")
        .querySelector(".email-error");

    if (!passed) {
        errorEl.classList.add("show");
    } else {
        errorEl.classList.remove("show");
    }

    return passed;
}




function checkPhone(phone, el) {

    // 10 digits aur 6,7,8,9 se start
    let pattern = /^[6-9]\d{9}$/;

    let passed = pattern.test(phone);

    let errorEl = el
        .closest("form")
        .querySelector(".phone-error");

    if (!passed) {
        errorEl.classList.add("show");
    } else {
        errorEl.classList.remove("show");
    }

    return passed;
}





function checkPassword(password, el) {

    let pattern =
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{6,}$/;

    let passed = pattern.test(password);

    let errorEl = el
        .closest("form")
        .querySelector(".password-error");

    if (!passed) {
        errorEl.classList.add("show");
    } else {
        errorEl.classList.remove("show");
    }

    return passed;
}





function checkDob(dobValue, el) {

    let passed = true;

    if (dobValue === "") {

        passed = false;

    } else {

        let selectedDob = new Date(dobValue);
        let today = new Date();

        // Future date allow nahi
        if (selectedDob > today) {
            passed = false;
        }

    }

    let errorEl = el
        .closest("form")
        .querySelector(".dob-error");

    if (!passed) {
        errorEl.classList.add("show");
    } else {
        errorEl.classList.remove("show");
    }

    return passed;
}





function checkGender(gender) {

    let errorEl = registrationForm.querySelector(".gender-error");

    if (!gender) {

        errorEl.classList.add("show");

        return false;

    } else {

        errorEl.classList.remove("show");

        return true;
    }

}





function checkCountry(countryValue, el) {

    let passed = countryValue !== "";

    let errorEl = el
        .closest("form")
        .querySelector(".country-error");

    if (!passed) {
        errorEl.classList.add("show");
    } else {
        errorEl.classList.remove("show");
    }

    return passed;
}





function checkCity(cityValue, el) {

    let pattern = /^[A-Za-z\s]{3,100}$/;

    let passed = pattern.test(cityValue);

    let errorEl = el
        .closest("form")
        .querySelector(".city-error");

    if (!passed) {
        errorEl.classList.add("show");
    } else {
        errorEl.classList.remove("show");
    }

    return passed;
}





function checkSkills(skillsValue, el) {

  
    let passed = skillsValue !== "";

    let errorEl = el
        .closest("form")
        .querySelector(".skills-error");

    if (!passed) {
        errorEl.classList.add("show");
    } else {
        errorEl.classList.remove("show");
    }

    return passed;
}