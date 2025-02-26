import React, { useEffect, useState } from "react";

const ArticleList = () => {
  const [clothingList, setClothingList] = useState(null);
  const [type, setType] = useState("");
  const [size, setSize] = useState("");
  const [genders, setGenders] = useState("");
  const [state, setState] = useState("");
  const [totalPages, setTotalPages] = useState(0);
  const [currentPage, setCurrentPage] = useState(1);
  const [error, setError] = useState(""); // Ajout de l'état d'erreur
  const limit = 10; // Ajout d'une variable limit pour la pagination

  const fetchClothing = async () => {
    const queryParams = new URLSearchParams({
      type,
      size,
      genders,
      state,
      page: currentPage,
      limit,
    });

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/list_articles/?${queryParams}`,
        {
          method: "GET",
          credentials: "include",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (!response.ok) {
        throw new Error("Erreur lors de la récupération des articles");
      }

      const data = await response.json();
      setClothingList(data);
      setTotalPages(data.totalPages);
      setError(""); // Réinitialiser l'erreur en cas de succès
    } catch (error) {
      console.error(error);
      setError(error.message); // Gérer l'erreur
    }
  };

  useEffect(() => {
    fetchClothing();
  }, [type, size, genders, state, currentPage]);

  const nextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(currentPage + 1);
    }
  };

  const prevPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  return (
    <div>
      <h1>Liste des articles</h1>
      {error && <div style={{ color: "red" }}>{error}</div>}{" "}
      {/* Affichage de l'erreur */}
      <label>
        Type :
        <select value={type} onChange={(e) => setType(e.target.value)}>
          <option value="">Tous</option>
          <option value="Hauts">Hauts</option>
          <option value="Accessoires">Accessoires</option>
          <option value="Bas">Bas</option>
          <option value="Vêtements de soirée">Vêtements de soirée</option>
          <option value="Déguisement">Déguisement</option>
          <option value="Vêtements de sport">Vêtements de sport</option>
        </select>
      </label>
      <label>
        Taille :
        <select value={size} onChange={(e) => setSize(e.target.value)}>
          <option value="">Toutes</option>
          <option value="XS">XS</option>
          <option value="S">S</option>
          <option value="M">M</option>
          <option value="L">L</option>
          <option value="XL">XL</option>
          <option value="XXL">XXL</option>
        </select>
      </label>
      <label>
        Genre :
        <select value={genders} onChange={(e) => setGenders(e.target.value)}>
          <option value="">Tous</option>
          <option value="Femme">Femme</option>
          <option value="Homme">Homme</option>
          <option value="Unisex">Unisexe</option>
        </select>
      </label>
      <label>
        État :
        <select value={state} onChange={(e) => setState(e.target.value)}>
          <option value="">Tous</option>
          <option value="Neuf">Neuf</option>
          <option value="Comme Neuf">Comme Neuf</option>
          <option value="Très bon état">Très bon état</option>
          <option value="Bon état">Bon état</option>
          <option value="Usé">Usé</option>
          <option value="Abimé">Abimé</option>
        </select>
      </label>
      <table>
        <thead>
          <tr>
            <th scope="col">Images</th>
            <th scope="col">Nom</th>
            <th scope="col">Description</th>
            <th scope="col">Type</th>
            <th scope="col">Taille</th>
            <th scope="col">Genre</th>
            <th scope="col">État</th>
            <th scope="col">Utilisateur</th>
          </tr>
        </thead>
        <tbody>
          {Array.isArray(clothingList) && clothingList.length > 0 ? (
            clothingList.map((clothing) => (
              <tr key={clothing.id}>
                <td>
                  {Array.isArray(clothing.pictures) &&
                    clothing.pictures.map((picture) => (
                      <img
                        key={picture.id}
                        src={picture.url}
                        alt={clothing.name}
                        width="100"
                        height="100"
                      />
                    ))}
                </td>
                <td>{clothing.name}</td>
                <td>{clothing.description}</td>
                <td>{clothing.type}</td>
                <td>{clothing.size}</td>
                <td>{clothing.genders}</td>
                <td>{clothing.state}</td>
                {clothing.user ? <td>{clothing.user.full_name}</td> : null}
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="8">Aucun article trouvé.</td>
            </tr>
          )}
        </tbody>
      </table>
      <div>
        <button disabled={currentPage === 1} onClick={prevPage}>
          Précédent
        </button>
        <span>
          Page {currentPage} sur {totalPages}
        </span>
        <button disabled={currentPage === totalPages} onClick={nextPage}>
          Suivant
        </button>
      </div>
    </div>
  );
};

export default ArticleList;
