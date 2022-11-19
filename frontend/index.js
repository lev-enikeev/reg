let button = document.querySelector(".btn")
let error = document.querySelector(".error")

button.addEventListener("click", () => {
    error.style.display = 'none'
    email = document.querySelector("#email")
    password = document.querySelector("#psw")
    passwordRepeat = document.querySelector("#psw-repeat")
    if (password.value === "" || passwordRepeat.value === "" || email.value === "") {
        error.textContent = 'Не все поля заполены'
        error.style.display = ''
    }
    if (password.value !== passwordRepeat.value) {
        error.textContent = "Парроли не совпадают"
        error.style.display = ''
    }
    fetch('http://localhost:8000',
        {
            mode: 'no-cors',
        })
        .then(function (res) { console.log(res.json()) })
    // fetch('http://localhost:8000/register',
    //     {   mode: 'no-cors',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         },
    //         method: "POST",
    //         data: JSON.stringify({ email: email.value, password:  password.value})
    //     }
    // )
    // .then(function(res){ console.log(res) })
})