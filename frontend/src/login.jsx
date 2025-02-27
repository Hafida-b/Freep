import { useState } from "react";
import { useAuth } from "./auth";

const Login = () => {
  const { login, user } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    setErrorMessage("");

    try {
      await login(email, password);
    } catch (error) {
      setErrorMessage(error.message);
      console.error("Échec de connexion :", error);
    }
  };

  return (
    <div>
      {user ? (
        <p>Bienvenue {user.username} !</p>
      ) : (
        <form onSubmit={handleLogin}>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            placeholder="Mot de passe"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button type="submit">Se connecter</button>
          {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
        </form>
      )}
    </div>
  );
};

export default Login;
