const API_URL = "http://127.0.0.1:8000";

// Fonction pour obtenir les tokens lors de la connexion
export const fetchToken = async (email, password) => {
  try {
    const response = await fetch(`${API_URL}/api/token/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Erreur lors de la connexion");
    }

    return data;
  } catch (error) {
    console.error("Erreur réseau :", error);
    throw new Error("Impossible de se connecter au serveur.");
  }
};

// Fonction pour rafraîchir le access token
export const refreshToken = async (refreshToken) => {
  const response = await fetch(`${API_URL}/api/token/refresh/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh: refreshToken }),
  });

  if (!response.ok) {
    throw new Error("Erreur lors du rafraîchissement du token");
  }

  return response.json();
};

// Fonction pour récupérer les infos utilisateur
export const getUserInfo = async (accessToken) => {
  const response = await fetch(`${API_URL}/auth/get_user/`, {
    method: "GET",
    headers: { Authorization: `Bearer ${accessToken}` },
  });

  if (!response.ok) {
    throw new Error(
      "Erreur lors de la récupération des informations utilisateur"
    );
  }

  return response.json();
};
