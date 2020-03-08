var profile;

$(document).ready(function () {
    $.when(get_user_profile(localStorage.getItem("email")).done(() => {
        /* Change DOM content */
        document.querySelector('input[name="first-name"]').value =
            localStorage.getItem("first_name");
        document.querySelector('input[name="last-name"]').value =
            localStorage.getItem("last_name");
        document.querySelector('input[name="email"]').value = localStorage.getItem("email");

        // DOB
        const d = new Date(profile.date_of_birth);
        const ye = new Intl.DateTimeFormat('en', {year: 'numeric'}).format(d);
        const mo = new Intl.DateTimeFormat('en', {month: '2-digit'}).format(d);
        const da = d.getUTCDate();
        document.querySelector('input[name="dob"]').value = `${ye}-${mo}-${da}`;

        // Gender
        let optionExist = document.querySelector(
            `select[name="gender"] option[value="${profile.gender}"]`
        );
        if (optionExist) {
            document.querySelector('select[name="gender"]').value = profile.gender;
        } else {
            document.querySelector('select[name="gender"]').value = 'null';
        }

        /* Listeners */
        // Update any setting once there is a change.
        var settingItem = $("select.custom-select.custom-select-sm.d-table.float-right")
            .map(function () {
                $(this).change(function () {
                    const key = this.name;
                    const val = $(this).val();
                    updateSetting(key, val);
                });
            });

        // Edit profile button
        const editProfileBtn = document.querySelector('#edit-profile');

        editProfileBtn.addEventListener('click', a => {
            // When it is an Edit button.
            if (editProfileBtn.classList.contains('btn-primary')) {
                // Button
                editProfileBtn.classList.add('btn-info');
                editProfileBtn.classList.remove('btn-primary');
                editProfileBtn.innerText = 'Save';

                // Enable fields
                document.querySelectorAll('input, select').forEach(field => {
                    if (field.name != 'email') {
                        field.disabled = false;
                    }
                });
            } else {
                // When it is a Save button.
                // Check if fields values are valid.
                let validSave = true;
                document.querySelectorAll('input, select').forEach(field => {
                    // Reset invalid style
                    field.classList.remove('invalid');

                    if (field.value.length == 0) {
                        validSave = false;
                        field.classList.add('invalid');
                    }
                });

                if (validSave) {
                    // Button
                    editProfileBtn.classList.add('btn-primary');
                    editProfileBtn.classList.remove('btn-info');
                    editProfileBtn.innerText = 'Edit';

                    // Disable fields
                    document.querySelectorAll('input, select').forEach(field => {
                        field.disabled = true;
                    });

                    // Send to server
                    let firstName = document.querySelector('input[name="first-name"]')
                        .value;
                    let lastName = document.querySelector('input[name="last-name"]')
                        .value;
                    let DOB = document.querySelector('input[name="dob"]').value;
                    let gender = document.querySelector('select[name="gender"]').value;
                    let email = document.querySelector('input[name="email"]').value;

                    saveProfile(firstName, lastName, DOB, gender, email);
                } else {
                    console.log('Invalid');
                }
            }
        });
    }));

});

/* Functions */
function chat(profile) {
    console.log('TODO: chat with profile user');
}

// AJAX Login
// function login () {
//   return $.ajax ({
//     type: 'POST',
//     url: '/login',
//     // The key needs to match your method's input parameter (case-sensitive).
//     data: JSON.stringify ({
//       token_id: 'asd',
//       email: 'at@te.com',
//     }),
//     contentType: 'application/json; charset=utf-8',
//     dataType: 'json',
//     success: data => {
//       console.log (`Login: ${data.login_success}`);
//     },
//     failure: function (errMsg) {
//       console.log (`Login failed: ${errMsg}`);
//     },
//   });
// }

// Retrieve User Profile
function get_user_profile(email) {
    return $.get(`/user/email/${email}`, function (
        data,
        status
    ) {
        console.log(`Retrieve user profile: ${status}`);
        profile = data.profile;
        console.log(data);
    });
}

// Save Profile
function saveProfile(firstName, lastName, DOB, gender, email) {
    return $.ajax({
        type: 'POST',
        url: '/user/profile',
        // The key needs to match your method's input parameter (case-sensitive).
        data: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            date_of_birth: DOB,
            gender: gender,
            email: email,
        }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: data => {
            console.log(`Create profile: ${data.create_profile_success}`);
        },
        failure: function (errMsg) {
            console.log(`Create profile failed: ${errMsg}`);
        },
    });
}


function updateSetting(name, value) {
    const key = name;
    const returnObj = {};
    returnObj["email"] = profile.email;

    // Currently we only allow update a pair of key
    returnObj[key] = value;


    return $.ajax({
        type: 'POST',
        url: '/user/settings',

        // The key needs to match your method's input parameter (case-sensitive).
        data: JSON.stringify(returnObj),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: data => {
            console.log(`Update setting: ${data.login_success}`);
        },
        failure: function (errMsg) {
            console.log(`Update setting failed: ${errMsg}`);
        },
    });
}


function signOut() {
    return $.ajax({
        type: 'POST',
        url: '/signout',
        success: data => {
            localStorage.clear();
            console.log(`Signout: ${data.signout}`);
            location.replace("/index.html");
        },
        failure: function (errMsg) {
            console.log(`Update setting failed: ${errMsg}`);
        },
    });
}