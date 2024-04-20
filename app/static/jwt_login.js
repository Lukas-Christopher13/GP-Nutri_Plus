function fazerLogin() {
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;

  // Faz uma requisição para o servidor Flask
  fetch('/login', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username: username, password: password })
  })
  .then(response => {
      if (!response.ok) {
          throw new Error('Erro ao fazer login.');
      }
      return response.json();
  })
  .then(data => {
      // Armazena o token JWT na localStorage
      localStorage.setItem('jwt_token', data.access_token);
      // Redireciona para outra página, por exemplo, a página protegida
      window.location.href = '/pagina-protegida';
  })
  .catch(error => {
      console.error('Erro:', error);
  });
}