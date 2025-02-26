import { createContext, useState, useContext } from "react";
import { fetchToken, refreshToken, getUserInfo } from "./api";

// Création du contexte
const AuthContext = createContext();

// Hook personnalisé pour utiliser le contexte
export const useAuth = () => useContext(AuthContext);

// Fournisseur de contexte (AuthProvider)
export const AuthProvider = ({ children }) => {
  const [accessToken, setAccessToken] = useState(null);
  const [refreshTokenValue, setRefreshTokenValue] = useState(null);
  const [user, setUser] = useState(null);

  // Fonction pour se connecter
  const login = async (email, password) => {
    const data = await fetchToken(email, password);
    if (data.access && data.refresh) {
      setAccessToken(data.access);
      setRefreshTokenValue(data.refresh);
      const userInfo = await getUserInfo(data.access);
      setUser(userInfo);
    }
  };

  // Fonction pour rafraîchir le token
  const refreshAccessToken = async () => {
    if (!refreshTokenValue) return;
    const data = await refreshToken(refreshTokenValue);
    if (data.access) {
      setAccessToken(data.access);
    }
  };

  // Fonction pour se déconnecter
  const logout = () => {
    setAccessToken(null);
    setRefreshTokenValue(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{ accessToken, user, login, logout, refreshAccessToken }}
    >
      {children}
    </AuthContext.Provider>
  );
};
