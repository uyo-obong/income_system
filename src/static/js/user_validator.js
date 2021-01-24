const usernameField = document.querySelector('#f-username')
const emailField = document.querySelector('#f-email')
const passwordField = document.querySelector('#f-password')
const usernameErrorField = document.querySelector('.username-error')
const emailErrorField = document.querySelector('.email-error')
const togglePassword = document.querySelector('.toggle-password')

const handleToggle = (e) => {
    if (togglePassword.textContent === 'SHOW') {
        togglePassword.textContent = 'HIDE'
        passwordField.setAttribute('type', 'text')
    } else {
        togglePassword.textContent = 'SHOW'
          passwordField.setAttribute('type', 'password')
    }
}

togglePassword.addEventListener('click', handleToggle)

emailField.addEventListener('keyup', (e) => {
    const email = e.target.value

    emailField.classList.remove("is-invalid")
    emailErrorField.style.display = 'none'

    if (email.length > 0) {
        fetch('/auth/validate/email', {
            body: JSON.stringify({email:email}),
            method: 'POST',
        }).then((res) => res.json()).then((data) => {

            if (data.email_error) {
                emailField.classList.add("is-invalid")
                emailErrorField.style.display = 'block'
                emailErrorField.innerHTML= `${data.email_error}`
            } else {
                console.log(data)
                emailField.classList.add("is-valid")
            }
        })
    }
})



usernameField.addEventListener('keyup', (e) => {
    const username = e.target.value

    usernameField.classList.remove("is-invalid")
    usernameErrorField.style.display = 'none'

    if (username.length > 0) {
        fetch('/auth/validate/username', {
            body: JSON.stringify({username:username}),
            method: 'POST',
        }).then((res) => res.json()).then((data) => {
            if (data.username_error) {
                usernameField.classList.add("is-invalid")
                usernameErrorField.style.display = 'block'
                usernameErrorField.innerHTML= `${data.username_error}`
            } else {
                usernameField.classList.add("is-valid")
            }
        })
    }
})



