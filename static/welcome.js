 setTimeout(() => {
      document.body.classList.add("fade-out");

      setTimeout(() => {
        window.location.href = "/home";
      }, 1000); // wait for fade before redirect
    }, 3000);