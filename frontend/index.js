let button = document.querySelector(".btn")
let error = document.querySelector(".error")

button.addEventListener("click", () => {
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
    const formData = new FormData();

    formData.append('email', 'levenikeev0@gmail.com');
    formData.append('password', "idontkno8w1");
    console.log(formData)
    fetch('http://localhost:8000/register',
        {   mode: 'no-cors',
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            //data: JSON.stringify({ email: email.value, password:  password.value})
            body: formData
            //data: {"email":"levenikeev0@gmail.com","password":"idontkno8w1"}
        }
    )
    .then(function(res){ console.log(res) })
})