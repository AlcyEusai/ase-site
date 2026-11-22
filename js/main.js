// Envoi des formulaires (contact, newsletter) vers les services configurés dans js/config.js
document.querySelectorAll("form.aseform").forEach(function (f) {
  f.addEventListener("submit", function (e) {
    e.preventDefault();
    var msg = f.parentNode.querySelector(".fmsg"), url = (window.ASE_CONFIG || {})[f.dataset.key];
    if (f.website && f.website.value) return; // anti-spam (champ piège)
    if (!url) { msg.textContent = "Ce formulaire n’est pas encore configuré (voir README.md)."; return; }
    fetch(url, {method: "POST", body: new FormData(f), headers: {Accept: "application/json"}})
      .then(function (r) { if (!r.ok) throw 0; f.reset(); msg.textContent = "Merci, votre message a bien été envoyé."; })
      .catch(function () { msg.textContent = "L’envoi a échoué. Merci de réessayer plus tard."; });
  });
});
