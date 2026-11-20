// Envoi du formulaire de contact via le service configuré dans js/config.js
var f = document.getElementById("contact-form");
if (f) f.addEventListener("submit", function (e) {
  e.preventDefault();
  var msg = document.getElementById("msg"), url = (window.ASE_CONFIG || {}).formEndpoint;
  if (f.website.value) return; // anti-spam (champ piège)
  if (!url) { msg.textContent = "Le formulaire n’est pas encore configuré (voir README.md)."; return; }
  fetch(url, {method: "POST", body: new FormData(f), headers: {Accept: "application/json"}})
    .then(function (r) { if (!r.ok) throw 0; f.reset(); msg.textContent = "Merci, votre message a bien été envoyé."; })
    .catch(function () { msg.textContent = "L’envoi a échoué. Merci de réessayer plus tard."; });
});
