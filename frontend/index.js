let button = document.querySelector(".btn")
let error = document.querySelector(".error")

button.addEventListener("click", async () => {
    error.style.display = 'none'
    email = document.querySelector("#email")
    password = document.querySelector("#psw")
    passwordRepeat = document.querySelector("#psw-repeat")
    if (password.value === "" || passwordRepeat.value === "" || email.value === "") {
        //error.textContent = 'Не все поля заполены'
        //error.style.display = ''
    }
    if (password.value !== passwordRepeat.value) {
        error.textContent = "Парроли не совпадают"
        error.style.display = ''
    }
    await fetch('http://localhost:8000/register',
        {   
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: email.value, password:  password.value})
        }
    )
    .then(function(res){ console.log(res) })
})